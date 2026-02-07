from proxy import proxy

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 23456
    obj = proxy(HOST, PORT)
    num1 = input("inserisci il primo numero: ")
    num2 = input("inserisci il secondo numero: ")

    result = obj.sum_request(num1, num2)
    print(f"client ottiene somma: {result}")