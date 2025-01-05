import { Component, OnInit, OnDestroy } from '@angular/core';
import { GameService } from '../../services/game.service';
import { WebSocketService } from '../../services/websocket.service';
import { Game, Card } from '../../models/game.model';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit, OnDestroy {
  // Definisci il tipo per i messaggi di vincita
  private readonly winMessages: { [key: string]: string } = {
    'ambo': 'Hai fatto AMBO!',
    'terno': 'Hai fatto TERNO!',
    'quaterna': 'Hai fatto QUATERNA!',
    'cinquina': 'Hai fatto CINQUINA!',
    'tombola': 'TOMBOLA! Hai vinto!'
  };

  currentGame: Game = {
    id: 0,
    status: 'inactive',
    current_number: 0,
    extracted_numbers: []
  };
  playerCard: Card | null = null;
  private wsSubscription: Subscription | null = null;
  wins: string[] = [];
  
  constructor(
    private gameService: GameService,
    private wsService: WebSocketService
  ) {}

  ngOnInit() {
    this.startNewGame();
  }

  ngOnDestroy() {
    if (this.wsSubscription) {
      this.wsSubscription.unsubscribe();
    }
    this.wsService.disconnect();
  }

  startNewGame() {
    this.gameService.createGame().subscribe(game => {
      this.currentGame = game;
      this.wsService.connectToGame(game.id);
      this.wsSubscription = this.wsService.gameUpdates$.subscribe(update => {
        this.currentGame.current_number = update.number;
        
        // Gestisce le vincite
        if (update.wins && this.playerCard) {
          const cardWins = update.wins[this.playerCard.id];
          if (cardWins) {
            this.wins = [...this.wins, ...cardWins];
            this.announceWins(cardWins);
          }
        }
      });
      this.generateCard();
    });
  }

  generateCard() {
    this.gameService.generateCard(this.currentGame.id).subscribe(card => {
      this.playerCard = card;
    });
  }

  extractNumber() {
    this.gameService.extractNumber(this.currentGame.id).subscribe(response => {
      this.currentGame.current_number = response.number;
      this.currentGame.extracted_numbers.push(response.number);
    });
  }

  announceWins(wins: string[]) {
    wins.forEach(win => {
      alert(this.winMessages[win]);
    });
  }
} 