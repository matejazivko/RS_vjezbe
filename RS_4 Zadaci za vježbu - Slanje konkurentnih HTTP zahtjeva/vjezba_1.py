import aiohttp
import asyncio
import time

async def fetch_users(session):
    print ("Šaljem zahtjev...")
    response = await session.get("https://jsonplaceholder.typicode.com/users")
    users_dict = await response.json()
    return users_dict

async def main():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        lista = [fetch_users(session) for _ in range (5)]
        rezultati = await asyncio.gather(*lista)
        users = rezultati [0]
        ime_korisnika = [user["name"] for user in users]
        email_korisnika = [user["email"] for user in users]
        username_korisnika = [user["username"] for user in users]
        end_time = time.time()
        print (f"Imena korisnika: {ime_korisnika}")
        print (f"Email korisnika: {email_korisnika}")
        print (f"Username korisnika: {username_korisnika}")
        print(f"Vrijeme izvođenja: {end_time - start_time:.2f}sec")
    
asyncio.run(main())