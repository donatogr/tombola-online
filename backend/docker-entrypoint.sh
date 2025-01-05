#!/bin/bash

# Attende che il database Redis sia pronto
until nc -z redis 6379; do
    echo "Waiting for Redis..."
    sleep 1
done

# Attende che PostgreSQL sia pronto
until nc -z db 5432; do
    echo "Waiting for PostgreSQL..."
    sleep 1
done

# Crea le migrazioni
python manage.py makemigrations game

# Applica le migrazioni
python manage.py migrate

# Raccoglie i file statici
python manage.py collectstatic --noinput

# Crea il superuser se non esiste
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

# Avvia il server
python manage.py runserver 0.0.0.0:8000 