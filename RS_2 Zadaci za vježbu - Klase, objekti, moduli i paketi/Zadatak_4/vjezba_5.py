class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    def work (self):
        return f"Radim na poziciji {self.pozicija}."
class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
    def work (self):
        return f"Radim na poziciji {self.pozicija} u odjelu {self.department}."
    def give_raise (self, radnik, povecanje):
        radnik.placa += povecanje
        return f"Plaća radnika {radnik.ime} s povećanjem iznosi {radnik.placa}."

radnik = Radnik ("Ivo", "građevinar", 1000)
manager = Manager ("Ivo", "građevinar", 1000, "ured")

print(radnik.work())
print (manager.work())
print (manager.give_raise(radnik, 200))
