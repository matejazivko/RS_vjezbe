from aiohttp import web
from asyncio import sleep

async def handle_pozdrav2(request):
    await sleep(4)
    return web.json_response({"message": "Pozdrav nakon 4 sekunde."})

app = web.Application()

app.router.add_get("/pozdrav2", handle_pozdrav2)

if __name__ == "__main__":
    web.run_app(app, host = "localhost", port = 8082)