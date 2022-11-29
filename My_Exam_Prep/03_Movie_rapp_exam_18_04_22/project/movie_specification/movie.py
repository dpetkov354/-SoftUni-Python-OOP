from abc import ABC, abstractmethod
from project.func.validators import Validator


class Movie(ABC):

    AGE_RESTRICTION = 0

    @abstractmethod
    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if Validator.empty_string_title(value):
            self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if Validator.movie_year_check(value):
            self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if Validator.owner_is_user_object(value):
            self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.AGE_RESTRICTION:
            raise ValueError(
                f"{self.__class__.__name__} movies must be restricted for audience under {self.AGE_RESTRICTION} years!")
        self.__age_restriction = value

    def details(self):
        return f"{self.__class__.__name__} - Title:{self.title}, Year:{self.year}," \
               f" Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"
