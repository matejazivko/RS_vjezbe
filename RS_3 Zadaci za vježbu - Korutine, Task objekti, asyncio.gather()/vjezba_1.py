import asyncio

async def fetch_list():
    print ("Dohvaćam podatke...")
    list = [1,2,3,4,5,6,7,8,9,10]
    await asyncio.sleep(3)
    print("Podaci dohvaćeni")
    return list

async def main():
    list = await fetch_list()
    print(f"Podaci: {list}")

asyncio.run(main())