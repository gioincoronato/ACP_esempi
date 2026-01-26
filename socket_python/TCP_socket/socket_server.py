import socket

# utilizziamo la socket TCP per la comunicazione sicura tra processi

#imposto i parametri di rete
IP = 'localhost' # indirizzo locale
PORT = 0 # prima porta disponibile
BUFF_SIZE = 1024 # max data ricevuti

# creazione della socket 
# socket.socket(
# .AF_INET ipv4
# .SOCK_STREAM -> TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding della socket all IP e la Port
s.bind((IP, PORT))

# mi metto in attesa di n connessioni
s.listen(1)

# recupero il valore corrente della porta ([1] perchè è una tupla ip,port)
current_port = s.getsockname()[1]
print(f"server pronto su: {IP} {current_port}")

# uso accept() che blocca il server finchè un client non si connette e
# restituisce una nuova socket per i dati ed un indirizzo (del client)
conn, addr = s.accept()
print(f"connessione ricevuta da {addr}")

# ricevo e decodifico i dati dalla socket ottenuta
data = conn.recv(BUFF_SIZE)
print("dati ricevuti" + data.decode("utf-8"))

# invio la risposta al client
to_client = "messaggio ricevuto dal server in maniera corretta"
conn.send(to_client.encode("utf-8"))

# chiudo la connessione
conn.close()
s.close()