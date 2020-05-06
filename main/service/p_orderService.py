from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from main.util import Util
from main.dao.p_orderDAO import P_orderDAO, P_order
from typing import List

import psycopg2
import psycopg2.extras

class P_orderService(Util, P_orderDAO):
    '''Service class for DAO P_orderDAO'''
    
    def __init__(self) -> None:
        super().__init__()
        self._connection = self.get_connection()

    def add(self, order: P_order) -> bool:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''INSERT INTO p_order ("number", user_id)
                 VALUES ('{number}', '{user_id}');'''

        sql = sql.format(number = order.number,
                         user_id = order.user_id)
                         
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

    def get_all(self) -> List[P_order]:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, "number", user_id
                 FROM p_order;'''
                
        try:
            cursor.execute(sql)
            p_order_list = list()
            for row in cursor:
                p_order = P_order()

                p_order.id = row['id']
                p_order.number = row['number']
                p_order.user_id = row['user_id']
                
                p_order_list.append(p_order)

            return p_order_list

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def get_by_id(self, id: str) -> P_order:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, "number", user_id
                 FROM p_order WHERE id = '{id}';'''

        sql = sql.format(id = id)
                
        try:
            cursor.execute(sql)
            row = cursor.fetchone()
            p_order = P_order()

            p_order.id = row['id']
            p_order.number = row['number']
            p_order.user_id = row['user_id']

            return p_order

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def get_by_user_id(self, user_id: str) -> List[P_order]:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, "number", user_id
                 FROM p_order WHERE user_id = '{user_id}';'''
        
        sql = sql.format(user_id = user_id)

        try:
            cursor.execute(sql)
            p_order_list = list()
            for row in cursor:
                p_order = P_order()

                p_order.id = row['id']
                p_order.number = row['number']
                p_order.user_id = row['user_id']
                
                p_order_list.append(p_order)

            return p_order_list

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def update(self, order: P_order) -> P_order:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''UPDATE P_order
                 SET "number" = '{number}', user_id = '{user_id}'
                 WHERE id = '{id}';'''

        sql = sql.format(id = order.id,
                         number = order.number,
                         user_id = order.user_id)
        try:
            cursor.execute(sql)
            self._connection.commit()
            return order

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def remove(self, order: P_order) -> bool:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''DELETE FROM p_order WHERE id = '{id}';'''

        sql = sql.format(id = order.id)

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