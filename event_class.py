import threading
from time import sleep

colpo_di_pistola = threading.Event()
# uso la classe evento che inizlmente viene settato su OFF

def atleta(nome):
    print(f"Atleta: {nome} pronto a partire")

    colpo_di_pistola.wait()
    # i thread si bloccano qui finchè l'event non è SET
    print(f"Atleta: {nome} partito, in corsa ...")

if __name__ == "__main__":
    for i in range(3):
        threading.Thread(target = atleta, args = (i,)).start()

    
    print("Pistola in carica...")
    sleep(2)
    print("Fuoco! ")
    colpo_di_pistola.set()    