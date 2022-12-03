from project.movie import Movie
from unittest import TestCase, main


class TestUnit(TestCase):

    def setUp(self) -> None:
        self.movie = Movie("StarWars", 1972, 8.5)

    def test_init(self):
        movie_name = "StarWars"
        movie_year = 1972
        movie_rating = 8.5

        self.assertEqual(movie_name, self.movie.name)
        self.assertEqual(movie_year, self.movie.year)
        self.assertEqual(movie_rating, self.movie.rating)

    def test_empty_name_string(self):
        movie_name = ""
        with self.assertRaises(ValueError) as error:
            self.movie.name = movie_name

        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test_age_below_1887(self):
        movie_year = 1886
        with self.assertRaises(ValueError) as error:
            self.movie.year = movie_year

        self.assertEqual("Year is not valid!", str(error.exception))

    def test_add_actor_successful(self):
        self.movie = Movie("StarWars", 1972, 8.5)
        self.assertEqual(0, len(self.movie.actors))
        self.movie.add_actor("Ivan")
        self.assertEqual(1, len(self.movie.actors))
        self.assertEqual("Ivan", self.movie.actors[0])

    def test_add_actor_unsuccessfully(self):
        self.movie = Movie("StarWars", 1972, 8.5)
        self.assertEqual(0, len(self.movie.actors))
        self.movie.add_actor("Ivan")
        self.assertEqual("Ivan is already added in the list of actors!", self.movie.add_actor("Ivan"))

    def test__gt__if_statement(self):
        self.movie1 = Movie("StarWars", 1972, 8.5)
        self.movie2 = Movie("HarryPotter", 2001, 7.5)

        self.assertEqual(f'"StarWars" is better than "HarryPotter"', self.movie1 > self.movie2)

    def test__gt__else_statement(self):
        self.movie1 = Movie("StarWars", 1972, 6.5)
        self.movie2 = Movie("HarryPotter", 2001, 7.5)

        self.assertEqual(f'"HarryPotter" is better than "StarWars"', self.movie1 > self.movie2)

    def test__repr__(self):
        self.movie = Movie("StarWars", 1972, 8.5)
        self.movie.add_actor("James Earl Jones")
        self.movie.add_actor("Mark Hamil")

        check = f"Name: StarWars\n" \
               f"Year of Release: 1972\n" \
               f"Rating: 8.50\n" \
               f"Cast: James Earl Jones, Mark Hamil"

        self.assertEqual(check, repr(self.movie))


if __name__ == "__main__":
    main()
