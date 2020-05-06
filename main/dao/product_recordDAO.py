from pathlib import Path
import sys 
sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

from abc import ABC, abstractmethod
from main.storage.product_record import Product_record
from typing import List

class Product_recordDAO(ABC):
    '''DAO for Product_record entity'''

    @abstractmethod
    def add(self, product_record: Product_record) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> List[Product_record]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Product_record:
        pass

    @abstractmethod
    def get_by_product_id(self, product_id: str) -> List[Product_record]:
        pass

    @abstractmethod
    def get_by_order_id(self, order_id: str) -> List[Product_record]:
        pass

    #@abstractmethod
    #def update(self, product_record: Product_record) -> Product_record:
    #    pass

    @abstractmethod
    def remove(self, product_record: Product_record) -> bool:
        pass    