class Validator:
    @staticmethod
    def empty_string_name(value):
        if value.strip() != "":
            return True
        raise ValueError("Invalid username!")

    @staticmethod
    def empty_string_title(value):
        if value.strip() != "":
            return True
        raise ValueError("The title cannot be empty string!")

    @staticmethod
    def age_check(value):
        if value >= 6:
            return True
        raise ValueError("Users under the age of 6 are not allowed!")

    @staticmethod
    def movie_year_check(value):
        if value >= 1888:
            return True
        raise ValueError("Movies weren't made before 1888!")

    @staticmethod
    def owner_is_user_object(value):  # TODO check if it works
        if value.__class__.__name__ == "User":
            return True
        raise ValueError("The owner must be an object of type User!")

    @staticmethod
    def fantasy_movie_age_restriction(value):
        if value >= 6:
            return True
        raise ValueError("Fantasy movies must be restricted for audience under 6 years!")

    @staticmethod
    def existing_client(data_user, user_name):
        if any(x.username == user_name for x in data_user):
            raise Exception("User already exists!")

    @staticmethod
    def missing_client(data_user, user_name):
        if not any(x.username == user_name for x in data_user):
            raise Exception("This user does not exist!")

    @staticmethod
    def check_if_user_is_not_the_owner(user, movie_object):
        if movie_object.owner == user:
            return True
        raise Exception(f"{user.username} is not the owner of the movie {movie_object.title}!")

    @staticmethod
    def movie_already_added(data_movie, movie_object):
        if any(x.title == movie_object.title for x in data_movie):
            raise Exception("Movie already added to the collection!")

    @staticmethod
    def missing_movie(data_movie, movie):
        if not any(x == movie for x in data_movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")

    @staticmethod
    def check_if_user_is_the_owner(user, movie_object):
        if movie_object.owner != user:
            return True
        raise Exception(f"{user.username} is the owner of the movie {movie_object.title}!")

    @staticmethod
    def check_if_movie_is_liked_by_user(user, movie):
        if movie not in user.movies_liked:
            return True
        raise Exception(f"{user.username} already liked the movie {movie.title}!")

    @staticmethod
    def check_if_movie_is_not_liked_by_user(user, movie):
        if movie in user.movies_liked:
            return True
        raise Exception(f"{user.username} has not liked the movie {movie.title}!")
