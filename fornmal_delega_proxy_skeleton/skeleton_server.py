# utilizzo della delega, approccio più pulito
# forniamo direttamnte il metodo da usare senza ereditarietà
# per fornire il metodo utilizziamo nel costruottore self.delegate = obj
# per chiamare il metodo che ci interessa facciamo self.delegate.Metodo
# il metodo deve essere definito nella classe dell'oggetto che passiamo
# ovvero creiamo l'oggetto proxy passando questo oggetto specifico


import socket
import threading
from abc import ABC, abstractmethod

# 1: creazione dell'interfaccia
class subject(ABC):
    @abstractmethod
    def request(self, data):
        pass

# 2: definiamo lo skeleton
class Skeleton(subject):
    def __init__(self, port, delegate):
        self.port = port
        self.delegate = delegate

    def request(self, data):
        return self.delegate.request(data)   

    def run_skeleton(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.bind(('localhost', self.port)) 
        s.listen(5)
        print(f"SKELETON in ascolto su {self.port}, modalità delega ") 

        while True:
            # creiamo il thread operaio e gli passiamo la socket ricevuta
            c, addr = s.accept()
            t = threading.Thread(target = self.thd_fun, args =(c,))
            t.start()

    def thd_fun(self, c):
        try: # usiamo il try per assicurarci che anche in caso di errore la connessione è chiusa
            # ricezione dei byte
            data = c.recv(1024).decode("utf-8")
            if data:
                print(f"skeleton, ricevuto {data}, delego operazione ")

                # azione di delega, metodo request sul'oggetto passato
                # siccome abbiamo definito request nella classe come delegate
                # ovvero nella classe request chiama il metodo sull oggetto
                result = self.request(data)
                
                #  invio del risultato
                c.send(result.encode("utf-8"))

        finally:
            c.close()   

# implementazione della logica reale
class real_subject(subject):
    # in questo approccio real subject non è figlia di skeleton
    # ma implementa tramite delegate il metodo request
    def request(self, data):
        return data[::-1]                     

if __name__ == "__main__":
    # costruisco l'oggetto reale
    cervello = real_subject()

    # uso l'oggetto reale nello skeleton
    server_skeleton = Skeleton(12345, cervello)
    # in questo caso l'oggetto cervello sarà salvato su self.delegate
    # nella funzione run_skeleton viene chiamata request dall'oggetto cervello 
    server_skeleton.run_skeleton()