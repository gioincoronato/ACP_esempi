import socket
from abc import ABC, abstractmethod
import threading

class subject(ABC):
    @abstractmethod
    def request(self, a, b):
        pass

class skeleton(subject):
    def __init__(self, port):
        self.port = port

    def run_skeleton(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.bind(('localhost', self.port))
        s.listen(5) 

        while True:
            s_client, addr = s.accept()
            t = threading.Thread(target = self.thread_fun, args = (s_client,))
            t.start()
            
                
    def thread_fun(self, socket):
        data_string = socket.recv(1024).decode("utf-8")
        valori = data_string.split(",")
        a = int(valori[0])
        b = int(valori[1])
        result = str(self.request(a, b))
        socket.send(result.encode("utf-8"))
        socket.close()
        

class realsubject(skeleton):
    def request(self, a, b):
        return a + b

if __name__ == "__main__":
    obj = realsubject(12345)
    obj.run_skeleton()