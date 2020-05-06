from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from main.util import Util
from main.dao.priceDAO import PriceDAO, Price
from typing import List

import psycopg2
import psycopg2.extras

class PriceService(Util, PriceDAO):
    '''Service class for DAO PriceDAO'''
    
    def __init__(self) -> None:
        super().__init__()
        self._connection = self.get_connection()

    def add(self, price: Price) -> bool:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''INSERT INTO price(
                 product_id, amount, type_currency_id)
                 VALUES ('{product_id}', '{amount}', '{type_currency_id}');'''

        sql = sql.format(product_id = price.product_id,
                         amount = price.amount,
                         type_currency_id = price.type_currency_id)
                         
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

    def get_all(self) -> List[Price]:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, product_id, amount, type_currency_id
                 FROM price;'''
                
        try:
            cursor.execute(sql)
            price_list = list()
            for row in cursor:
                price = Price()

                price.id = row['id']
                price.product_id = row['product_id']
                price.amount = row['amount']
                price.type_currency_id = row['type_currency_id']
                
                price_list.append(price)
            return price_list

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def get_by_id(self, id: str) -> Price:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, product_id, amount, type_currency_id
                 FROM price WHERE id = '{id}';'''

        sql = sql.format(id = id)
                
        try:
            cursor.execute(sql)
            row = cursor.fetchone()
            price = Price()

            price.id = row['id']
            price.product_id = row['product_id']
            price.amount = row['amount']
            price.type_currency_id = row['type_currency_id']
           
            return price

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def get_by_product_id(self, product_id: str) -> List[Price]:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, product_id, amount, type_currency_id
                 FROM price WHERE product_id = '{product_id}';'''

        sql = sql.format(product_id = product_id)

        try:
            cursor.execute(sql)
            price_list = list()
            for row in cursor:
                price = Price()

                price.id = row['id']
                price.product_id = row['product_id']
                price.amount = row['amount']
                price.type_currency_id = row['type_currency_id']
                
                price_list.append(price)
            return price_list

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

    def update(self, price: Price) -> Price:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''UPDATE price
                 SET product_id = '{product_id}', 
                 amount = '{amount}', type_currency_id = '{type_currency_id}'
                 WHERE id = {id};'''

        sql = sql.format(id = price.id,
                         product_id = price.product_id,
                         amount = price.amount,
                         type_currency_id = price.type_currency_id)
        try:
            cursor.execute(sql)
            self._connection.commit()
            return price

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def remove(self, price: Price) -> bool:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)
                
        sql = '''DELETE FROM price WHERE id = '{id}';'''

        sql = sql.format(id = price.id)
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