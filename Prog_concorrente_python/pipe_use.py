import multiprocessing as mp

# le pipe sono dei canali di comunicazione tra processi
# hanno due endpoint e possono essere sia bi che mono direzionali
# con i due endpoint è possibule fare send e recv per scambiarsi oggetti

def invia_messaggio(conn):
    conn.send("messaggio inviato dal processo figlio ")
    conn.close()

if __name__ == "__main__":
    # per crerare la pipe utilizzo il comando Pipe da multiprocessing
    conn_padre, conn_figlio = mp.Pipe()

    # creo ed avvio il processo figlio per l'invio del messaggio
    p = mp.Process(target = invia_messaggio, args = (conn_figlio,))
    p.start()

    # il padre usa la receive per ottenere il messaggio
    print(f"Processo padre ha ricevuto un messaggio: {conn_padre.recv()}")

    #raccolgo l'esecuzione
    p.join()
