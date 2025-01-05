from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Game, Card
from .serializers import GameSerializer, CardSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.permissions import AllowAny

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['post'])
    def extract_number(self, request, pk=None):
        game = self.get_object()
        number = game.extract_number()
        if number is None:
            return Response(
                {"error": "No more numbers available"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Controlla le vincite per tutte le cartelle del gioco
        wins = {}
        for card in game.card_set.all():
            card_wins = card.check_wins()
            if card_wins:
                wins[card.id] = card_wins

        # Notifica tutti i client tramite WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'game_{game.id}',
            {
                'type': 'game_update',
                'number': number,
                'wins': wins
            }
        )

        return Response({
            "number": number,
            "wins": wins
        })

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], url_path='generate')
    def generate(self, request):
        game_id = request.data.get('game_id')
        try:
            game = Game.objects.get(id=game_id)
            if request.user.is_authenticated:
                card = Card.create_card(request.user, game)
            else:
                card = Card.objects.create(
                    game=game,
                    numbers=Card.generate_card_numbers()
                )
            serializer = self.get_serializer(card)
            return Response(serializer.data)
        except Game.DoesNotExist:
            return Response(
                {"error": "Game not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=['get'])
    def check_wins(self, request, pk=None):
        card = self.get_object()
        wins = card.check_wins()
        return Response({"wins": wins}) 