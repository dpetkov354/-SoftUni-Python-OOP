from abc import ABC, abstractmethod

from project.func.validation import Validation


class Delicacy(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: int, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if Validation.empty_string(value):
            self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if Validation.check_positive_number(value):
            self.__price = value

    def details(self):
        pass
