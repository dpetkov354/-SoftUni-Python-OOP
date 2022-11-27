from project.func.validators import Validation


class Jockey:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if Validation.empty_string(value):
            self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if Validation.age_above_age_restriction(value):
            self.__age = value

