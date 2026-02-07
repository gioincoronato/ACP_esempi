import socket
from abc import ABC, abstractmethod

class subject(ABC):
    @abstractmethod
    def request(self, a, b):
        pass


class proxy(subject):
    def __init__(self, port, host):
        self.port = port
        self.host = host

    def request(self, a, b):
        payload = f"{a},{b}"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((self.host, self.port)) 
        s.send(payload.encode("utf-8"))
        risp = int(s.recv(1024) .decode("utf-8"))        
        s.close()
        return risp 

    
