from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from aiohttp.web import View

class OrdersView(View):
    async def get(self):
        return web.json_response({"orders": "get"})

    async def post(self):
        return web.json_response({"orders": "post"})
    
    async def put(self):
        return web.json_response({"orders": "put"})

    async def delete(self):
        return web.json_response({"orders": "delete"})
