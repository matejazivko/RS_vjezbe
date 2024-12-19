from aiohttp import web

async def handle_zbroj(request):
    data = await request.json()
    data_lista = data.get("lista")
    if not (type(data_lista)==list):
        return web.json_response({"error": "Lista koju ste proslijedili nije ispravna"}, status=400)
    zbroj = sum(data_lista)
    return web.json_response({"zbroj brojeva iz liste": zbroj})

app = web.Application()
app.router.add_post("/zbroj", handle_zbroj)
if __name__ == "__main__":
    web.run_app(app, host = "localhost", port=8083)