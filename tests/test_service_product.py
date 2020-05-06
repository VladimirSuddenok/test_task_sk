from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

import pytest
from project.main.service.productService import ProductService, Product
from tests.property import ProductProperty

product = Product()

def test_add():
    ProductProperty.setter(product)

    productService = ProductService()
    result = productService.add(product)

    assert result

def test_get_all():
    productService = ProductService()
    product_list = productService.get_all()
    
    if len(product_list) >= 1:
        product.id = product_list[-1].id
        product.name = product_list[-1].name
        product.descriptions = product_list[-1].descriptions
        product.left_in_stock = product_list[-1].left_in_stock
        assert True
    else:
        assert False

def test_get_by_id():
    productService = ProductService()
    result = productService.get_by_id(product.id)
    equal = result.equal(product)
    assert equal

def test_get_by_name():
    productService = ProductService()
    result = productService.get_by_name(product.name)
    equal = result.equal(product)
    assert equal

def test_update():
    product.name = 'new_name'
    productService = ProductService()
    result = productService.update(product)

    equal = result.equal(product)
    assert equal

def test_remove():
    productService = ProductService()
    result = productService.remove(product)
    assert result