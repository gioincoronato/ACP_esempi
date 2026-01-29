# gestore dei messaggi
# listener che si mette in ascolto per la ricezione dei messaggi
# definisce come reagire quando arriva un messaggio

# 1 -- DEF CLASSE --
# definire la classe mylistener (eredita da stomp.connectionlistener)
# overide metodo on_message(), si avvia auto ogni volta che activemq pusha un msg



# 2 -- SETUP --
# istanziare oggetto connection e collegarlo al listener
# usare il metodo connect() e subscribe() per selezionare la coda 




# 3 -- LOOP --
# abilitare la ricezione ascinrona non facendo terminare il programma

from time import sleep
import stomp

class mylistener(stomp.ConnectionListener):
    # cotruttore + overiride metodo on_message()
    def __init__(self, conn):
        self.conn = conn

    
    def on_message(self, frame):
        print("-----------------------------------------------------")
        print(f"msg ricevuto: {frame.body}")
        print("-----------------------------------------------------")

if __name__ == "__main__":
    print("listener attivato, avvio setup.. ")
    # istanziare oggetto connection sulla porta std
    conn = stomp.Connection([('127.0.0.1', 61613)])

    # collego il listener alla connessione
    # chiamo la classe mylistener passando la connessione creata
    conn.set_listener('', mylistener(conn))

    # avvio della connessione
    print("in attesa di connessione.. ")
    # wait = True per sicurezza
    # MODIFICA -> setto l'header con l'ID univoco del client
    conn.connect(wait = True, headers={'client-id': 'MyClientID1'})
    print("connessione stabilita con id MyClientID1 ")

    # sub alla coda di interesse
    # nome e id della dest -> [in questo caso un topic]
    # ack = auto -> autoeliminazione del msg post consumo
    # MODIFICA aggiungo l'header activemq.subscriptionName con ID univoco
    #          persistent = TRUE
    conn.subscribe( 
        destination='/topic/test', 
        id = 1, 
        ack = 'auto',
        persistent = True,
        headers={'activemq.subscriptionName': 'MydurableSUB'})
    
    print("in ascolto su /topic/test (Durable)")

    # loop per non fare morire il listener
    try:
        while True:
            sleep(2)
    except KeyboardInterrupt:
        print(" receiver disconnesso ")
        conn.disconnect()


