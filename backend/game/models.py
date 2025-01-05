from django.db import models
from django.contrib.auth.models import User
import random

class Game(models.Model):
    WINS = {
        'ambo': 2,
        'terno': 3,
        'quaterna': 4,
        'cinquina': 5,
        'tombola': 15
    }
    
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='active')
    current_number = models.IntegerField(null=True, blank=True)
    extracted_numbers = models.JSONField(default=list)
    winners = models.JSONField(default=dict)  # {'ambo': [user_id], 'terno': [], ...}

    def __str__(self):
        return f"Game {self.id} - {self.status}"

    def extract_number(self):
        available_numbers = [n for n in range(1, 91) if n not in self.extracted_numbers]
        if not available_numbers:
            return None
        number = random.choice(available_numbers)
        self.current_number = number
        self.extracted_numbers.append(number)
        self.save()
        return number

    def check_win(self, card, win_type):
        if win_type not in self.WINS:
            return False
        
        # Verifica se qualcuno ha già vinto questo tipo
        if win_type in self.winners and card.user.id in self.winners[win_type]:
            return False

        numbers_needed = self.WINS[win_type]
        extracted_set = set(self.extracted_numbers)

        # Per la tombola controlliamo tutta la cartella
        if win_type == 'tombola':
            total_matches = sum(
                1 for row in card.numbers 
                for num in row 
                if num != 0 and num in extracted_set
            )
            return total_matches == numbers_needed

        # Per le altre vincite controlliamo riga per riga
        for row in card.numbers:
            matches = sum(1 for num in row if num != 0 and num in extracted_set)
            if matches == numbers_needed:
                # Aggiorna i vincitori
                if win_type not in self.winners:
                    self.winners[win_type] = []
                self.winners[win_type].append(card.user.id)
                self.save()
                return True

        return False

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    numbers = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    wins = models.JSONField(default=list)  # ['ambo', 'terno', ...]

    def __str__(self):
        return f"Card {self.id} - Game {self.game.id}"

    def check_wins(self):
        new_wins = []
        for win_type in Game.WINS:
            if win_type not in self.wins and self.game.check_win(self, win_type):
                self.wins.append(win_type)
                new_wins.append(win_type)
        if new_wins:
            self.save()
        return new_wins

    @staticmethod
    def generate_card_numbers():
        # Una cartella della tombola ha 3 righe e 9 colonne
        # Ogni riga deve avere 5 numeri
        numbers = []
        for row in range(3):
            row_numbers = []
            # Per ogni colonna (1-9) scegliamo un numero nel range appropriato
            available_positions = random.sample(range(9), 5)  # 5 posizioni per riga
            for col in range(9):
                if col in available_positions:
                    # Calcola il range per questa colonna
                    min_num = col * 10 + 1
                    max_num = min_num + 9 if col < 8 else 91
                    number = random.randint(min_num, max_num)
                    row_numbers.append(number)
                else:
                    row_numbers.append(0)  # 0 rappresenta una cella vuota
            numbers.append(row_numbers)
        return numbers

    @classmethod
    def create_card(cls, user, game):
        numbers = cls.generate_card_numbers()
        return cls.objects.create(
            user=user,
            game=game,
            numbers=numbers
        ) 