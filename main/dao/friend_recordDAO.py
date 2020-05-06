from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from abc import ABC, abstractmethod
from main.storage.friend_record import Friend_record
from typing import List

class Friend_recordDAO(ABC):
    '''DAO for Friend_record entity'''

    @abstractmethod
    def add(self, friend_record: Friend_record) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> List[Friend_record]:
        pass

    @abstractmethod
    def get_by_user_friend_id(self, user_id: str, 
                              friend_id: str) -> Friend_record:
        pass

    #@abstractmethod
    #def get_by_friend_id(self, friend_id: str) -> List[Friend_record]:
    #    pass

    #@abstractmethod
    #def update(self, friend_record: Friend_record) -> Friend_record:
    #    pass

    @abstractmethod
    def remove(self, friend_record: Friend_record) -> bool:
        pass    