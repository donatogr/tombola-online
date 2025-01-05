from rest_framework import serializers
from .models import Game, Card

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'status', 'current_number', 'extracted_numbers', 'created_at']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'user', 'game', 'numbers', 'created_at'] 