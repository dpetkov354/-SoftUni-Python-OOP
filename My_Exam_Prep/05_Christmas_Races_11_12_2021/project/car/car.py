from abc import ABC, abstractmethod

from project.func.validator import Validator


class Car(ABC):
    @abstractmethod
    def __init__(self,model: str, speed_limit: int, is_taken=False):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = is_taken

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if Validator.input_lenght_check(value):
            self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if Validator.speed_limit_check(self.type, value):
            self.__speed_limit = value
