# Manuale Utente - Tombola Online

## 1. Introduzione
Tombola Online è un'applicazione web che permette di giocare alla tombola tradizionale in modalità multiplayer. Gli utenti possono partecipare a partite in tempo reale, acquistare cartelle e competere per vincite come ambo, terno, quaterna, cinquina e tombola.

## 2. Come Iniziare

### 2.1 Accesso al Sistema
1. Apri il browser e vai su `http://localhost`
2. Per accedere come utente registrato:
   - Clicca su "Login" in alto a destra
   - Inserisci username e password
   - Clicca su "Login"
3. Per giocare come ospite, puoi procedere direttamente senza login

### 2.2 Interfaccia Principale
L'interfaccia di gioco è composta da:
- **Tabellone**: Mostra tutti i numeri da 1 a 90
- **Numero Corrente**: Visualizza l'ultimo numero estratto
- **Le tue Cartelle**: Mostra le cartelle in tuo possesso
- **Pulsanti di Controllo**: Per estrarre numeri e gestire il gioco

## 3. Come Giocare

### 3.1 Creare una Nuova Partita
1. Clicca su "Nuova Partita"
2. La partita viene creata e ti viene assegnato un ID partita
3. Puoi condividere questo ID con altri giocatori

### 3.2 Generare una Cartella
1. Clicca su "Genera Cartella"
2. Una nuova cartella viene generata automaticamente
3. La cartella contiene:
   - 3 righe
   - 9 colonne
   - 5 numeri per riga
   - Numeri distribuiti secondo le regole della tombola

### 3.3 Durante il Gioco
1. **Estrazione Numeri**:
   - Clicca "Estrai Numero" per estrarre un nuovo numero
   - Il numero estratto viene evidenziato sul tabellone
   - I numeri presenti sulle cartelle vengono marcati automaticamente

2. **Vincite**:
   - Le vincite vengono verificate automaticamente
   - Riceverai una notifica quando realizzi una vincita
   - Tipi di vincite possibili:
     * Ambo (2 numeri sulla stessa riga)
     * Terno (3 numeri sulla stessa riga)
     * Quaterna (4 numeri sulla stessa riga)
     * Cinquina (5 numeri sulla stessa riga)
     * Tombola (tutti i numeri della cartella)

## 4. Funzionalità Speciali

### 4.1 Aggiornamenti in Tempo Reale
- Tutti i giocatori vedono le estrazioni in tempo reale
- Le cartelle si aggiornano automaticamente
- Le vincite vengono notificate immediatamente

### 4.2 Verifica Automatica
- Il sistema verifica automaticamente le vincite
- Non è necessario chiamare manualmente "Ambo", "Terno", ecc.
- Le vincite vengono registrate nell'ordine corretto

## 5. Gestione Partita

### 5.1 Visualizzazione Stato
- **Numeri Estratti**: Lista di tutti i numeri già estratti
- **Vincite Realizzate**: Elenco delle tue vincite nella partita
- **Stato Cartelle**: Visualizzazione dei numeri marcati

### 5.2 Fine Partita
- La partita termina quando viene realizzata la tombola
- Viene mostrato un riepilogo delle vincite
- È possibile iniziare una nuova partita

## 6. Risoluzione Problemi

### 6.1 Problemi Comuni
1. **Pagina non si aggiorna**:
   - Ricarica la pagina
   - Verifica la connessione internet

2. **Numeri non si marcano**:
   - Controlla la connessione WebSocket
   - Ricarica la pagina

3. **Errori di Login**:
   - Verifica le credenziali
   - Contatta l'amministratore se persiste

### 6.2 Supporto
Per assistenza tecnica:
- Email: support@tombola-online.com
- Orari: Lun-Ven 9:00-18:00

## 7. Requisiti Tecnici
- Browser web moderno (Chrome, Firefox, Safari, Edge)
- Connessione internet stabile
- JavaScript abilitato
- Cookie abilitati

## 8. Privacy e Sicurezza
- I dati personali sono protetti
- Le connessioni sono sicure
- Le partite sono monitorate per fairplay

## 9. Suggerimenti
- Tieni d'occhio i numeri estratti
- Puoi giocare con più cartelle contemporaneamente
- Usa la funzione di auto-marcatura per non perdere numeri
- Mantieni una connessione internet stabile

## 10. Glossario
- **Ambo**: Due numeri sulla stessa riga
- **Terno**: Tre numeri sulla stessa riga
- **Quaterna**: Quattro numeri sulla stessa riga
- **Cinquina**: Cinque numeri sulla stessa riga
- **Tombola**: Tutti i numeri della cartella 