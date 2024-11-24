class Narudzba:
    def __init__(self, proizvodi, ukupna_cijena):
        self.proizvodi = proizvodi
        self.ukupna_cijena = ukupna_cijena
    
    def napravi_narudzbu (self, novi_proizvodi):
        ukupna_cijena = sum([proizvod["cijena"] * proizvod["kolicina"]for proizvod in novi_proizvodi])
        return Narudzba(novi_proizvodi, ukupna_cijena)
    
    def ispis_narudzbe (self):
        print("Naručeni proizvodi: ")
        for proizvod in self.proizvodi:
            print (f"Naziv: {proizvod["naziv"]}, Ukupna cijena: {self.ukupna_cijena}")