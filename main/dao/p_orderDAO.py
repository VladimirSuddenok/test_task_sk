from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from abc import ABC, abstractmethod
from main.storage.p_order import P_order
from typing import List

class P_orderDAO(ABC):
    '''DAO for P_order entity'''

    @abstractmethod
    def add(self, order: P_order) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> List[P_order]:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> P_order:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: str) -> List[P_order]:
        pass

    @abstractmethod
    def update(self, oreder: P_order) -> P_order:
        pass

    @abstractmethod
    def remove(self, order: P_order) -> bool:
        pass    