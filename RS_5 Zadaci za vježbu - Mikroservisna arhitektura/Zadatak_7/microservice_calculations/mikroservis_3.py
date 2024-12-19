from aiohttp import web
import aiohttp


async def handle_kolicinik(request):
    data = await request.json()
    data_lista = data.get("lista")
    data_zbroj = data.get("zbroj")
    data_umnozak = data.get ("umnozak")
    if data_umnozak == 0:
        return web.json_response({"error": "Umnožak se ne može dijelti s 0."})
    kolicnik = [i / data_zbroj * data_umnozak for i in data_lista]
    return web.json_response({"kolicnik iznosi": kolicnik})

app = web.Application()
app.router.add_post("/kolicnik", handle_kolicinik)
if __name__ == "__main__":
    web.run_app(app, host = "localhost", port = 8086)


    