class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina
    def ispis(self):
        return f"Naziv: {self.naziv}, cijena: {self.cijena}, kolicina: {self.kolicina}"
proizvodi = []

def dodaj_proizvod(naziv, cijena, kolicina):
    dodani_proizvod = Proizvod (naziv, cijena, kolicina)
    proizvodi.append(dodani_proizvod)

