class Product_record:
    '''Entity - product_record'''

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id


    @property
    def order_id(self) -> str:
        return self._order_id

    @order_id.setter
    def order_id(self, order_id: str) -> None:
        self._order_id = order_id


    @property
    def product_id(self) -> str:
        return self._product_id

    @product_id.setter
    def product_id(self, product_id: str) -> None:
        self._product_id = product_id


    def equal(self, price) -> bool:
        if ((self.id == price.id) and
            (self.order_id == price.order_id) and
            (self.product_id == price.product_id)):
            return True
        else:
            return False

    def __str__(self) -> str:
        str_instance = ''
        for string in ('Friend_record:{',
                       '   id=%s' % self._id,
                       '   order_id=%s' % self._order_id,
                       '   product_id=%s' % self._product_id,
                       '}'):
            str_instance += string + '\n'

        return str_instance