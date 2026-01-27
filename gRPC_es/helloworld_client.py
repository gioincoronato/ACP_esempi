# codice per chiamare la logica
# diviso in 3 parti
# 1- creazione del canale: aprire una connessione verso l'indirizzo del server

# 2- creazione dello stub: otteniamo lo stub(proxy) in modo da chiamare
#                          i metodi remoti come se fossero locali                            

# 3- chiamata rpc: creazione e invio del messaggio di richiesta +
#                  ricezione del messaggio di risposta dal server


import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    # creazione canale e apertura connessione verso indirizzo server
    # usiamo with in modo da gestire in maniera automatica la chiusura del canale
    with grpc.insecure_channel("localhost:50051") as channel:

        # otteniamo lo stub
        # channel è il canale di comunicazione
        # stub è il proxy
        # GreeterStub è la classe creata automaticmante dal file .proto
        stub = helloworld_pb2_grpc.GreeterStub(channel)

        # chiamata rpc
        # helloworld_pb2.HelloRequest(name = "Canonico") -> pacchetto inviato
        # chiamando il metodo  SayHello sullo stub:
        # lo stub ottiene il pacchetto e lo trasforma in binario
        # response sarà un oggetto del tipo HelloReply
        response = stub.SayHello(helloworld_pb2.HelloRequest(name = "Canonico"))

        # stampa del messaggio contenuto nella risposta
        print("risposta ricevuta dal server: " + response.message)

if __name__ == "__main__":
    run()        



