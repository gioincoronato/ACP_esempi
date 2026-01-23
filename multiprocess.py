import multiprocessing as mp
import time

# per i task cpu-bound l'utilizzo dei thread è inefficace a causa del GIL
# in quel caso l'approccio muklti-thread è equivalente a quello sequenziale
# utilizziamo il multiprocess in modo da aggirare il problema

def calcolo_cpu_bound(nome):
    print(f"processo : {nome} pronto ad eseguire il calcolo ")
    # eseguo il calcolo cpu-bound
    risultato = sum(i*i for i in range(10**8))
    print(f"processo {nome} calcolo terminato ")


if __name__ == "__main__":
    #creazione dei processi
    p1 = mp.Process(target = calcolo_cpu_bound, args = ("A",))
    p2 = mp.Process(target = calcolo_cpu_bound, args = ("B",))

    inizio = time.time() # start cronometro
    print("avvio timer ")

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    fine = time.time()

    print(f"operazionicompletate in {fine - inizio} secondi")