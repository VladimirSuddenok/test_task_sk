from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from abc import ABC, abstractmethod
from main.storage.product import Product
from typing import List

class ProductDAO(ABC):
    '''DAO for Product entity'''

    @abstractmethod
    def add(self, product: Product) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> List[Product]:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Product:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Product:
        pass

    @abstractmethod
    def update(self, product: Product) -> Product:
        pass

    @abstractmethod
    def remove(self, product: Product) -> bool:
        pass    