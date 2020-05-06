from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from aiohttp.web import View, json_response
from main.policy.friends_policy import FriendsPolicy
from typing import Iterable
import json

class FriendsView(View):

    KEYS = ('user_id', 'friend_id')

    async def get(self):
        result = await FriendsPolicy().get_friends()
        return json_response(result)

    async def get_dict_data(self, keys: Iterable):
        data = dict()
        request = await self.request.json()
        for key in keys:
            data[key] = request.get(key, None)
        return data

    async def post(self):
        data = await self.get_dict_data(keys = FriendsView.KEYS)
        result = await FriendsPolicy().add_friend(data = data)
        return json_response(result)
