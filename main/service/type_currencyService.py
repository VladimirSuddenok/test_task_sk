from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from main.util import Util
from main.dao.type_currency import Type_currencyDAO, Type_currency
from typing import List

import psycopg2
import psycopg2.extras

class Type_currencyService(Util, Type_currencyDAO):
    '''Service class for DAO Type_currencyDAO'''
    
    def __init__(self) -> None:
        super().__init__()
        self._connection = self.get_connection()

    def add(self, type_currency: Type_currency) -> bool:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''INSERT INTO type_currency (name) VALUES ('{name}');'''

        sql = sql.format(name = type_currency.name)
                         
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

    def get_all(self) -> List[Type_currency]:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)
        sql = '''SELECT id, name FROM type_currency;'''
                
        try:
            cursor.execute(sql)
            type_currency_list = list()
            for row in cursor:
                type_currency = Type_currency()

                type_currency.id = row['id']
                type_currency.name = row['name']
            
                type_currency_list.append(type_currency)
            return type_currency_list

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def get_by_id(self, id: int) -> Type_currency:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)
        sql = '''SELECT id, name FROM type_currency 
                 WHERE id = '{id}' '''

        sql = sql.format(id = id)
                
        try:
            cursor.execute(sql)
            row = cursor.fetchone()
            type_currency = Type_currency()

            type_currency.id = row['id']
            type_currency.name = row['name']

            return type_currency

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()
    
    def update(self, type_currency: Type_currency) -> Type_currency:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''UPDATE type_currency
                 SET name = '{name}' WHERE id = '{id}';'''

        sql = sql.format(id = type_currency.id,
                         name = type_currency.name)
        try:
            cursor.execute(sql)
            self._connection.commit()
            return type_currency

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def remove(self, type_currency: Type_currency):
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''DELETE FROM type_currency WHERE id = '{id}';'''

        sql = sql.format(id = type_currency.id)
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