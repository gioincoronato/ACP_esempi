import threading
from time import sleep

# definisco la routine che il thread eseuirà
def compito_lento(nome_task, durata):
    print(f"Thread {nome_task} inzio esecuzione... ")
    sleep(durata)
    print(f"Thread {nome_task} finito esecuzione in {durata} secondi. ")

if __name__ == "__main__":
    # creazione del thread
    # passaggio routine e arogomenti
    mythread = threading.Thread(target = compito_lento, args = ("Thread 1", 5))   
    mythread.start()

    print("il thread sta eseguendo, il programma continua.. ")

    # join per raccogliere l'esecuzione del thread
    mythread.join()
    print("il thread ha finito la sua esecuzione. ")