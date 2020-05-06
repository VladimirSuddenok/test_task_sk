from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from abc import ABC, abstractmethod
from main.storage.price import Price
from typing import List

class PriceDAO(ABC):
    '''DAO for Price entity'''

    @abstractmethod
    def add(self, price: Price) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> List[Price]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Price:
        pass

    @abstractmethod
    def get_by_product_id(self, product_id: str) -> List[Price]:
        pass

    @abstractmethod
    def update(self, price: Price) -> Price:
        pass

    @abstractmethod
    def remove(self, price: Price) -> bool:
        pass    