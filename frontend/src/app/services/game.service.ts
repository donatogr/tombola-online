import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Game, Card } from '../models/game.model';

@Injectable({
  providedIn: 'root'
})
export class GameService {
  private apiUrl = '/api';
  private httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    }),
    withCredentials: true
  };

  constructor(private http: HttpClient) { }

  createGame(): Observable<Game> {
    return this.http.post<Game>(`${this.apiUrl}/games/`, {}, this.httpOptions);
  }

  extractNumber(gameId: number): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/games/${gameId}/extract_number/`, {}, this.httpOptions);
  }

  generateCard(gameId: number): Observable<Card> {
    return this.http.post<Card>(`${this.apiUrl}/cards/generate/`, { game_id: gameId }, this.httpOptions);
  }
} 