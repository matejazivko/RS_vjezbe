from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp

proizvodi = [
        {"id": 1, "naziv": "Laptop", "cijena": 5000},
        {"id": 2, "naziv": "Miš", "cijena": 100},
        {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
        {"id": 4, "naziv": "Monitor", "cijena": 1000},
        {"id": 5, "naziv": "Slušalice", "cijena": 50}
    ]
narudzbe = []

async def get_proizvodi(request):
    return web.json_response(proizvodi, status=200)

async def get_proizvodi_id(request):
    proizvod_id = request.match_info.get("id")
    
    for proizvod in proizvodi:
        if proizvod["id"] == int(proizvod_id):
            return web.json_response(proizvod, status=200)
        
    return web.json_response({"error": "Proizvod s traženim ID-em ne postoji"}, status=404)

async def add_narudzbe(request):
    data = await request.json()
    proizvod_id = data.get("proizvod_id")
    kolicina = data.get("kolicina")

    provjera_proizvoda = next ((p for p in proizvodi if p ["id"] == proizvod_id), None)
    if provjera_proizvoda is None:
        return web.json_response({"error": "Proizvod s traženim ID-em ne postoji"}, status=404)
    
    narudzba = {
        "proizvod_id": proizvod_id,
        "kolicina": kolicina,
        "naziv": provjera_proizvoda ["naziv"],
        "cijena": provjera_proizvoda ["cijena"]
    }
    narudzbe.append(narudzba)

    return web.json_response({"narudzbe": narudzbe}, status=201)

app = web.Application()

app.router.add_routes([
    web.get("/proizvodi", get_proizvodi),
    web.get("/proizvodi/{id}", get_proizvodi_id),
    web.post ("/narudzbe", add_narudzbe)
])

async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, port=8081)
    await site.start()

async def main():
    await start_server()
    async with aiohttp.ClientSession() as session:
        rezultat = await session.get("http://localhost:8081/proizvodi")
        print(await rezultat.text())

        rezultat = await session.get("http://localhost:8081/proizvodi/1")
        rezultat1 = await rezultat.text()
        print(rezultat1)

        rezultat = await session.get("http://localhost:8081/proizvodi/88")
        rezultat2 = await rezultat.json()
        print(rezultat2)
    
        narudzba = await session.post("http://localhost:8081/narudzbe", json={"proizvod_id": 1, "kolicina": 2})
        print(await narudzba.json())
        

        narudzba1 = await session.post("http://localhost:8081/narudzbe", json={"proizvod_id": 88, "kolicina": 2})
        print(await narudzba1.json())
      

if __name__ == "__main__":
    asyncio.run(main())