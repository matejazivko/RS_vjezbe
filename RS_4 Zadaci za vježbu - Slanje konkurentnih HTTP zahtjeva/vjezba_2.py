import aiohttp
import asyncio

async def get_cat_fact (session):
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json()
    return fact_dict

def filter_cat_facts(rezultat):
    return [fact for fact in rezultat if "cat" in fact["fact"].lower() or "cats" in fact["fact"].lower()]

async def main():
    async with aiohttp.ClientSession() as session:
        task_cat = [get_cat_fact (session) for _ in range (20)]
        rezultat = await asyncio.gather(*task_cat)
        print (rezultat)
        filtered_facts = filter_cat_facts(rezultat)
        print(f"Filtrirane činjenice o mačkama: {filtered_facts}")

asyncio.run(main())