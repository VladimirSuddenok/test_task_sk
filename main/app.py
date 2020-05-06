from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from aiohttp import web
from main.view.view_users import UsersView
from main.view.view_friends import FriendsView
from main.view.view_products import ProductsView

def set_views(app):
    app.router.add_view("/users/", UsersView)#+
    app.router.add_view("/friends/", FriendsView)#+
    app.router.add_view("/products/", ProductsView)#+
    #app.router.add_view("/orders/", OrdersView)

def init_func(argv):
    app = web.Application()
    set_views(app = app)
    return app

if __name__ == "__main__":
    app = init_func(argv = [])
    web.run_app(app)
