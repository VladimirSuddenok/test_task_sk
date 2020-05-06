from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from aiohttp.web import View, json_response
from main.policy.products_policy import ProductsPolicy
from typing import Iterable, Tuple, Dict
import json

class ProductsView(View):

    KEYS_PRODUCT = ('name', 'descriptions', 'left_in_stock')
    KEYS_CURRECNTY = ('name',)
    KEYS_PRICE = ('amount',)

    async def get(self):
        result = await ProductsPolicy().get_products()
        return json_response(result)

    async def post(self):
        data = await self.read_data()
        product_dict = await self.get_dict(data = data,
                object = 'product', keys = ProductsView.KEYS_PRODUCT)
        
        currency_dict = await self.get_dict(data = data,
                object = 'currency', keys = ProductsView.KEYS_CURRECNTY)

        price_dict = await self.get_dict(data = data,
                object = 'price', keys = ProductsView.KEYS_PRICE)

        result = await ProductsPolicy().create_product(
                product_dict = product_dict, 
                currency_dict = currency_dict, price_dict = price_dict)
        return json_response(result)

    async def get_dict(self, data: Dict, object: str, keys: Tuple):
        buffer = data.get(object, {})
        result = dict()
        for key in keys:
            result[key] = buffer.get(key, None)
        
        return result

    async def read_data(self):
        return await self.request.json()
    
    async def get_dict_one(self, data: Dict , keys: Tuple):
        result = dict()
        for key in keys:
            result[key] = data.get(key, None)
        
        return result

    async def put(self):
        input_data = await self.read_data()
        data = await self.get_dict_one(data = input_data, keys = list(ProductsView.KEYS_PRODUCT) + ['id'])
        result = await ProductsPolicy().update_product(data = data)
        return json_response(result)

    async def delete(self):
        input_data = await self.read_data()
        data = await self.get_dict_one(data = input_data, keys = list(ProductsView.KEYS_PRODUCT) + ['id'])
        result = await ProductsPolicy().delete_product(data = data)
        return json_response(result)
