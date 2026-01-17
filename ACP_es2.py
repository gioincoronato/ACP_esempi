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

    pass