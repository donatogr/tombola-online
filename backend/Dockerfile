FROM python:3.11-slim

WORKDIR /app

# Installa le dipendenze di sistema necessarie
RUN apt-get update && apt-get install -y \
    gcc \
    netcat-traditional \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copia i requisiti e installa le dipendenze Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Crea la directory per i file statici
RUN mkdir -p /app/static /app/staticfiles

# Copia il codice dell'applicazione
COPY . .

# Espone la porta per il server
EXPOSE 8000

# Script di avvio
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"] 