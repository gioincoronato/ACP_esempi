ARCHITETTURA DELL'ESEMPIO MONGODB + PYTHON
1. CHI FA DA SERVER? Il server NON è un file che abbiamo creato noi. Il ruolo di Server è svolto dal servizio di sistema mongod (MongoDB Daemon).
È un software installato sulla macchina virtuale che gira in background (attivato con systemctl start mongod).
Il suo compito è ascoltare le richieste sulla porta 27017, gestire la memoria e scrivere fisicamente i dati sul disco rigido.

2. CHI È IL CLIENT? Il Client è il nostro script Python (main.py).
Utilizza la libreria PyMongo  per "telefonare" al server (sulla porta 27017) e inviargli i comandi.
Il codice MongoClient("mongodb://127.0.0.1:27017") serve proprio a stabilire questo ponte .

3. CHI CREA IL DATABASE? La creazione è gestita dal Server, ma è innescata dal Client Python.
In MongoDB vige la regola della "Lazy Creation" (Creazione Pigra).
Non esiste un comando CREATE DATABASE esplicito.
Nel codice Python scriviamo client['test'] e poi insert_many(...).
Nel momento esatto in cui Python invia i dati, il Server controlla: "Esiste il DB 'test'? No". Allora lo crea all'istante, crea la collection user_1_items e ci salva dentro i dati.

4. DOVE SI CONSULTA IL DATABASE? I dati NON si trovano in un file leggibile (come un .txt o un .xml) nella nostra cartella.
Il Server li salva in formato binario (BSON) in cartelle di sistema protette (solitamente /var/lib/mongodb), inaccessibili all'utente normale.
Per consultarli, dobbiamo usare un client. Abbiamo due modi:
Via Codice: Scrivendo un altro script Python che usa find().
Via Shell (Terminale): Usando il comando mongosh. Questo è il metodo più veloce per una verifica manuale.

PROCEDURA DI VERIFICA (SHELL):
Aprire il terminale e digitare: mongosh
Visualizzare i dbs: show dbs
Selezionare il DB creato: use test
Leggere i dati: db.user_1_items.find()