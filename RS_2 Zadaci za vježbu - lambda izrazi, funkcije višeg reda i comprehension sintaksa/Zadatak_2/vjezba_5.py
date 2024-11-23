rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]
min_duljina = int(input("Unesite minimalnu duljinu riječi: "))
duge_rijeci = list(filter(lambda rijeci: len(rijeci) > min_duljina, rijeci))
print(duge_rijeci)