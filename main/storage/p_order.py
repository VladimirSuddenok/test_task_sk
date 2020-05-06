class P_order:
    '''Entity - p_order'''

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        self._id = id


    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, number: int) -> None:
        self._number = number


    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str) -> None:
        self._user_id = user_id


    def equal(self, p_order) -> bool:
        if ((self.id == p_order.id) and
            (self.number == p_order.number) and 
            (self.user_id == p_order.user_id)):
            return True
        else:
            return False
            

    def __str__(self) -> str:
        str_instance = ''
        for string in ('P_order:{',
                       '   id=%s' % self._id,
                       '   number=%s' % self._number,
                       '   user_id=%s' % self._user_id,
                       '}'):
            str_instance += string + '\n'

        return str_instance