from typing import Dict
class Friend_record:
    '''Entity - friend_record'''

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id


    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str) -> None:
        self._user_id = user_id


    @property
    def friend_id(self) -> str:
        return self._friend_id

    @friend_id.setter
    def friend_id(self, friend_id: str) -> None:
        self._friend_id = friend_id


    def equal(self, friend_record) -> bool:
        if ((self.id == friend_record.id) and
            (self.user_id == friend_record.user_id) and 
            (self.friend_id == friend_record.friend_id)):
            return True
        else:
            return False

    def __str__(self) -> str:
        str_instance = ''
        for string in ('Friend_record:{',
                       '   id=%s' % self._id,
                       '   user_id=%s' % self._user_id,
                       '   friend_id=%s' % self._friend_id,
                       '}'):
            str_instance += string + '\n'

        return str_instance

    def to_dict(self) -> Dict:
        return {"id": self.id, "user_id": self.user_id, "friend_id": self.friend_id}