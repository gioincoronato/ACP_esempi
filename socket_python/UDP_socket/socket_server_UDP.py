import socket

# utilizziamo UDP, versione meno affidabile ma più veloce di TCP

# messaggio di risposta dal server
msg = "messaggio di risposta dal server "

# configurazione porta
server_address_port = ('localhost', 7000)
BUFF_SIZE = 1024

# creazione socket UDP
# SOCK_DGRAM per UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# binding del server per dichiarare dove ricevere i pacchetti
s.bind(server_address_port)
print("Server in ascolto per pacchetti UDP ")

# otteniamo dati e indirizzo del client
# utilizzo utf-8 per l'encode e decode
msg_client, addr = s.recvfrom(BUFF_SIZE)
print("SERVER| messaggio ricevuto: " + msg_client.decode("utf-8"))
print(f"SERVER| indirizzo client: {addr} ")

# utilizziamo l'indirizzo appena ottenuto per inviare dati al client
print("SERVER| invio messaggio di risposta al client ")
s.sendto(msg.encode("utf-8"), addr)

# chiudo la connessione
s.close()