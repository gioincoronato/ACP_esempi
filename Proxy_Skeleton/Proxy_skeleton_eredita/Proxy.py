# il proxy deve implementare la stessa interfaccia dello skeleton (server)
# se il server ha un metodo request(data) anche il proxy dovrà averlo
# nel server request fa il vero lavoro mentre nel proxy
# 1- apre una socket verso il server
# 2- impacchetta l'argomento data
# 3- spedisce tutto sulla rete
# 4- aspetta la risposta
# 5- restuisce il risultato al client come se fosse un operazione normale

import socket
from abc import ABC, abstractmethod

# interfaccia identica a quella dello skeleton
class subject(ABC):
    @abstractmethod
    def request(self, data):
        pass

# definiamo ora il proxy vero e proprio
class Proxy(subject):
    def __init__ (self, host, port):
        self.host = host
        self.port = port

    # implementazione del metodo dell'interfaccia
    def request(self, data):
        # socket utilizzata per le operazioni a basso livello
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        
        # connessione al server Skeleton
        s.connect((self.host, self.port)) 

        # invio dei dati
        s.send(data.encode("utf-8"))

        # riceve la risposta
        risp = s.recv(1024).decode("utf-8")

        # chiusura connessione
        s.close()

        return risp # ritorna al client il risultato ottenuto


# main del client che userà proxy-skeleton
if __name__ == "__main__":

    # creazione del proxy e passaggio dei parametri
    oggetto_remoto = Proxy('localhost', 12345) 

    # chiamata di servizio della funzione request
    stringa = "messaggio del client verso il proxy-scheleton " 
    risposta = oggetto_remoto.request(stringa)

    print(f"sono il client, risultato: {risposta}")
