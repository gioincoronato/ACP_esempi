from abc import ABC, abstractmethod
import socket

class subject(ABC):
    @abstractmethod
    def sum_request(self, num1, num2):
        pass

class proxy(subject):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def proxy_conn(self):
        print("avvio connessione lato proxy ")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        print(f"connessione avviata host: {self.host}, port: {self.port} ")
        return s

    def proxy_disconn(self, socket):
        socket.close()
        print("disconnessione lato proxy effettuata ")
        
    def sum_request(self, num1, num2):
        socket = self.proxy_conn()
        data_string = f"{num1},{num2}"
        print("invio dati al server ")
        socket.send(data_string.encode("utf-8"))
        print("ricezione dati dal server")
        result = (socket.recv(1024).decode("utf-8"))
        self.proxy_disconn(socket)
        return result

