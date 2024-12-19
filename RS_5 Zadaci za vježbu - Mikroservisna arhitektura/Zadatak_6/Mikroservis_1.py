from aiohttp import web 
from asyncio import sleep

async def handle_pozdrav1(request):
    await sleep(3)
    return web.json_response({"message": "Pozdrav nakon 3 sekunde."})

app = web.Application()
app.router.add_get("/pozdrav1", handle_pozdrav1)

if __name__ == "__main__":
    web.run_app(app, host = "localhost", port=8081)