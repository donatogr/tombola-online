from django.contrib import admin
from .models import Game, Card

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'current_number', 'created_at')
    list_filter = ('status',)
    search_fields = ('id', 'status')

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'game', 'created_at')
    list_filter = ('game',)
    search_fields = ('user__username', 'game__id') 