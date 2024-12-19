from aiohttp import web
from functools import reduce

async def handle_umnozak(request):
    data = await request.json()
    data_lista = data.get("lista")
    if not(type(data_lista)==list):
        return web.json_response({"error": "Lista koju ste proslijedili nije ispravna"}, status=400)
    umnozak = reduce(lambda x,y: x*y, data_lista)
    return web.json_response({"Umnozak liste": umnozak})

app = web.Application()

app.router.add_post("/umnozak", handle_umnozak)

if __name__ == "__main__":
    web.run_app(app, host = "localhost", port=8084)

    