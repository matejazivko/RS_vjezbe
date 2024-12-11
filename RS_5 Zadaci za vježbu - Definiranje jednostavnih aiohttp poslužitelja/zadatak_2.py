from aiohttp import web

proizvodi = [
    {"naziv":"bilježnica", "cijena": "10", "količina":"4"},
    {"naziv":"olovka", "cijena": "5", "količina":"10"}
]
async def handle_proizvodi(request):
    return web.json_response({"proizvodi": proizvodi})

async def post_handler(request):
    data = await request.json()
    print(data)

    proizvodi.append(data)
    return web.json_response({"proizvodi": proizvodi})

app = web.Application()
app.router.add_get("/proizvodi", handle_proizvodi)
app.router.add_post("/proizvodi", post_handler)


web.run_app(app, host="localhost", port=8080)