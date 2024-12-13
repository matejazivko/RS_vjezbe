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
async def get_proizvodi(request):
    return web.json_response(proizvodi, status=200)

async def get_proizvodi_id(request):
    proizvod_id = request.match_info.get("id")
    
    for proizvod in proizvodi:
        if proizvod["id"] == int(proizvod_id):
            return web.json_response(proizvod, status=200)
        
    return web.json_response({"error": "Proizvod s traženim ID-em ne postoji"}, status=404)

app = web.Application()

app.router.add_routes([
    web.get("/proizvodi", get_proizvodi),
    web.get("/proizvodi/{id}", get_proizvodi_id)
])

async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, port=8081)
    await site.start()

async def main():
    await start_server()
    async with aiohttp.ClientSession() as session:
        rezultat = await session.get("http://0.0.0.0:8081/proizvodi")
        print(await rezultat.text())

        rezultat = await session.get("http://0.0.0.0:8081/proizvodi/1")
        rezultat1 = await rezultat.text()
        print(rezultat1)

        rezultat = await session.get("http://0.0.0.0:8081/proizvodi/88")
        rezultat2 = await rezultat.json()
        print(rezultat2)

if __name__ == "__main__":
    asyncio.run(main())