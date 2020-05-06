from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

import pytest
from project.main.service.priceService import PriceService, Price
from tests.property import PriceProperty

from main.util import db_request

sql_insert_product = '''INSERT INTO product (name, descriptions, left_in_stock)
                         VALUES ('name_test1', 'descriptions_test1', 3);'''

sql_insert_user = '''INSERT INTO type_currency (name)
                         VALUES ('name_test1');'''

sql_select_product = '''SELECT id FROM product 
                         WHERE (name = 'name_test1' AND 
                         descriptions = 'descriptions_test1') ;'''

sql_select_currency = '''SELECT id FROM type_currency 
                         WHERE name = 'name_test1';'''

sql_delete_product = '''DELETE FROM product WHERE id = '{product_id}';'''

sql_delete_currency = '''DELETE FROM type_currency WHERE id = '{type_currency_id}';'''

#create test data
db_request(commit = True, sql = sql_insert_product)
result = db_request(commit = True, sql = sql_select_product)
product_id = result[0][0]

db_request(commit = True, sql = sql_insert_currency)
result = db_request(commit = True, sql = sql_select_currency)
type_currency_id = result[0][0]

#base data
price = Price()

def test_add():
    PriceProperty.setter(price, product_id, type_currency_id)

    priceService = PriceService()
    result = priceService.add(price)

    assert result

def test_get_all():
    priceService = PriceService()
    price_list = priceService.get_all()
    
    if len(price_list) >= 1:
        price.id = price_list[-1].id
        price.product_id = price_list[-1].product_id
        price.amount = price_list[-1].amount
        price.type_currency_id = price_list[-1].type_currency_id
        assert True
    else:
        assert False

def test_get_by_id():
    priceService = PriceService()
    result = priceService.get_by_id(price.id)
    equal = result.equal(price)
    assert equal

def test_get_by_product_id():
    priceService = PriceService()
    price_list = priceService.get_by_product_id(product_id)
    if len(price_list) >= 1:
        assert True
    else:
        assert False

def test_update():
    price.amount = 123
    priceService = PriceService()
    result = priceService.update(price)

    equal = result.equal(price)
    assert equal

def test_remove():
    global sql_delete_currency, sql_delete_product
    priceService = PriceService()
    result = priceService.remove(price)
    assert result

    sql_delete_currency = sql_delete_currency.format(
            type_currency_id = type_currency_id)
    result = db_request(commit = True, sql = sql_delete_currency)

    sql_delete_product = sql_delete_product.format(
            product_id = product_id)
    result = db_request(commit = True, sql = sql_delete_product)