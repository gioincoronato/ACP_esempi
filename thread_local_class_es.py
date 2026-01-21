import threading
from time import sleep

# usiamo la classe local per definire un istanza perosnale per ogni thread
# se non lo facessimo siccome queste risorse sono condivise trai thread sarebbero sovrascritte
# in questo modo ogni thread può modificarla a suo piacimento senza interferire con gli altri
sessione_utente = threading.local()

def gestione_utente(nome_utente):
    # salvo nome utente nell'istanza della classe local
    # in questa classe posso definire qualsiasi variabile voglia , in questo caso "user"
    sessione_utente.user = nome_utente

    print(f"{threading.current_thread().name} sto lavoronado per {sessione_utente.user}... ")
    sleep(3)
    print(f"{threading.current_thread().name} lavoro finito ")

if __name__ == "__main__":

    t1 = threading.Thread(target = gestione_utente, args = ("Utente 1",), name = "thread-1")
    t2 = threading.Thread(target = gestione_utente, args = ("Utente 2",), name = "thread-2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Tutti i thread hanno finito. ")