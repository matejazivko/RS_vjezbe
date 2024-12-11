from aiohttp import web

proizvodi = [
    {"naziv":"bilježnica", "cijena": "10", "količina":"4"},
    {"naziv":"olovka", "cijena": "5", "količina":"10"}
]
async def handle_proizvodi(request):
    return web.json_response({"proizvodi": proizvodi})

app = web.Application()
app.router.add_get("/proizvodi", handle_proizvodi)


web.run_app(app, host="localhost", port=8080)