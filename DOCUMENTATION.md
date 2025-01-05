# Documentazione Tecnica - Tombola Online

## 1. Panoramica del Sistema
Tombola Online è un'applicazione web multiplayer che permette di giocare alla tombola in tempo reale. Il sistema è composto da:
- Backend: Django + Django REST Framework + Channels
- Frontend: Angular 17
- Database: PostgreSQL
- WebSocket: Redis per la gestione delle connessioni real-time
- Container: Docker e Docker Compose per l'orchestrazione

## 2. Architettura

### 2.1 Backend (Django)

#### Modelli principali
```python
class Game:
    status: str              # Stato del gioco (active/completed)
    current_number: int      # Ultimo numero estratto
    extracted_numbers: list  # Lista numeri estratti
    winners: dict           # Vincitori per tipo di vincita

class Card:
    user: ForeignKey        # Riferimento all'utente
    game: ForeignKey        # Riferimento alla partita
    numbers: JSONField      # Matrice 3x9 dei numeri
    wins: list             # Lista delle vincite ottenute
```

#### API Endpoints
```
POST /api/games/                    # Crea nuova partita
POST /api/games/{id}/extract_number # Estrae nuovo numero
POST /api/cards/generate/           # Genera nuova cartella
POST /api/auth/login/              # Autenticazione utente
```

### 2.2 Frontend (Angular)

#### Componenti principali
```typescript
// GameComponent
- Gestione partita
- Visualizzazione cartella
- Estrazione numeri
- Gestione vincite

// LoginComponent
- Autenticazione utente
- Gestione sessione
```

#### Servizi
```typescript
// GameService
- Comunicazione con API backend
- Gestione stato partita

// WebSocketService
- Gestione connessione WebSocket
- Aggiornamenti real-time

// AuthService
- Gestione autenticazione
- JWT token management
```

## 3. Funzionalità Principali

### 3.1 Gestione Partita
- Creazione nuova partita
- Estrazione numeri casuali
- Verifica vincite (ambo, terno, quaterna, cinquina, tombola)
- Aggiornamenti in tempo reale via WebSocket

### 3.2 Gestione Cartelle
- Generazione automatica cartelle
- Verifica numeri estratti
- Marcatura automatica dei numeri
- Calcolo vincite

### 3.3 Sistema di Vincite
```python
WINS = {
    'ambo': 2,      # Due numeri sulla stessa riga
    'terno': 3,     # Tre numeri sulla stessa riga
    'quaterna': 4,  # Quattro numeri sulla stessa riga
    'cinquina': 5,  # Cinque numeri sulla stessa riga
    'tombola': 15   # Tutti i numeri della cartella
}
```

## 4. Configurazione Docker

### 4.1 Servizi
```yaml
services:
  backend:    # Server Django
  frontend:   # Server Angular/Nginx
  redis:      # Gestione WebSocket
  db:         # Database PostgreSQL
```

### 4.2 Networks
- `tombola-network`: Rete interna per la comunicazione tra container

### 4.3 Volumes
- `postgres_data`: Persistenza dati PostgreSQL
- `redis_data`: Persistenza dati Redis

## 5. Sicurezza

### 5.1 Autenticazione
- JWT (JSON Web Token) per l'autenticazione API
- Sessioni utente gestite lato client
- Token refresh automatico

### 5.2 CORS
```python
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost",
    "http://localhost:80"
]
```

## 6. WebSocket

### 6.1 Connessione
```typescript
connectToGame(gameId: number) {
    this.socket = new WebSocket(`ws://${environment.wsUrl}/ws/game/${gameId}/`);
}
```

### 6.2 Eventi
- `game_update`: Aggiornamento numeri estratti
- `win_notification`: Notifica vincite

## 7. Deployment

### 7.1 Requisiti
- Docker
- Docker Compose
- 2GB RAM minimo
- 10GB spazio disco

### 7.2 Comandi principali
```bash
# Avvio applicazione
docker-compose up --build

# Stop applicazione
docker-compose down

# Logs
docker-compose logs -f [service_name]
```

## 8. Testing

### 8.1 Backend
```bash
python manage.py test
```

### 8.2 Frontend
```bash
ng test
```

## 9. Manutenzione

### 9.1 Database
- Backup automatico PostgreSQL
- Pulizia dati obsoleti
- Monitoraggio performance

### 9.2 Logging
- Log applicativi in `/var/log/`
- Log Docker tramite `docker-compose logs`
- Monitoraggio errori e performance

## 10. Scalabilità
- Architettura containerizzata per facile scaling
- WebSocket per gestione real-time
- Cache Redis per ottimizzazione performance
