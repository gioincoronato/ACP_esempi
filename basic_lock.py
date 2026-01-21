import threading
from time import sleep

# la variabile lock serve per la protezione di una risorsa condivisa

contatore_globale = 0 #risorsa condivisa
lucchetto = threading.Lock()

def safe_increment(nome_thread):
    global contatore_globale

    print(f"{nome_thread} tentativo di acquisizione... ")

    lucchetto.acquire() # provo ad acquisire la risorsa critica

    # creazione del flusso di controllo sezione critica

    try:
        print(f"{nome_thread} lock acquisito modifico la risorsa condivisa... ")

        contatore_globale = contatore_globale +1
        sleep(3)
       
        print(f"{nome_thread} incemento effettuato, contatore {contatore_globale} ")

    finally:
        print(f"{nome_thread} rilascio il lock... ")
        lucchetto.release()

if __name__ == "__main__":
    t1 = threading.Thread(target = safe_increment, args = ("Thread-1", ))
    t2 = threading.Thread(target = safe_increment, args = ("thread-2", ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"operazioni terminate contatore: {contatore_globale}")       