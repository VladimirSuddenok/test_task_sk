from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

import psycopg2
from main.config import Config 

class Util:
    '''Data base connection class'''
    def __init__(self):
        #get application configuration
        config = Config()

        self._host = config.get("data_base_settings", "host")
        self._database = config.get("data_base_settings", "database")
        self._user = config.get("data_base_settings", "user")
        self._password = config.get("data_base_settings", "password")

    def get_connection(self):
        try:
            connection = psycopg2.connect(host = self._host,
                                          database =  self._database, 
                                          user =  self._user, 
                                          password =  self._password)

            return connection

        except psycopg2.DatabaseError as ex:
            raise psycopg2.DatabaseError(ex)

def db_request(commit, sql):
    '''Test procedure'''
    connection = Util().get_connection()
    cursor = connection.cursor(
             cursor_factory = psycopg2.extras.DictCursor)
 
    cursor.execute(sql)
    data = None

    try:
        data = cursor.fetchall()
    except :
        pass

    cursor.close()

    if commit:
        connection.commit()
    connection.close()
    return data