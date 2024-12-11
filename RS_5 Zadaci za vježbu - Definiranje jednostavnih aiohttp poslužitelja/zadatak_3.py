from aiohttp import web

korisnici = [
    {"ime": "Ivo", "godine": 25},
    {"ime": "Ana", "godine": 17},
    {"ime": "Marko", "godine": 19},
    {"ime": "Maja", "godine": 16},
    {"ime": "Iva", "godine": 22}
]
async def handler_korisnici(request):
    punoljetni = list(filter(lambda korisnik: korisnik["godine"]>18, korisnici))
    return web.json_response({"punoljetni": punoljetni})

app = web.Application()

app.router.add_get("/stariji_korisnici", handler_korisnici)

web.run_app(app, port=8082)