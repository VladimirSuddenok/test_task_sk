from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from aiohttp.web import View, json_response
from main.policy.users_policy import UsersPolicy
from typing import Iterable
import json

class UsersView(View):

    KEYS = ('firstname', 'surname',
            'middlename', 'sex', 'age')

    async def get_dict_data(self, keys: Iterable):
        data = dict()
        request = await self.request.json()
        for key in keys:
            data[key] = request.get(key, None)
        return data

    async def get(self):
        result = await UsersPolicy().get_users()
        return json_response(result)

    async def post(self):
        data = await self.get_dict_data(keys = UsersPolicy.KEYS)
        result = await UsersPolicy().create_user(data = data)
        return json_response(result)
    
    async def put(self):
        data = await self.get_dict_data(keys = list(UsersPolicy.KEYS) + ['id'])
        result = await UsersPolicy().update_user(data = data)
        return json_response(result)

    async def delete(self):
        data = await self.get_dict_data(keys = list(UsersPolicy.KEYS) + ['id'])
        result = await UsersPolicy().delete_user(data = data)
        return json_response(result)
