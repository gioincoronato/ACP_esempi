# per il sender non cambia nulla

# si occupa di mandare messaggi

# 1 -- SETUP --
# ci connettiamo (esattamente come nel receiver)


# 2 -- INVIO MSG --
# utilizzo metodo send(), il msg sarà gestito da ACtiveMq


# 3 -- CHIUSURA --
# metodo disconnect() per chiudere la connessione

import stomp 

if __name__ == "__main__":
    print("sender attivato, avvio setup.. ")

    #  setup e connessione same as receiver
    conn = stomp.Connection([('127.0.0.1', 61613)])

    conn.connect(wait = True)
    print("sender connesso al broker")

    # invio del messaggio
    msg = "test1 - STOMP  persistent complete "
    # anche qui inviamo al topic e non alla coda
    conn.send(destination= '/topic/test', body = msg)
    print("messaggio inviato al broker ..")

    # disconnessione
    conn.disconnect()
    print("sender disconnesso ")

