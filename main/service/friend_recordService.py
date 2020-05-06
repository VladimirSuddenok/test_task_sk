from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from main.util import Util
from main.dao.friend_recordDAO import Friend_recordDAO, Friend_record
from typing import List

import psycopg2
import psycopg2.extras

class Friend_recordService(Util, Friend_recordDAO):
    '''Service class for DAO Friend_recordDAO'''
    
    def __init__(self) -> None:
        super().__init__()
        self._connection = self.get_connection()

    def add(self, friend_record: Friend_record) -> bool:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''INSERT INTO friend_record(
                 user_id, friend_id) VALUES ('{user_id}', '{friend_id}');'''

        sql = sql.format(user_id = friend_record.user_id,
                         friend_id = friend_record.friend_id)
                         
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

    def get_all(self) -> List[Friend_record]:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)
        sql = '''SELECT id, user_id, friend_id
                 FROM friend_record;'''
                
        try:
            cursor.execute(sql)
            friend_record_list = list()
            for row in cursor:
                friend_record = Friend_record()

                friend_record.id = row['id']
                friend_record.user_id = row['user_id']
                friend_record.friend_id = row['friend_id']
            
                friend_record_list.append(friend_record)
            return friend_record_list

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def get_by_user_friend_id(self, user_id: str, 
                              friend_id: str) -> Friend_record:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)
        sql = '''SELECT id, user_id, friend_id
                 FROM friend_record 
                 WHERE user_id = '{user_id}' and friend_id = '{friend_id}';'''

        sql = sql.format(user_id = user_id, friend_id = friend_id)
                
        try:
            cursor.execute(sql)
            row = cursor.fetchone()
            friend_record = Friend_record()

            friend_record.id = row['id']
            friend_record.user_id = row['user_id']
            friend_record.friend_id = row['friend_id']

            return friend_record

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    #def get_by_friend_id(self, friend_id: str) -> List[Friend_record]:
    #    pass

    #def update(self, friend_record: Friend_record) -> Friend_record:
    #    pass

    def remove(self, friend_record: Friend_record):
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)
        sql = '''DELETE FROM friend_record WHERE id = '{id}';'''

        sql = sql.format(id = friend_record.id)
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