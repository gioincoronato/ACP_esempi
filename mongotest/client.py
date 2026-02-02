from pymongo import MongoClient

def get_db():
    """
    funzione per stabilire la connessione,
    restituisce un riferimento al db
    """

    # localhost:porta
    connection_string = "mongodb://127.0.0.1:27017"

    # creazione del client
    client = MongoClient(connection_string) 
    print("ottenuta connessione con DB " + connection_string)

    # ritorniamo il db denominato test
    # se non esistente verrà creato
    return client['test']


def add_item(collection):
    """
    funzione che prepara gli item e li inserisci nella collection
    """

    # creiamo gli oggetti (possono anche avere campi diversi)
    # mongodb creerà il suo _id specifico

    item1 = {
        "ID" : "1234",
        "PRODOTTO" : "Dentifricio",
        "PREZZO" : "1.99",
        "CATEGORIA" : "Bagno",
        "QUANTITA'" : "21"
    }

    item2 = {
        "ID" : "1235",
        "PRODOTTO" : "uova",
        "PREZZO" : "3.99",
        "SCADENZA" : "21/02/2026",
        "CATEGORIA" : "Cibo",
        "QUANTITA'" : "6 x 6"

    }

    # inseriamo gli oggetti nella collection

    collection.insert_many([item1, item2])
    print("dati inseriti correttamente nel DB")

if __name__ == "__main__":
    
    # otteniamo il riferimento al db
    db_name = get_db()

    # selezioniamo la colection specifica
    collection_name = db_name["prodotti"]

    add_item(collection_name)
