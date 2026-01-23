import socket

# parametri di rete
IP = 'localhost'
PORT = 47913 # qui va messo il numero di porta dato dal server
BUFF_SIZE = 1024

# creo la socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# apro il canale verso il server
s.connect((IP, PORT))

# invio dati verso il server
message = "messaggio inviato dal client verso il server"
s.send(message.encode("utf-8"))

# aspetto la ricezione dei dati dal server
data = s.recv(BUFF_SIZE)
print("risposta dal server: " + data.decode("utf-8"))

# chiudo la connessione
s.close()