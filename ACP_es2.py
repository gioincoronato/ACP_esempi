# Classi


class AutoMobile:

    def __init__(self, marca, modello, km_iniziali = 0):
        var_test = "ciao" #variabile locale del metodo init
        # attributi dell'istanza
        # self serve ad accedere allo stato interno dell'oggetto
        self.marca = marca
        self.modello = modello
        self.Km = km_iniziali
        self.accesa = False

    # overide print
    def __str__(self):
        stato = "accesa" if self.accesa else "spenta"
        return f"Auto :{self.marca} {self.modello} | KM {self.Km} | stato: {stato}"  

    # overide sum
    def __add__(self, km_car2):
        return self.Km + km_car2  

    def accendi(self):
        self.accesa = True
        print(f"la {self.modello} è accesa")
         
    def viaggia(self, km_percorsi):
        if self.accesa:
            self.Km += km_percorsi
            print(f"La {self.modello} ha percorso {km_percorsi} KM ")
            print(f"Il tachimetro segna un totale di {self.Km} KM ")
        else:
            print(f"La {self.modello} è spenta. ")
            print(f"Il tachimetro segna un totale di {self.Km} KM ")


if __name__ == "__main__":
    marca = input("inserisci marca dell'auto: ")
    modello = input("inserisci il modello dell'auto: ")
    km  = int(input("inserisci quanti km ha la tua macchina: "))
    # importante fare cast ad int per i numeri per evitare problemi
    c1 = AutoMobile(marca, modello, km)
    print(c1)
    c1.accendi()
    c1.viaggia(30)
