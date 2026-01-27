# generalmente diviso in 2 parti
# 1 - logica del servizio: cosa fa il server
# 2 - infrastruttura di rete: come riceve le chiamate

import helloworld_pb2
import helloworld_pb2_grpc

from concurrent import futures
import grpc

# -\-\-\-\-\-\-\-\- 1 -\-\-\-\-\-\-\-\-\-

# creaimo una classe che eredita dallo skeleton generato automaticamente
class Greeter(helloworld_pb2_grpc.GreeterServicer):
    # qui dobbiamo implmentare i metodi (con lo stesso nome)  def nel .proto
    def SayHello(self, request, context):
        # request contiene dati inviati dal client
        # context contiene metadati come sato ecc

        print(f"Server ricevuta richiesta da {request.name}")

        # dobbiamo ritornare un oggetto del tipo definito nel contratto
        return helloworld_pb2.HelloReply(message = f"ciao {request.name}, dal server ")


# -\-\-\-\-\-\-\-\-\- 2 -\-\-\-\-\-\-\-\-\-

def serve():
    # per poter gestire più chiamate impostiamo il num_max di thread
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # bisogna collegare ora la logica (Greeter) al server grpc creato
    # la funzione usata viene creata in automatico
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    # definiamo ora su quale porta ascoltare
    # 50051 è lo standard
    port = "50051"
    # bind al porto impostato
    # insecure -> comunicazione in chiaro senza permessi
    # "[::]:" + port -> notazione standard ipv6
    server.add_insecure_port("[::]:" + port)

    # avviamo il server
    server.start()
    print("Server avviato al porto: " + port)

    # aspettiamo di ricevere delle chiamate
    server.wait_for_termination()


if __name__ == "__main__":
    serve() # chiamata di avvio del server
