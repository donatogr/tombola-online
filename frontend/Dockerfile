# Stage 1: Build
FROM node:20-slim as builder

WORKDIR /app

# Copia package.json e package-lock.json
COPY package*.json ./

# Installa le dipendenze
RUN npm install

# Copia tutti i file necessari
COPY . .

# Compila l'applicazione
RUN npm run build

# Stage 2: Runtime
FROM nginx:alpine

# Copia i file compilati nella directory di nginx
COPY --from=builder /app/dist/tombola /usr/share/nginx/html

# Copia la configurazione di nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80 