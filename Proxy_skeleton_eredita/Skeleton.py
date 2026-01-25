# implementazione dello schema proxy-scheleton tramite ereditarierà
# qui implementiamo lo skeleton (server)
# si usa un interfaccia astratta che poi verrài implementata dalla classe server_imp

# definizione dell'interfaccia:
from abc import ABC, abstractmethod

class subject(ABC):
    @abstractmethod
    def request(self, data):
        pass

# lo skeleton eredita dall'interfaccia andando ad implemnetare tutta la logica a basso livello
import socket
import threading

class Skeleton(subject):
    def __init__(self, port):
        self.port = port

    def run_skeleton(self):
        # def, bind e listen della socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.bind(('localhost', self.port))  
        s.listen(5)
        print(f"Skeleton in ascolto sulla porta {self.port}") 

        while True:
            c, addr = s.accept()
            # c in questo caso è l'oggetto socket per fare send e rcv
            # questo oggetto verrà consegnato quando il cient tramite proxy prova a connettersi
            # addr come al solito la tupla indirizzo e porta

            # avvio il thread con la routine thd_fun contneuta nella stessa classe (ereditarietà)
            # questo thread "operaio" permette allo skeleton di continuare ad occuparsi di altri client
            # passo l'oggetto socket ricevuto
            t = threading.Thread(target = self.thd_fun, args = (c,))
            t.start() # avvio il thread

    def thd_fun(self, c):
        data = c.recv(1024)

        # eseguo l'upcall invocando il metodo del figlio
        # in pratica lo skeleton chiede a chi lo ha ereditato di elaborare i dati
        result = self.request(data.decode("utf-8"))
        c.send(result.encode("utf-8"))
        c.close()

class real_subject(Skeleton):
    # qui implementiamo la vera logica richiesta dall'interfaccia
    # request nello skeleton fa il vero lavoro
    def request(self, data):
        return data[::-1] # ritorna i dati in ingresso imvertiti

if __name__ == "__main__":
    server = real_subject(12345) # costruizione dell'oggetto fisico
    server.run_skeleton() # invocazione del metodo per la creazione e avvio della socket                       