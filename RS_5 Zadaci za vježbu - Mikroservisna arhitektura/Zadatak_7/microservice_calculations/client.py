import aiohttp
import asyncio

async def fetch_mikroservis():
    async with aiohttp.ClientSession() as session:
        data= {"lista": [1,2,3,4]}

        mikroservis_1 = session.post("http://localhost:8083/zbroj", json=data)
        mikroservis_2 = session.post("http://localhost:8084/umnozak", json=data)
        
        zbroj, umnozak = await asyncio.gather(mikroservis_1, mikroservis_2)

        zbroj = await zbroj.json()
        umnozak = await umnozak.json()

        kolicnik_data = {
            "lista": data["lista"],
            "zbroj": zbroj ["zbroj brojeva iz liste"],
            "umnozak": umnozak ["Umnozak liste"] 
        }
        mikroservis_3 = await session.post("http://localhost:8086/kolicnik", json=kolicnik_data)
        kolicnik = await mikroservis_3.json()

        return {"zbroj": zbroj, "umnozak": umnozak, "kolicnik": kolicnik}

async def main():
    print ("Pokretanje korutine")
    rezultat = await fetch_mikroservis()
    print(rezultat)

if __name__ == "__main__":
    asyncio.run(main())


