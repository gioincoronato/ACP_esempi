import threading
from time import sleep



# in questo caso creo una classe che:
# eredita dalla classe thread e ne chima il costruittore
# esegue le operazioni che voglio facendo l'overiride del metodo run

class calculatorThread(threading.Thread):
    def __init__(self, id_operazione, valore):
        
        super().__init__() # chiamo il costruttore della classe base
        self.id = id_operazione
        self.valore = valore

    # per eseguire le operazioni faccio l'overide del metodo run()
    def run(self):
        print(f"Thread {self.id} avvio calcolo con il valore {self.valore}... ")
        sleep(3)
        risultato = self.valore * self.valore
        print(f"risultato dell'operazione: {risultato}")


if __name__ == "__main__":
   # creo i thread come oggetto della classe
   # avvio i thread con start()
   # raccolgo con join() 
   t1 = calculatorThread(id_operazione=1, valore=10)
   t2 = calculatorThread(id_operazione=2, valore=20)

   t1.start()
   t2.start()

   t1.join()
   t2.join()