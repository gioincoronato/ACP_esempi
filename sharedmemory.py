from multiprocessing import Process, Value, Array

# in generale i processi hanno area di memoria distinte
# per condividere la stessa area di memoria tra più processi
# è necessario usare le classi Value (valore singolo) e array(sequenza di valori dello stesso tipo)

def funzione_figlio(n ,a):
    n.value = 16.96 # modifico il valore del numero condiviso

    for i in range(len(a)):
        a[i] = -a[i] # inverto i segni dell'array condiviso


if __name__ == "__main__":
    # inizializzo con ctype un value e un array che saranno condivisi
    
    num = Value('d', 0.0)
    # 'd' sta per double i  questo caso

    arr = Array('i', range(10))
    # 'i' sta per int
    print("pre modifica: ")
    print(num.value)
    print(arr[:])

    # creo e avvio il processo che modifica le risorse condivise
    p = Process(target = funzione_figlio, args = (num,arr))
    p.start()
    p.join()


    # stampo le risorse condivise
    print("post modifica: ")
    print(num.value)
    print(arr[:])