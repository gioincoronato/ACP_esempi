import threading
from time import sleep
import random

posti_disp = threading.Semaphore(2)
# semaforo con counter inizializzato a 2

def accesso(id_utente):
    print(f"utente {id_utente} provo l'accesso al server ")

    with posti_disp: # utilizzo with per accesso e rilascio automatico
        # operazioni:
        print(f"utente {id_utente} accesso eseguito ")
        print("svolgo operazioni... ")
        sleep(3)
        print(f"utente {id_utente} terminato ")
        # rilascio automatico con with

if __name__ == "__main__":
    for i in range(5):
        threading.Thread(target = accesso, args = (i,)).start()
        # avvio 5 thread in competizione 