from abc import ABC, abstractmethod
from project.func.validators import Validation

TRAINING_INCREASE = 0


class Horse(ABC):

    @abstractmethod
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if Validation.empty_string(value) and Validation.horse_name_check(value):
            self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if Validation.horse_max_speed_limit_check(self.breed, value):
            self.__speed = value

    @abstractmethod
    def train(self):
        self.speed += TRAINING_INCREASE
        return self.speed
