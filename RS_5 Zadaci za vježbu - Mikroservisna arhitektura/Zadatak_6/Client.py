import aiohttp 
import asyncio

async def fetch_pozdrav1():
    async with aiohttp.ClientSession() as session:
        response = await session.get("http://localhost:8081/pozdrav1")
        return await response.json()
    
async def fetch_pozdrav2():
    async with aiohttp.ClientSession() as session:
        response = await session.get("http://localhost:8082/pozdrav2")
        return await response.json()
    
#sekvencijalno slanje zahtjeva

async def main():
   print("Pokretanje main korutine")
   pozdrav1_response = await fetch_pozdrav1()
   print (f"Odgovor Mikroservisa_1: {pozdrav1_response}")

   pozdrav2_response = await fetch_pozdrav2()
   print (f"Odgovor Mikroservisa_2: {pozdrav2_response}")

# konkurentno slanje zahtjeva

async def main():
    print ("Pokretanje main korutine")
    rezultat = await asyncio.gather(fetch_pozdrav1(), fetch_pozdrav2())
    print (rezultat)

if __name__ == "__main__":
    asyncio.run(main())