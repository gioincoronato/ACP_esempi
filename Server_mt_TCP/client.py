import socket
IP = 'localhost'
PORT = 12345
BUFF_SIZE = 1024

# creazione e connessione al server della socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

# mando un messaggio al server
messaggio = "inverti questo messaggio 16 "
print(" Cient invia messaggio al server ")
s.send(messaggio.encode("utf-8"))

# ricevo e stampo la risp inviata dal server
risp = s.recv(BUFF_SIZE)
print("il server mi ha mandato: " +risp.decode("utf-8"))

# chiudo la connessione
s.close()
