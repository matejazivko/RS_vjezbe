import datetime
class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self. kilometraza = kilometraza
    def starost(self):
        trenutna_godina = datetime.datetime.now().year
        return trenutna_godina - self.godina_proizvodnje
automobil = Automobil("Audi", "A4", 2010, 180000)
print (automobil.kilometraza)
print (f"Starost automobila je: {automobil.starost()} godina.")

  