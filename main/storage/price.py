from typing import Dict
class Price:
    '''Entity - price'''

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id


    @property
    def product_id(self) -> str:
        return self._product_id

    @product_id.setter
    def product_id(self, product_id: str) -> None:
        self._product_id = product_id


    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, amount: int) -> None:
        self._amount = amount


    @property
    def type_currency_id(self) -> int:
        return self._type_currency_id

    @type_currency_id.setter
    def type_currency_id(self, type_currency_id: int) -> None:
        self._type_currency_id = type_currency_id


    def equal(self, price) -> bool:
        if ((self.id == price.id) and
            (self.product_id == price.product_id) and
            (self.amount == price.amount) and 
            (self.type_currency_id == price.type_currency_id)):
            return True
        else:
            return False

    def __str__(self) -> str:
        str_instance = ''
        for string in ('Price:{',
                       '   id=%s' % self._id,
                       '   product_id=%s' % self._product_id,
                       '   amount=%s' % self._amount,
                       '   type_currency_id=%s' % self.type_currency_id,
                       '}'):
            str_instance += string + '\n'

        return str_instance

    def to_dict(self) -> Dict:
        return {'id': self.id, 'product_id': self.product_id,
                'amount': self.amount,
                'type_currency_id': self.type_currency_id}