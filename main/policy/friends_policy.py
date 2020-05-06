from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from concurrent.futures import ThreadPoolExecutor
from main.service.friend_recordService import Friend_recordService, Friend_record
from typing import Dict, Tuple
import asyncio

class FriendsPolicy:
    KEYS = ('user_id', 'friend_id')

    async def get_friends(self):
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor(max_workers = 10) as pool:
            raw_result = await loop.run_in_executor(
                pool, Friend_recordService().get_all)
            result = [data.to_dict() for data in raw_result]
        
        return {'result': result, 'message': 'done'}

    async def add_friend(self, data):
        if await self.check_require_data(data = data, keys = FriendsPolicy.KEYS):
            friend_record = await self.get_fields_add(data = data)
            loop = asyncio.get_event_loop()

            with ThreadPoolExecutor(max_workers = 10) as pool:
                result = await loop.run_in_executor(
                    pool, Friend_recordService().add, friend_record)

            return {'result': result, 'message': 'done'}
        else:
            msg = 'next field is requered: user_id, friend_id'
            return {'result': False, 'message': msg}

    async def get_fields_add(self, data: Dict):
        friend_record = Friend_record()
        friend_record.user_id = data['user_id']
        friend_record.friend_id = data['friend_id']
        return friend_record

    async def check_require_data(self, data: Dict, keys: Tuple):
        for field in keys:
            if data[field] is not None:
                continue
            else:
                break
        else:
            return True

        return False