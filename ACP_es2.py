# Classi


class AutoMobile:

    def __init__(self, marca, modello, km_iniziali = 0):
        var_test = "ciao" #variabile locale del metodo init
        # attributi dell'istanza
        # self serve ad accedere allo stato interno dell'oggetto
        self.marca = marca
        self.modello = modello

        # __ permette di rendere l'attributo privato (anche se non formalmente)
        if km_iniziali > 0:
            self.__Km = km_iniziali
        else:
            self.__Km = 0
            print("valore Km non valido, set to 0 ")    
        self.accesa = False

    def get_km(self):
        # getter per la lettura dei km
        return self.__Km

    def set_km(self, valore):
        # setter per il parametro km
        if self.get_km() < valore:
            self.__Km = valore
        else:
            print("impossibile scalare il tachimetro ")


    # overide print
    def __str__(self):
        stato = "accesa" if self.accesa else "spenta"
        return f"Auto :{self.marca} {self.modello} | KM {self.__Km} | stato: {stato}"  

    # overide sum
    def __add__(self, km_car2):
        return self.__Km + km_car2  

    def accendi(self):
        self.accesa = True
        print(f"la {self.modello} è accesa")
         
    def viaggia(self, km_percorsi):
        if self.accesa:
            self.__Km += km_percorsi
            print(f"La {self.modello} ha percorso {km_percorsi} KM ")
            print(f"Il tachimetro segna un totale di {self.get_km()} KM ")
        else:
            print(f"La {self.modello} è spenta. ")
            print(f"Il tachimetro segna un totale di {self.get_km()} KM ")


class Camion(AutoMobile):
    def __init__(self, marca, modello, carico_max, km_iniziali,):
        super().__init__(marca, modello, km_iniziali)
        # super() permette di utilizzare i metodi della classe padre
        self.carico_max = carico_max
        self.carico_attuale = 0

    def carica(self, peso):
        print(f"tentativo carico di {peso} kg ")
        if peso > 0:
            if self.carico_attuale + peso <= self.carico_max:
                self.carico_attuale += peso
                print(f"caricati {peso} kg, carico attuale {self.carico_attuale} kg ")
            else:
                print(f"raggiunto limite carico ({self.carico_max}), impossibile caricare")
        else:
            print("nessun carico disponibile")
    def __str__(self):
        info_base = super().__str__()
        return f"{info_base} | carico : {self.carico_attuale}/ {self.carico_max}"             
        


if __name__ == "__main__":
    marca = input("inserisci marca dell'auto: ")
    modello = input("inserisci il modello dell'auto: ")
    km  = int(input("inserisci quanti km ha la tua macchina: "))
    # importante fare cast ad int per i numeri per evitare problemi

    marca2 = input("inserisci marca dell'auto: ")
    modello2 = input("inserisci il modello dell'auto: ")
    km2  = int(input("inserisci quanti km ha la tua macchina: "))
    c1 = AutoMobile(marca, modello, km)
    c2 = AutoMobile(marca2, modello2, km2)
    print(c1)
    print(c2)
    c1.accendi()
    c1.viaggia(30)
    c2.viaggia(20)
    print(f"la somma dei km delle tue auto è {c1 + c2.get_km()}")

    marca3 = input("inserisci marca camion ")
    modello3 = input("inserisci il modello del camion ")
    km_3 = int(input("inserisci i km del camion "))
    carico = int(input("inserisci il carico max del camion: "))
    c3 = Camion(marca3, modello3, carico, km_3)
    print(c3)
    c3.carica(345)
    c3.carica(543)


