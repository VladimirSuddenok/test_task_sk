from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

import pytest
from project.main.service.product_recordService import Product_recordService, Product_record
from tests.property import ProductRecordProperty

from main.util import db_request

#create test data
#product
sql_insert_product = '''INSERT INTO product (name, descriptions, left_in_stock)
                        VALUES ('name_test1', 'descriptions_test1', 3);'''

sql_select_product = '''SELECT id FROM product 
                         WHERE (name = 'name_test1' AND 
                         descriptions = 'descriptions_test1') ;'''

sql_delete_product = '''DELETE FROM product WHERE id = '{product_id}';'''

db_request(commit = True, sql = sql_insert_product)
result = db_request(commit = True, sql = sql_select_product)
product_id = result[0][0]

sql_delete_product = sql_delete_product.format(product_id = product_id)
#user
sql_insert_user = '''INSERT INTO p_user (firstname, surname, sex, age)
                        VALUES ('firstname_test1', 'surname_test1', 'sex', '50');'''

sql_select_user = '''SELECT id FROM p_user 
                     WHERE firstname = 'firstname_test1' AND 
                           surname = 'surname_test1';'''

sql_delete_user = '''DELETE FROM p_user WHERE id = '{user_id}';'''

db_request(commit = True, sql = sql_insert_user)
result = db_request(commit = True, sql = sql_select_user)
user_id = result[0][0]

sql_delete_user = sql_delete_user.format(user_id = user_id)

#order
sql_insert_order = '''INSERT INTO p_order ("number", user_id)
                     VALUES ('123456789', '{user_id}');'''

sql_insert_order = sql_insert_order.format(user_id = user_id)

sql_select_order = '''SELECT id FROM p_order 
                      WHERE "number" = '123456789' AND 
                             user_id = '{user_id}';'''

sql_select_order = sql_select_order.format(user_id = user_id)

sql_delete_order = '''DELETE FROM p_order WHERE id = '{order_id}';'''

db_request(commit = True, sql = sql_insert_order)
result = db_request(commit = True, sql = sql_select_order)
order_id = result[0][0]

sql_delete_order = sql_delete_order.format(order_id = order_id)

#base data
product_record = Product_record()

def test_add():
    ProductRecordProperty.setter(product_record, product_id, order_id)

    product_recordService = Product_recordService()
    result = product_recordService.add(product_record)

    assert result

def test_get_all():
    product_recordService = Product_recordService()
    product_record_list = product_recordService.get_all()
    
    if len(product_record_list) >= 1:
        product_record.id = product_record_list[-1].id
        product_record.product_id = product_record_list[-1].product_id
        product_record.order_id = product_record_list[-1].order_id
        assert True
    else:
        assert False

def test_get_by_id():
    product_recordService = Product_recordService()
    result = product_recordService.get_by_id(product_record.id)
    equal = result.equal(product_record)
    assert equal

def test_get_by_product_id():
    product_recordService = Product_recordService()
    product_record_list = product_recordService.get_by_product_id(product_record.product_id)
    if len(product_record_list) >= 1:
        assert True
    else:
        assert False

def test_get_by_order_id():
    product_recordService = Product_recordService()
    product_record_list = product_recordService.get_by_order_id(product_record.order_id)
    if len(product_record_list) >= 1:
        assert True
    else:
        assert False

#def test_update():
#    pass

def test_remove():
    global sql_delete_order, sql_delete_product, sql_delete_user
    product_recordService = Product_recordService()
    result = product_recordService.remove(product_record)
    assert result

    result = db_request(commit = True, sql = sql_delete_product)
    result = db_request(commit = True, sql = sql_delete_order)
    result = db_request(commit = True, sql = sql_delete_user)