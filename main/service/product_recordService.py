from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from main.util import Util
from main.dao.product_recordDAO import Product_recordDAO, Product_record
from typing import List

import psycopg2
import psycopg2.extras

class Product_recordService(Util, Product_recordDAO):
    '''Service class for DAO Product_recordDAO'''
    
    def __init__(self) -> None:
        super().__init__()
        self._connection = self.get_connection()

    def add(self, product_record: Product_record) -> bool:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''INSERT INTO product_record(
                 order_id, product_id)
                 VALUES ('{order_id}', '{product_id}');'''

        sql = sql.format(order_id = product_record.order_id,
                         product_id = product_record.product_id)
                         
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

    def get_all(self) -> List[Product_record]:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, order_id, product_id
                 FROM product_record;'''
                
        try:
            cursor.execute(sql)
            product_record_list = list()
            for row in cursor:
                product_record = Product_record()

                product_record.id = row['id']
                product_record.order_id = row['order_id']
                product_record.product_id = row['product_id']
                
                product_record_list.append(product_record)
            return product_record_list

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def get_by_id(self, id: int) -> Product_record:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, order_id, product_id
                 FROM product_record WHERE id = '{id}';'''

        sql = sql.format(id = id)
                
        try:
            cursor.execute(sql)
            row = cursor.fetchone()
            product_record = Product_record()

            product_record.id = row['id']
            product_record.order_id = row['order_id']
            product_record.product_id = row['product_id']
           
            return product_record

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def get_by_product_id(self, product_id: str) -> List[Product_record]:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, order_id, product_id
                 FROM product_record WHERE product_id = '{product_id}';'''
        
        sql = sql.format(product_id = product_id)

        try:
            cursor.execute(sql)
            product_record_list = list()
            for row in cursor:
                product_record = Product_record()

                product_record.id = row['id']
                product_record.order_id = row['order_id']
                product_record.product_id = row['product_id']
                
                product_record_list.append(product_record)
            return product_record_list

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def get_by_order_id(self, order_id: str) -> List[Product_record]:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, order_id, product_id
                 FROM product_record WHERE order_id = '{order_id}';'''
        
        sql = sql.format(order_id = order_id)

        try:
            cursor.execute(sql)
            product_record_list = list()
            for row in cursor:
                product_record = Product_record()

                product_record.id = row['id']
                product_record.order_id = row['order_id']
                product_record.product_id = row['product_id']
                
                product_record_list.append(product_record)
            return product_record_list

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    #def update(self, product_record: Product_record) -> Product_record:
    #    pass

    def remove(self, product_record: Product_record) -> bool:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)
                
        sql = '''DELETE FROM product_record WHERE id = '{id}';'''

        sql = sql.format(id = product_record.id)
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