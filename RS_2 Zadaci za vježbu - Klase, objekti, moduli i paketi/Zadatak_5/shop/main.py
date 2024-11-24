from proizvod import dodaj_proizvod, proizvodi
from narudzbe import Narudzba

novi_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

narudzbe = []
for proizvod in novi_proizvodi:
    dodaj_proizvod (proizvod["naziv"], proizvod["cijena"], proizvod["kolicina"])


print("Novi proizvodi: ")
for proizvod in proizvodi:
    print (proizvod.ispis())

nova_narudzba = Narudzba.napravi_narudzbu(novi_proizvodi)
nova_narudzba.ispis_narudzbe()