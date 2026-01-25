import socket
import threading

# per fare in modo di gestire più client contemporanemante
# è necessario usare un loop while true

# funzione che gira nel thread
def fun(c):
    data = c.recv(1024) # ricevo dati dal client
    data = data[::-1] # logica di inversione
    c.send(data) # invio dati al client
    c.close() # chiudo la connessione con il client

if __name__ == "__main__":
    # setup connection
    host = 'localhost'
    port = 12345

    # create e bind della socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port)) # bind vuole una tupla
    s.listen(5) # mi metto in ascolto su 5 client
    print(f"creazione e bind con la socket: host:{host}, port:{port} ")

    # creazione del loop per non far morire il server
    while True:
        # accetto la connessione dal server
        # addr[0] ip client
        # addr[1] port client
        c, addr = s.accept()
        # accept() si occupa di creare una socket privata per il client specifico
        print(f"connesso a {addr[0]} : {addr[1]}")

        # creao e avvio il thread per far eseguire la funzione
        t = threading.Thread(target = fun, args =(c,))
        t.start() # avvio il thread, va gestito o terminato manualmente