import aiohttp
import asyncio

async def get_dog_fact(session):
    response = await session.get("https://dogapi.dog/api/v2/facts")
    fact_dict = await response.json()
    return fact_dict

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json()
    return fact_dict

def mix_facts (dog_facts, cat_facts):
    mixed_facts =[]
    for dog_fact, cat_fact in zip(dog_facts, cat_facts):
        if len(dog_fact)>len(cat_fact):
         mixed_facts.append(dog_fact)
    else:
        mixed_facts.append(cat_fact)
    return mixed_facts


async def main():
    async with aiohttp.ClientSession() as session:
        dog_facts_tasks = [get_dog_fact(session) for _ in range (5)]
        cat_facts_tasks = [get_cat_fact(session) for _ in range (5)]
        dog_cat_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)
   
    dog_facts = dog_cat_facts[:5]
    cat_facts = dog_cat_facts[5:]
    mixed_facts = mix_facts(dog_facts, cat_facts)

    print(f"Činjenice o psima: {dog_facts}")
    print (f"Činjenice o mačkama: {cat_facts}")
    print(f"Mixane činjenice o psima i mačkama: {mixed_facts}")


asyncio.run(main())
    
        
