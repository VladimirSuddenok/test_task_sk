from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

import pytest
from project.main.service.p_userService import P_userService, P_user
from tests.property import UserProperty

#base data
p_user1 = P_user()
p_user2 = P_user()

def test_add():
    UserProperty.setter(p_user1)
    UserProperty.setter(p_user2)

    p_userService = P_userService()
    result1 = p_userService.add(p_user1)

    p_userService = P_userService()
    result2 = p_userService.add(p_user2)

    assert result1
    assert result2

def test_get_all():
    p_userService = P_userService()
    p_users_list = p_userService.get_all()
    
    if len(p_users_list) >= 2:
        p_user1.id = p_users_list[-2].id
        p_user2.id = p_users_list[-1].id
        assert True
    else:
        assert False

def test_get_by_id():
    p_userService = P_userService()
    result = p_userService.get_by_id(p_user1.id)
    equal = result.equal(p_user1)
    assert equal

def test_update():
    p_user1.middlename = 'new_middlename'
    p_userService = P_userService()
    result = p_userService.update(p_user1)

    equal = result.equal(p_user1)
    assert equal

def test_remove():
    p_userService = P_userService()
    result = p_userService.remove(p_user1)
    assert result

    p_userService = P_userService()
    result = p_userService.remove(p_user2)
    assert result