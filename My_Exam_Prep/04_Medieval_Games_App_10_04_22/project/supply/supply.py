from abc import ABC, abstractmethod
from project.func.validator import Validator


class Supply(ABC):
    @abstractmethod
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if Validator.empty_string(value):
            self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if Validator.less_than_zero(value):
            self.__energy = value

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
