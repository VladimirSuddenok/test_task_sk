from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from main.util import Util
from main.dao.p_userDAO import P_userDAO, P_user
from typing import List

import psycopg2
import psycopg2.extras

class P_userService(Util, P_userDAO):
    '''Service class for DAO P_userDAO'''
    
    def __init__(self) -> None:
        super().__init__()
        self._connection = self.get_connection()

    def add(self, user: P_user) -> bool:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''INSERT INTO p_user(
                    firstname, surname, middlename, sex, age)
                    VALUES ('{firstname}', '{surname}', 
                            '{middlename}', '{sex}', {age})'''

        sql = sql.format(firstname = user.firstname,
                         surname = user.surname,
                         middlename = user.middlename,
                         sex = user.sex, age = user.age)
                         
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

    def get_all(self) -> List[P_user]:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, firstname, surname, middlename, fio, sex, age
                 FROM p_user;'''
                
        try:
            cursor.execute(sql)
            p_user_list = list()
            for row in cursor:
                p_user = P_user()

                p_user.id = row['id']
                p_user.firstname = row['firstname']
                p_user.surname = row['surname']
                p_user.middlename = row['middlename']
                p_user.fio = row['fio']
                p_user.sex = row['sex']
                p_user.age = row['age']
                
                p_user_list.append(p_user)
            return p_user_list

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def get_by_id(self, id: str) -> P_user:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''SELECT id, firstname, surname, middlename, fio, sex, age
                 FROM p_user WHERE id = '{id}';'''

        sql = sql.format(id = id)
                
        try:
            cursor.execute(sql)
            row = cursor.fetchone()
            p_user = P_user()

            p_user.id = row['id']
            p_user.firstname = row['firstname']
            p_user.surname = row['surname']
            p_user.middlename = row['middlename']
            p_user.fio = row['fio']
            p_user.sex = row['sex']
            p_user.age = row['age']
           
            return p_user

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def update(self, user: P_user) -> P_user:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)

        sql = '''UPDATE p_user
                 SET firstname = '{firstname}', 
                 surname = '{surname}', middlename = '{middlename}', 
                 fio = '{fio}', sex = '{sex}', age = '{age}'
                 WHERE id = '{id}';'''

        sql = sql.format(id = user.id,
                         firstname = user.firstname,
                         surname = user.surname,
                         middlename = user.middlename,
                         fio = user.fio,
                         sex = user.sex, age = user.age)
        try:
            cursor.execute(sql)
            self._connection.commit()
            return user

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

        finally:
            cursor.close()
            if self._connection is not None:
                self._connection.close()

    def remove(self, user: P_user) -> bool:
        cursor = self._connection.cursor(
                cursor_factory = psycopg2.extras.DictCursor)
                
        sql = '''DELETE FROM p_user WHERE id = '{id}';'''

        sql = sql.format(id = user.id)
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