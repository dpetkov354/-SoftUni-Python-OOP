from project.car.car import Car
from project.func.validator import Validator


class Driver:
    def __init__(self, name: str, number_of_wins=0):
        self.name = name
        self.car = None
        self.number_of_wins = number_of_wins

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if Validator.empty_string(value):
            self.__name  = value
