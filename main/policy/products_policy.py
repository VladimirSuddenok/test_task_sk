from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from concurrent.futures import ThreadPoolExecutor
from main.service.productService import ProductService, Product
from main.service.priceService import PriceService, Price
from main.service.type_currencyService import Type_currencyService, Type_currency

from typing import Dict, Tuple, List
import asyncio

class ProductsPolicy:
    KEYS_PRODUCT = ('name', 'descriptions', 'left_in_stock')
    KEYS_CURRECNTY = ('name',)
    KEYS_PRICE = ('amount',)#('product_id', 'amount', 'type_currency_id')

    async def get_products(self):
        loop = asyncio.get_event_loop()

        raw_product = None
        with ThreadPoolExecutor(max_workers = 10) as pool:
            raw_product = await loop.run_in_executor(
                pool, ProductService().get_all)

        raw_price = None
        with ThreadPoolExecutor(max_workers = 10) as pool:
            raw_price = await loop.run_in_executor(
                pool, PriceService().get_all)

        raw_type_currency = None
        with ThreadPoolExecutor(max_workers = 10) as pool:
            raw_type_currency = await loop.run_in_executor(
                pool, Type_currencyService().get_all)

        to_wrap_data = await self.to_wrap_product_price_currency(
                    products = raw_product, prices = raw_price,
                    type_currencys = raw_type_currency)
        
        return {'result': to_wrap_data, 'message': 'done'}
        
    async def to_wrap_product_price_currency(self, products: List[Product],
                                           prices: List[Price],
                                           type_currencys: List[Type_currency]):
        products_list = [product.to_dict() for product in products]
        price_list = [price.to_dict() for price in prices]
        type_currency_list = [type_currency.to_dict() for type_currency in type_currencys]
        
        #result = list()
        for product in products_list:
            #all product prices
            product['prices'] = list()
            for price in price_list:
                if price['product_id'] == product['id']:
                    product['prices'].append(price)
            #buffer = [product['prices'].append(price) if price['product_id'] == product['id'] \
            #            for price in price_list]
            
            #currency type and price comparison
            for price in product['prices']:
                for type_currency in type_currency_list:
                    if type_currency['id'] == price['type_currency_id']:
                        price['type_currency'] = type_currency
            #    buffer = [price['type_currency'] = type_currency if type_currency['id'] == price['type_currency_id']
            #        for type_currency in type_currency_list]
        return products_list

    async def create_product(self, product_dict: Dict,
            currency_dict: Dict, price_dict: Dict):
        #проверить поля товара
        if not await self.check_require_data(data = product_dict,
                keys = ProductsPolicy.KEYS_PRODUCT):
            msg = 'next field is requered: '  + \
                  'name, descriptions, left_in_stock'
            return {'result': False, 'message': msg} 
        #ок, вставляю в базу
        product = await self.get_fields_add_product(data = product_dict)

        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor(max_workers = 10) as pool:
            result = await loop.run_in_executor(
                pool, ProductService().add, product)
        
        #возвращаю id товара
        product_id = None
        if not result:
            return {'result':result, 'message': 'error insert product'}
        else:
            with ThreadPoolExecutor(max_workers = 10) as pool:
                result = await loop.run_in_executor(
                    pool, ProductService().get_by_name, product.name)
                product_id = result.id

        #проверить поля валюты
        if not await self.check_require_data(data = currency_dict,
                keys = ProductsPolicy.KEYS_CURRECNTY):
            msg = 'next field is requered: name'
            return {'result': False, 'message': msg} 
        
        currency = await self.get_fields_add_currency(data = currency_dict)
        #вставляю в базу
        with ThreadPoolExecutor(max_workers = 10) as pool:
            result = await loop.run_in_executor(
                    pool, Type_currencyService().add, currency)

        #возвращаю id валюты
        type_currency_id = None
        with ThreadPoolExecutor(max_workers = 10) as pool:
            result = await loop.run_in_executor(
                    pool, Type_currencyService().get_all)
            type_currency_id = result[-1].id
        
        #проверить поля цены
        if not await self.check_require_data(data = price_dict,
                keys = ProductsPolicy.KEYS_PRICE):
            msg = 'next field is requered: '  + \
                  'product_id, amount, type_currency_id'
            return {'result': False, 'message': msg}

        #вставить в базу используя товар id и валюта id
        price = await self.get_fields_add_price(
                data = price_dict, product_id = product_id,
                type_currency_id = type_currency_id)

        with ThreadPoolExecutor(max_workers = 10) as pool:
            result = await loop.run_in_executor(
                    pool, PriceService().add, price)
            return {'result': result, 'message': 'done'}
        

    async def get_fields_add_price(self, data: Dict, 
                product_id: str, type_currency_id: str):
        price = Price()
        price.amount = data['amount']
        price.product_id = product_id
        price.type_currency_id = type_currency_id
        return price

    async def get_fields_add_currency(self, data: Dict):
        type_currency = Type_currency()
        type_currency.name = data['name']
        return type_currency

    async def get_fields_add_product(self, data: Dict):
        product = Product()
        product.name = data['name']
        product.descriptions = data['descriptions']
        product.left_in_stock = data['left_in_stock']

        return product

    async def get_fields_update_delete_product(self, data: Dict):
        product = Product()
        product.id = data['id']
        product.name = data['name']
        product.descriptions = data['descriptions']
        product.left_in_stock = data['left_in_stock']

        return product

    async def check_require_data(self, data: Dict, keys: Tuple):
        for field in keys:
            if data[field] is not None:
                continue
            else:
                break
        else:
            return True

        return False

    async def update_product(self, data: Dict):
        if not await self.check_require_data(data = data,
                keys = list(ProductsPolicy.KEYS_PRODUCT) + ['id']):
            msg = 'next field is requered: '  + \
                  'id, name, descriptions, left_in_stock'
            return {'result': False, 'message': msg}

        product = await self.get_fields_update_delete_product(data = data)
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor(max_workers = 10) as pool:
            result = await loop.run_in_executor(
                    pool, ProductService().update, product)
            return {'result': result.to_dict(), 'message': 'done'}

    async def delete_product(self, data: Dict):
        if not await self.check_require_data(data = data,
                keys = list(ProductsPolicy.KEYS_PRODUCT) + ['id']):
            msg = 'next field is requered: '  + \
                  'id, name, descriptions, left_in_stock'
            return {'result': False, 'message': msg}

        product = await self.get_fields_update_delete_product(data = data)
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor(max_workers = 10) as pool:
            result = await loop.run_in_executor(
                    pool, ProductService().remove, product)
            return {'result': result, 'message': 'done'}
        
        
