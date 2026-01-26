import socket
from abc import ABC, abstractmethod

# interfaccia deve essere identica a quella dello Skeleton
class subject(ABC):
    @abstractmethod
    def request(self, data):
        pass

# definisco il proxy
class proxy(subject):
    def __init__(self, host, port):
        self.port = port
        self.host = host

    def request(self, data):
        # il proxy apre la connession ogni volta che serve senza occupare la risorsa se non necessario
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try: 
            # connessione
            s.connect((self.host, self.port))

            # invio dati
            s.send(data.encode("utf-8"))

            # attendo risposta
            risp = s.recv(1024).decode("utf-8")

            return risp

        finally:
            s.close() # chiusura della socket per liberare risorse  

if __name__ == "__main__":

    # creazione del proxy con le cordinate del server
    proxy = proxy('localhost', 12345)

    messaggio = " messaggio inviato dal client 37"

    print(f"Client incio messaggio allo skeleton ")

    # chiamata della funzione locale
    risposta = proxy.request(messaggio)

    print(f"ottenuta risposta dal server: {risposta}")


