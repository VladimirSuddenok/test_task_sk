from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

import pytest
from project.main.service.p_orderService import P_orderService, P_order
from tests.property import OrderProperty

from main.util import db_request

sql_insert = '''INSERT INTO p_user (firstname, surname, sex, age)
                      VALUES ('firstname_test1', 'surname_test1', 'sex', '50');'''

sql_select = '''SELECT id FROM p_user 
                WHERE (firstname = 'firstname_test1' AND 
                       surname = 'surname_test1') ;'''

sql_delete = '''DELETE FROM p_user WHERE id = '{id1}';'''

#create test users
db_request(commit = True, sql = sql_insert)
result = db_request(commit = True, sql = sql_select)
id1 = result[0][0]
#base data
p_order1 = P_order()

def test_add():
    OrderProperty.setter(p_order1, id1)

    p_orderService = P_orderService()
    result = p_orderService.add(p_order1)

    assert result

def test_get_all():
    p_orderService = P_orderService()
    p_order_list = p_orderService.get_all()
    
    if len(p_order_list) >= 1:
        p_order1.id = p_order_list[-1].id
        p_order1.number = p_order_list[-1].number
        p_order1.user_id = p_order_list[-1].user_id
        assert True
    else:
        assert False

def test_get_by_id():
    p_orderService = P_orderService()
    result = p_orderService.get_by_id(p_order1.id)
    equal = result.equal(p_order1)
    assert equal

def test_get_by_user_id():
    p_orderService = P_orderService()
    p_order_list = p_orderService.get_by_user_id(id1)
    if len(p_order_list) >= 1:
        assert True
    else:
        assert False

def test_update():
    p_order1.number = 123
    p_orderService = P_orderService()
    result = p_orderService.update(p_order1)

    equal = result.equal(p_order1)
    assert equal

def test_remove():
    global sql_delete
    p_orderService = P_orderService()
    result = p_orderService.remove(p_order1)
    assert result

    sql_delete = sql_delete.format(id1 = id1)
    result = db_request(commit = True, sql = sql_delete)