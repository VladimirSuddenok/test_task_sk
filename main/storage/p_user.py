from typing import Dict
class P_user:
    '''Entity - p_user'''

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        self._id = id
    

    @property
    def firstname(self) -> str:
        return self._firstname

    @firstname.setter
    def firstname(self, firstname: str) -> None:
        self._firstname = firstname
    

    @property
    def surname(self) -> str:
        return self._surname

    @surname.setter
    def surname(self, surname: str) -> None:
        self._surname = surname


    @property
    def middlename(self) -> str:
        return self._middlename

    @middlename.setter
    def middlename(self, middlename: str) -> None:
        self._middlename = middlename


    @property
    def fio(self) -> str:
        return self._fio

    @fio.setter
    def fio(self, fio: str) -> None:
        self._fio = fio
    

    @property
    def sex(self) -> str:
        return self._sex

    @sex.setter
    def sex(self, sex: str) -> None:
        self._sex = sex


    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    def equal(self, p_user) -> bool:
        if ((self.id == p_user.id) and
            (self.firstname == p_user.firstname) and 
            (self.surname == p_user.surname) and 
            (self.middlename == p_user.middlename) and 
            (self.sex == p_user.sex) and 
            (self.age == p_user.age)):
            return True
        else:
            return False

    def __str__(self) -> str:
        str_instance = ''
        for string in ('P_user:{',
                       '   id=%s' % self._id,
                       '   firstname=%s' % self._firstname,
                       '   surname=%s' % self._surname,
                       '   middlename=%s' % self._middlename,
                       '   fio=%s' % self._fio,
                       '   sex=%s' % self._sex,
                       '   age=%s' % self._age,
                       '}'):
            str_instance += string + '\n'

        return str_instance

    def to_dict(self) -> Dict:
        return {'id': self._id, 'firstname': self._firstname,
                'surname': self._surname, 'middlename': self._middlename,
                'fio': self._fio, 'sex': self._sex, 'age': self._age}