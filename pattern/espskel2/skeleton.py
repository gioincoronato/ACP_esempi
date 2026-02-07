from abc import ABC, abstractmethod
import socket
import threading

class subject(ABC):
    @abstractmethod
    def sum_request(self, num1, num2):
        pass

class skeleton(subject):
    def __init__(self, port):
        self.port = port

    def skeleton_conn(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', self.port))
        print(f"skeleton connesso porta: {self.port}")
        return s

    def run_skeleton(self):
        socket = self.skeleton_conn()
        socket.listen(5)
        while True:
            socket_client, addr = socket.accept()
            t = threading.Thread(target = self.thread_fun, args=(socket_client,))
            t.start()
        
    def thread_fun(self, socket):
        data_client_string = socket.recv(1024).decode("utf-8")
        data_client = data_client_string.split(",")
        num1 = int(data_client[0])
        num2 = int(data_client[1])
        result = str(self.sum_request(num1, num2))
        socket.send(result.encode("utf-8"))
        socket.close()
        

class realsubjcet(skeleton):
    def sum_request(self, num1, num2):
        return num1 + num2


if __name__ == "__main__":
    obj = realsubjcet(23456)
    obj.run_skeleton()
    


      