from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from main.util import Util
from main.dao.productDAO import ProductDAO, Product
from typing import List

import psycopg2
import psycopg2.extras

class ProductService(Util, ProductDAO):
    '''Service class for DAO ProductDAO'''
    
    def __init__(self) -> None:
        super().__init__()
        self._connection = self.get_connection()

    def add(self, product: Product) -> bool:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''INSERT INTO product(
                 name, descriptions, left_in_stock)
                 VALUES ('{name}', '{descriptions}', '{left_in_stock}');'''

        sql = sql.format(name = product.name,
                         descriptions = product.descriptions,
                         left_in_stock = product.left_in_stock)
                         
        try:
            cursor.execute(sql)
            self._connection.commit()
            return True

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def get_all(self) -> List[Product]:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, name, descriptions, left_in_stock
                 FROM product;'''
                
        try:
            cursor.execute(sql)
            product_list = list()
            for row in cursor:
                product = Product()

                product.id = row['id']
                product.name = row['name']
                product.descriptions = row['descriptions']
                product.left_in_stock = row['left_in_stock']
                
                product_list.append(product)
            return product_list

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def get_by_id(self, id: str) -> Product:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, name, descriptions, left_in_stock
                 FROM product WHERE id = '{id}';'''

        sql = sql.format(id = id)
                
        try:
            cursor.execute(sql)
            row = cursor.fetchone()
            product = Product()

            product.id = row['id']
            product.name = row['name']
            product.descriptions = row['descriptions']
            product.left_in_stock = row['left_in_stock']
           
            return product

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def get_by_name(self, name: str) -> Product:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, name, descriptions, left_in_stock
                 FROM product WHERE name = '{name}';'''

        sql = sql.format(name = name)
                
        try:
            cursor.execute(sql)
            row = cursor.fetchone()
            product = Product()

            product.id = row['id']
            product.name = row['name']
            product.descriptions = row['descriptions']
            product.left_in_stock = row['left_in_stock']
           
            return product

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def update(self, product: Product) -> Product:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''UPDATE product
                 SET name = '{name}', descriptions = '{descriptions}',
                 left_in_stock = '{left_in_stock}'
                 WHERE id = '{id}';'''

        sql = sql.format(id = product.id,
                         name = product.name,
                         descriptions = product.descriptions,
                         left_in_stock = product.left_in_stock)
        try:
            cursor.execute(sql)
            self._connection.commit()
            return product

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def remove(self, product: Product) -> bool:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)
                
        sql = '''DELETE FROM product WHERE id = '{id}';'''

        sql = sql.format(id = product.id)
        try:
            cursor.execute(sql)
            self._connection.commit()
            return True

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()