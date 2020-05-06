from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from abc import ABC, abstractmethod
from main.storage.type_currency import Type_currency
from typing import List

class Type_currencyDAO(ABC):
    '''DAO for Type_currency entity'''

    @abstractmethod
    def add(self, type_currency: Type_currency) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> List[Type_currency]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Type_currency:
        pass

    @abstractmethod
    def update(self, type_currency: Type_currency) -> Type_currency:
        pass

    @abstractmethod
    def remove(self, type_currency: Type_currency) -> bool:
        pass    