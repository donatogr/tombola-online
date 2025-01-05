import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WebSocketService {
  private socket: WebSocket | null = null;
  private gameUpdates = new Subject<any>();

  gameUpdates$ = this.gameUpdates.asObservable();

  connectToGame(gameId: number) {
    this.socket = new WebSocket(`ws://${environment.wsUrl}/ws/game/${gameId}/`);

    this.socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'game_update') {
        this.gameUpdates.next(data);
      }
    };

    this.socket.onclose = () => {
      console.log('WebSocket connection closed');
    };
  }

  disconnect() {
    if (this.socket) {
      this.socket.close();
      this.socket = null;
    }
  }
} 