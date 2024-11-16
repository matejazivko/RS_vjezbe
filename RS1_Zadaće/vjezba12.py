rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print (rjecnik.keys())
print (rjecnik.values())
def obrni_rjecnik(rjecnik):
    for kljuc, vrijednost in rjecnik.items():
       return vrijednost, kljuc
    print(obrni_rjecnik(rjecnik))

