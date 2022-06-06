class Human:
    def __init__(self, name: str, age: int, gender: str):
        self.__name = name
        self.__age = age
        self._gender = gender
        self.__status = 'alive'
        self.__age_limit = 105
        self.friends = []

    @property
    def status(self):
        return self.__status

    @property
    def age(self) -> int:
        return self.__age

    def grow(self):
        self.__is_alive()
        if self.__age < self.__age_limit:
            self.__age += 1
        else:
            self.__status = 'dead'

    @property
    def name(self):
        return self.__name

    def change_name(self, new_name):
        self.__is_alive()
        if not new_name[0].isupper() and len(new_name) < 10:
            raise SyntaxError('Name should starts with capital letter')
        self.__name = new_name

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_gender):
        if new_gender not in ['male', 'female']:
            raise Exception('Gender is not as expected')
        self._gender = new_gender

    def make_friends(self, new_friend):
        """:param new_friend: Human , another Human object"""
        if new_friend.__status == 'alive':
            self.friends.append(new_friend)

    def get_friends(self):
        return self.friends

    def __is_alive(self):
        if self.__status == 'alive':
            return True
        else:
            raise Exception(f'{self.__name} is already dead')
