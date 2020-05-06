from typing import Dict 
class Type_currency:
    '''Entity - type_currency'''

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id


    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name
    

    def equal(self, type_currency) -> bool:
        if ((self.id == type_currency.id) and
            (self.name == type_currency.name)):
            return True
        else:
            return False

    def __str__(self) -> str:
        str_instance = ''
        for string in ('Type_currency:{',
                       '   id=%s' % self._id,
                       '   name=%s' % self._name,
                       '}'):
            str_instance += string + '\n'

        return str_instance

    def to_dict(self) -> Dict:
        return {'id': self.id, 'name': self.name}