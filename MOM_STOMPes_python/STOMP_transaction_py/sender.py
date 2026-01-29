# il sender dovrà inviare 3 messaggi in un unica transazione

from time import sleep
import stomp

if __name__ == "__main__":
    # avvio connessione
    print(" avvio connessione per la transazione ")
    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.connect(wait = True)
    print(" connessione stabilita, pronto per la transazione ")

    # ottengo l'id della transazione
    txid = conn.begin()
    print(f" transazione iniziata con ID: {txid}")

    # invio dei messaggi
    msg1 = " TR1 : test1/3 "
    msg2 = " TR2 : test 2/3 "
    msg3 = " TR3 : test 3/3 "
    
    conn.send(destination='/topic/test', body = msg1, transaction = txid)
    print(" messaggio 1/3 inviato ")

    conn.send(destination='/topic/test', body = msg2, transaction = txid)
    print(" messaggio 2/3 inviato ")

    conn.send(destination='/topic/test', body = msg3, transaction = txid)
    print(" messaggio 3/3 inviato ")

    # simulo tempo di attesa
    print(" in attesa del completamento ... ")
    sleep(5)

    # sblocco della transazione
    conn.commit(txid)
    print(" transazione completata")
    conn.disconnect()
    print(" sender disconnesso")


