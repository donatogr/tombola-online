# Tombola Online

Applicazione web multiplayer per giocare alla tombola in tempo reale.

## Tecnologie Utilizzate

- Backend: Django + Django REST Framework + Channels
- Frontend: Angular 17
- Database: PostgreSQL
- WebSocket: Redis
- Container: Docker e Docker Compose

## Documentazione

- [Documentazione Tecnica](DOCUMENTATION.md)
- [Manuale Utente](USER_MANUAL.md)

## Requisiti

- Docker
- Docker Compose
- 2GB RAM minimo
- 10GB spazio disco

## Installazione

1. Clona il repository:
```bash
git clone https://github.com/tuousername/tombola-online.git
cd tombola-online
```

2. Avvia l'applicazione:
```bash
docker-compose up --build
```

3. Accedi all'applicazione:
- Frontend: http://localhost
- Backend: http://localhost:8000
- Admin: http://localhost/admin

## Sviluppo

Per avviare l'ambiente di sviluppo:

```bash
# Frontend
cd frontend
npm install
ng serve

# Backend
cd backend
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate su Windows
pip install -r requirements.txt
python manage.py runserver
```

## Licenza

MIT License 