from abc import ABC, abstractmethod
from project.func.validation import Validation


class Booth(ABC):
    @abstractmethod
    def __init__(self, booth_number: int,  capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if Validation.check_positive_capacity(value):
            self.__capacity = value

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True
