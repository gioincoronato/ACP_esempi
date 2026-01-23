import multiprocessing as mp

# le queue sono uno strumento utile per fare comunicare più di 2 processi
# lo scambio avviene in modo FIFO 

def lavoratore(q):
    q.put([42, "risultato", True])


if __name__ == "__main__":
    
    # creo la coda con il metodo Queue
    coda = mp.Queue()

    # creo e avvio il processo che chiama il metodo che utilizza la coda
    p = mp.Process(target = lavoratore, args = (coda,))
    p.start()

    # prelevo FIFO dalla coda l'elemento immesso
    dato = coda.get()
    print(f"dato prelevato: {dato}")

    # raccolgo l'esecuzione
    p.join()


