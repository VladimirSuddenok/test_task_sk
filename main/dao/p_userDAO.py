from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from abc import ABC, abstractmethod
from main.storage.p_user import P_user
from typing import List

class P_userDAO(ABC):
    '''DAO for p_user entity'''

    @abstractmethod
    def add(self, user: P_user) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> List[P_user]:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> P_user:
        pass

    @abstractmethod
    def update(self, user: P_user) -> P_user:
        pass

    @abstractmethod
    def remove(self, user: P_user) -> bool:
        pass    