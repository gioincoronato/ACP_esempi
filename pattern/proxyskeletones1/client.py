# invoca il metodo locale (importato dal proxy) ed ottiene il valore di ritorno
from proxy import proxy

if __name__ == "__main__":
    port = 12345
    host = "localhost"
    obj = proxy(port, host)
    res =obj.request(3, 4)
    print(f"result: {res}")
