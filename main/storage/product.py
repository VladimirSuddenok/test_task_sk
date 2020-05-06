from typing import Dict
class Product:
    '''Entity - product'''

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        self._id = id


    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name


    @property
    def descriptions(self) -> str:
        return self._descriptions

    @descriptions.setter
    def descriptions(self, descriptions) -> None:
        self._descriptions = descriptions

    
    @property
    def left_in_stock(self) -> int:
        return self._left_in_stock

    @left_in_stock.setter
    def left_in_stock(self, left_in_stock) -> None:
        self._left_in_stock = left_in_stock

    def equal(self, product) -> bool:
        if ((self.id == product.id) and
            (self.name == product.name) and
            (self.descriptions == product.descriptions) and 
            (self.left_in_stock == product.left_in_stock)):
            return True
        else:
            return False

    def __str__(self) -> str:
        str_instance = ''
        for string in ('Product:{',
                       '   id=%s' % self._id,
                       '   name=%s' % self._name,
                       '   descriptions=%s' % self._descriptions,
                       '   left_in_stock=%s' % self._left_in_stock,
                       '}'):
            str_instance += string + '\n'

        return str_instance


    def to_dict(self) -> Dict:
        return {'id': self.id, 'name': self.name,
                'descriptions': self.descriptions,
                'left_in_stock': self.left_in_stock}