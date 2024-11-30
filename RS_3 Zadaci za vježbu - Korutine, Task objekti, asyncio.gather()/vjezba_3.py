import asyncio

baza_korisnika = [
        {"korisničko_ime": "mirko123", "email": "mirko123@gmail.com"},
        {"korisničko_ime": "ana_anic", "email": "aanic@gmail.com",},
        {"korisničko_ime": "maja_0x", "email": "majaaaaa@gmail.com"},
        {"korisničko_ime": "zdeslav32", "email": "deso032@gmail.com"}
    ]
baza_lozinka = [
        {"korisničko_ime": "mirko123", "lozinka": "lozinka123"},
        {"korisničko_ime": "ana_anic", "lozinka": "super_teska_lozinka"},
        {"korisničko_ime": "maja_0x", "lozinka": "s324SDFfdsj234"},
        {"korisničko_ime": "zdeslav32", "lozinka": "deso123"}
    ]

async def autentifikacija(korisnik):
    print ("Dohvaćam podatke...")
    await asyncio.sleep(3)

async def autorizacija(korisnik, lozinka):
    print(f"Autorizacija korisnika{korisnik["korisničko_ime"]}")
    await asyncio.sleep(2)
    return (f"Korisnik{korisnik["korisničko_ime"]} autoriziran.")
   
for korisnik in baza_korisnika:
        if korisnik ["korisničko_ime"] == baza_korisnika ["korisničko_ime"] and korisnik ["email"] == baza_korisnika["email"]:
            print(f"Korisnik{korisnik} je pronađen")
        else:
            print(f"Korisnik {korisnik} nije pronađen")

async def main():
        korisnik1 = {"korisničko_ime": "mirko123", "email": "mirko123@gmail.com"}
        rezultat = await autentifikacija(korisnik1)
        print(rezultat)

asyncio.run(main())
        