from project.func.validators import Validator
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def find_user_by_username(self, username):
        user = [u for u in self.users_collection if u.username == username]
        if user:
            return user[0]

    def register_user(self, username: str, age: int):
        Validator.existing_client(self.users_collection, username)

        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        find_user = self.find_user_by_username(username)
        Validator.missing_client(self.users_collection, username)
        Validator.check_if_user_is_not_the_owner(find_user, movie)
        Validator.movie_already_added(self.movies_collection, movie)
        self.movies_collection.append(movie)
        find_user.movies_owned.append(movie)
        return f"{find_user.username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        find_user = self.find_user_by_username(username)
        Validator.missing_movie(self.movies_collection, movie)
        Validator.check_if_user_is_not_the_owner(find_user, movie)
        for kwarg in kwargs.items():
            if kwarg[0] == "title":
                movie.title = kwarg[1]
            elif kwarg[0] == "year":
                movie.year = kwarg[1]
            elif kwarg[0] == "age_restriction":
                movie.age_restriction = kwarg[1]
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        find_user = self.find_user_by_username(username)
        Validator.missing_movie(self.movies_collection, movie)
        Validator.check_if_user_is_not_the_owner(find_user, movie)
        self.movies_collection.remove(movie)
        find_user.movies_owned.remove(movie)
        return f"{find_user.username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        find_user = self.find_user_by_username(username)
        Validator.check_if_user_is_the_owner(find_user, movie)
        Validator.check_if_movie_is_liked_by_user(find_user, movie)
        movie.likes += 1
        find_user.movies_liked.append(movie)
        return f"{find_user.username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        find_user = self.find_user_by_username(username)
        Validator.check_if_movie_is_not_liked_by_user(find_user, movie)
        movie.likes -= 1
        find_user.movies_liked.remove(movie)
        return f"{find_user.username} disliked {movie.title} movie."

    def display_movies(self):
        result = []
        if len(self.movies_collection) < 1:
            return "No movies found."
        sorted_list = sorted(self.movies_collection, key=lambda x: (x.year, x.title), reverse=True)
        for movie in sorted_list:
            result.append(f"{movie.details()}")
        return "\n".join(result)

    def __str__(self):
        result = ""
        if len(self.users_collection) < 1:
            result += "All users: No users."
        else:
            user_names = [user.username for user in self.users_collection]
            result += f"All users: {', '.join(user_names)}"
        result += "\n"
        if len(self.movies_collection) < 1:
            result += "All movies: No movies."
        else:
            movie_names = [movie.title for movie in self.movies_collection]
            result += f"All movies: {', '.join(movie_names)}"
        return result

