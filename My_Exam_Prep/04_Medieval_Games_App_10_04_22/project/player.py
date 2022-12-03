from project.func.validator import Validator


class Player:
    STAMINA_DEFAULT_VALUE = 100
    players = []

    def __init__(self, name: str, age: int, stamina=STAMINA_DEFAULT_VALUE, need_sustenance=False):

        self.name = name
        self.age = age
        self.stamina = stamina
        self._need_sustenance = need_sustenance

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if Validator.empty_name(value):
            if value not in self.players:
                self.__name = value
                self.players.append(value)
            else:
                raise Exception(f"Name {value} is already used!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if Validator.check_age(value):
            self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if Validator.check_stamina(value):
            self.__stamina = value

    @property
    def need_sustenance(self):
        return self._need_sustenance

    @need_sustenance.setter
    def need_sustenance(self, value):
        if value < 100:
            self._need_sustenance = True

    def __str__(self):
        if self.stamina < 100:
            self._need_sustenance = True
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self._need_sustenance}"
