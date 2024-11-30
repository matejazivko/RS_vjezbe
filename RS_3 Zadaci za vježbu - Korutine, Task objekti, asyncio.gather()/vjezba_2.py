import asyncio

async def fetch_rjecnik1():
    print ("Dohvaćam podatke...")
    rjecnik1 = {"ime": "Ivo", "prezime": "Ivić", "dob": 30}
    await asyncio.sleep(3)
    print ("Podaci dohvaćeni")
    return rjecnik1

async def fetch_rjecnik2():
    print ("Dohvaćam podatke drugog rjecnika...")
    rjecnik2 = {"jabuka": 5, "kruška": 3, "banana": 2}
    await asyncio.sleep(5)
    print("Podaci drugog rjecnika dohvaćeni")
    return rjecnik2

async def main():
    rjecnik1, rjecnik2 = await asyncio.gather(fetch_rjecnik1(), fetch_rjecnik2())
    print(f"Podaci iz rjecnika1: {rjecnik1}")
    print(f"Podaci iz rjecnika2: {rjecnik2}")

asyncio.run(main())