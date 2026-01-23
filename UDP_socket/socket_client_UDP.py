import socket

# configuro messaggi, porta e dim
msg = "messaggio dal client verso il server"
server_address_port = ('localhost', 7000)
BUFF_SIZE = 1024

# creazioe socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# invio messaggi al server
print("CLIENT| invio messaggio al server ")
s.sendto(msg.encode("utf-8"), server_address_port)

# ricezione risposta dal server
msg_server, addr = s.recvfrom(BUFF_SIZE)
print("CLIENT| risposta da parte del server: " + msg_server.decode("utf-8"))

# chiudo la connessione
s.close()