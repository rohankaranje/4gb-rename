# route.py
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("PyʀᴏBᴏᴛᴢ")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    runner = web.AppRunner(web_app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)  # Listen on all interfaces
    await site.start()
    print("======= Serving on http://0.0.0.0:8080/ =======")
