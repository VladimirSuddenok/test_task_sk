from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

import pytest
from project.main.service.type_currencyService import Type_currencyService, Type_currency
from tests.property import TypeCurrencyProperty

type_currency1 = Type_currency()

def test_add():
    TypeCurrencyProperty.setter(type_currency1)

    type_currencyService = Type_currencyService()
    result = type_currencyService.add(type_currency1)

    assert result

def test_get_all():
    type_currencyService = Type_currencyService()
    type_currency_list = type_currencyService.get_all()
    
    if len(type_currency_list) >= 1:
        type_currency1.id = type_currency_list[-1].id
        type_currency1.name = type_currency_list[-1].name
        assert True
    else:
        assert False

def test_get_by_id():
    type_currencyService = Type_currencyService()
    result = type_currencyService.get_by_id(type_currency1.id)
    equal = result.equal(type_currency1)
    assert equal

def test_update():
    type_currency1.name = 'new_name'
    type_currencyService = Type_currencyService()
    result = type_currencyService.update(type_currency1)
    equal = result.equal(type_currency1)
    assert equal

def test_remove():
    type_currencyService = Type_currencyService()
    result = type_currencyService.remove(type_currency1)
    assert result