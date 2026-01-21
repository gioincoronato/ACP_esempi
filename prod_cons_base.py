import threading
from time import sleep

magazzino = [] # risorsa condivisa

condizione = threading.Condition() 
# uso la classe condition per stabilire una condizione di sincornizzazione

def consumatore():
    with condizione: # funzione che acquisisce e rilascia il lock in automatico
        while(len(magazzino) == 0): # verifica condizione sincro
            print("magazzino vuoto impossibile consumare ")
            condizione.wait() # rilascio il lock, aspettando la notify

        prodotto = magazzino.pop()
        print(f"consumazione effettuata: {prodotto}")

def produttore():
    with condizione:
        print("produttore in produzione... ")
        sleep(3)
        magazzino.append("Pacco")
        print(f"produttore ha operato ")
        condizione.notify() # avviso il consumatore

if __name__ == "__main__":
    t1 = threading.Thread(target = consumatore)
    t2 = threading.Thread(target = produttore)

    t1.start()
    t2.start()

    t1.join()
    t2.join()