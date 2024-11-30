import asyncio

async def secure_data(rjecnik):
    print ({"prezime": rjecnik ["prezime"], "broj_kartice": "enkriptirano", "cvv": "enkriptirano"})
    await asyncio.sleep(3)
    

lista = [
    {"prezime": "Marić", "broj_kartice": "13445343", "cvv": "123"},
    {"prezime": "Ivić", "broj_kartice": "84374435", "cvv": "456"},
    {"prezime": "Anić", "broj_kartice": "63988356", "cvv": "789"}
]
async def main():
    zadaci = [asyncio.create_task(secure_data(rjecnik)) for rjecnik in lista]
    rezultat = await asyncio.gather(*zadaci)
    print(rezultat)

asyncio.run(main())