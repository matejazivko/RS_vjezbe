def provjera_lozinke(lozinka):
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova")
    elif not lozinka.isupper() and not lozinka.isdigit():
        print ("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
    elif "password" in lozinka.lower() or "lozinka" in lozinka.lower():
        print ("Lozinka ne smije sadržavati riječi password ili lozinka")
    else:
        print("Lozinka je jaka")
    
lozinka= str(input("Upiši lozinku: "))
print(provjera_lozinke(lozinka))