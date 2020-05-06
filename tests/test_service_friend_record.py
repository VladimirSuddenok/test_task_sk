from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

import pytest
from project.main.service.friend_recordService import Friend_recordService, Friend_record
from tests.property import FriendRecordPropertry

from main.util import db_request

sql_insert = '''INSERT INTO p_user (firstname, surname, sex, age)
                      VALUES ('firstname_test1', 'surname_test1', 'sex', '50'),
                             ('firstname_test2', 'surname_test2', 'sex', '50');'''

sql_select = '''SELECT id FROM p_user 
                WHERE (firstname = 'firstname_test1' AND 
                       surname = 'surname_test1') 
                       OR (firstname = 'firstname_test2' AND 
                       surname = 'surname_test2') ;'''

sql_delete = '''DELETE FROM p_user WHERE id IN ('{id1}', '{id2}'); '''

#create test users
db_request(commit = True, sql = sql_insert)
result = db_request(commit = True, sql = sql_select)
id1, id2 = result[0][0], result[1][0]
#base data
friend_record1 = Friend_record()

def test_add():
    FriendRecordPropertry.setter(friend_record1, id1, id2)

    friend_recordService = Friend_recordService()
    result = friend_recordService.add(friend_record1)

    assert result

def test_get_all():
    friend_recordService = Friend_recordService()
    friend_record_list = friend_recordService.get_all()
    
    if len(friend_record_list) >= 1:
        friend_record1.id = friend_record_list[-1].id
        friend_record1.user_id = friend_record_list[-1].user_id
        friend_record1.friend_id = friend_record_list[-1].friend_id
        assert True
    else:
        assert False

def test_get_by_user_friend_id():
    friend_recordService = Friend_recordService()
    result = friend_recordService.get_by_user_friend_id(id1, id2)
    equal = result.equal(friend_record1)
    assert equal

def test_remove():
    global sql_delete
    friend_recordService = Friend_recordService()
    result = friend_recordService.remove(friend_record1)
    assert result

    sql_delete = sql_delete.format(id1 = id1, id2 = id2)
    result = db_request(commit = True, sql = sql_delete)