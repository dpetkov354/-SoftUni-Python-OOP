from project.func.validators import Validator


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if Validator.empty_string_name(value):
            self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if Validator.age_check(value):
            self.__age = value

    def __str__(self):
        result = [f"Username: {self.username}, Age: {self.age}", "Liked movies:"]

        if len(self.movies_liked) > 0:
            for movie in self.movies_liked:
                result.append(f"{movie.details()}")
        else:
            result.append(f"No movies liked.")

        result.append("Owned movies:")

        if len(self.movies_owned) > 0:
            for movie in self.movies_owned:
                result.append(f"{movie.details()}")
        else:
            result.append(f"No movies owned.")

        return '\n'.join(result)
