from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from concurrent.futures import ThreadPoolExecutor
from main.service.p_userService import P_userService, P_user
from typing import Dict, Tuple
import asyncio

class UsersPolicy:
    KEYS = ('firstname','surname', 'sex', 'age')

    async def get_users(self):
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor(max_workers = 10) as pool:
            raw_result = await loop.run_in_executor(
                pool, P_userService().get_all)
            result = [data.to_dict() for data in raw_result]
        
        return {'result': result, 'message': 'done'}

    async def create_user(self, data):
        if await self.check_require_data(data = data, keys = UsersPolicy.KEYS):
            user = await self.get_fields_add(data = data)
            loop = asyncio.get_event_loop()

            with ThreadPoolExecutor(max_workers = 10) as pool:
                result = await loop.run_in_executor(
                    pool, P_userService().add, user)

            return {'result': result, 'message': 'done'}
        else:
            msg = 'next field is requered: firstname, ' + \
                                          'surname, sex, age'
            return {'result': False, 'message': msg}

    async def get_fields_add(self, data: Dict):
        p_user = P_user()
        p_user.firstname = data['firstname']
        p_user.surname = data['surname']
        p_user.middlename = '' if data['middlename'] == None \
                                                     else data['middlename']
        p_user.sex = data['sex']
        p_user.age = data['age']
        return p_user

    async def check_require_data(self, data: Dict, keys: Tuple):
        for field in keys:
            if data[field] is not None:
                continue
            else:
                break
        else:
            return True

        return False

    async def get_fields_update_delete(self, data: Dict):
        p_user = await self.get_fields_add(data = data)
        p_user.id = data['id']
        p_user.fio = '' if data.get('fio', None) == None \
                                            else data['fio']
        return p_user

    async def update_user(self, data: Dict):
        if await self.check_require_data(
                data = data, keys = list(UsersPolicy.KEYS) + ['id']):
            user = await self.get_fields_update_delete(data = data)
            loop = asyncio.get_event_loop()

            with ThreadPoolExecutor(max_workers = 10) as pool:
                result = await loop.run_in_executor(
                    pool, P_userService().update, user)

            return {'result': result.to_dict(), 'message': 'done'}
        else:
            msg = 'next field is requered: '  + \
                  'firstname, surname, sex, age'
            return {'result': False, 'message': msg}

    async def delete_user(self, data: Dict):
        if await self.check_require_data(
                data = data, keys = list(UsersPolicy.KEYS) + ['id']):
            user = await self.get_fields_update_delete(data = data)
            loop = asyncio.get_event_loop()

            with ThreadPoolExecutor(max_workers = 10) as pool:
                result = await loop.run_in_executor(
                    pool, P_userService().remove, user)

            return {'result': result, 'message': 'done'}
        else:
            msg = 'next field is requered: '  + \
                  'firstname, surname, sex, age'
            return {'result': False, 'message': msg}
