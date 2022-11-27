from project.bookstore import Bookstore
from unittest import TestCase, main


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.bookstore = Bookstore(100)

    def test_successful_initialization(self):
        self.assertEqual(100, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_total_books_sold(self):
        bookstore = Bookstore(30)
        bookstore.receive_book("Rise of the Lich King", 5)
        bookstore.receive_book("Star Wars", 5)
        bookstore.receive_book("Harry Potter", 5)
        bookstore.sell_book("Harry Potter", 2)
        self.assertEqual(bookstore.total_sold_books, 2)

    def test_raise_error_book_limit_equals_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_raise_error_book_limit_equals_below_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -5000

        self.assertEqual("Books limit of -5000 is not valid", str(ve.exception))

    def test_len_function(self):
        bookstore = Bookstore(20)
        bookstore.availability_in_store_by_book_titles = {
            "Harry Potter": 10,
            "Star Wars": 5,
        }
        self.assertEqual(15, len(bookstore))

    def test_unsuccessful__receive_book(self):
        bookstore = Bookstore(10)

        with self.assertRaises(Exception) as ex:
            bookstore.receive_book("Rise of the Lich King", 11)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_successful__receive_book(self):
        bookstore = Bookstore(20)
        self.assertEqual(f"11 copies of Rise of the Lich King are available in the bookstore.",
                         bookstore.receive_book("Rise of the Lich King", 11))

    def test_successful__receive_book_new_book(self):
        self.bookstore.availability_in_store_by_book_titles = {"Harry Potter": 3}
        result = self.bookstore.receive_book("Rise of the Lich King", 11)
        self.assertEqual(f"11 copies of Rise of the Lich King are available in the bookstore.", result)
        self.assertEqual(2, len(self.bookstore.availability_in_store_by_book_titles))
        result = self.bookstore.receive_book("Rise of the Lich King", 11)
        self.assertEqual(f"22 copies of Rise of the Lich King are available in the bookstore.", result)
        self.assertEqual(2, len(self.bookstore.availability_in_store_by_book_titles))

    def test_unsuccessful__sell_book__book_unavailable(self):
        bookstore = Bookstore(10)

        with self.assertRaises(Exception) as ex:
            bookstore.sell_book("Rise of the Lich King", 11)

        self.assertEqual("Book Rise of the Lich King doesn't exist!", str(ex.exception))

    def test_unsuccessful__sell_book__book_quantity_not_enough(self):
        bookstore = Bookstore(30)
        bookstore.receive_book("Rise of the Lich King", 11)

        with self.assertRaises(Exception) as ex:
            bookstore.sell_book("Rise of the Lich King", 20)

        self.assertEqual("Rise of the Lich King has not enough copies to sell. Left: 11", str(ex.exception))

    def test_successful__sell_book(self):
        self.bookstore.receive_book("Rise of the Lich King", 11)
        self.assertEqual(f"Sold 6 copies of Rise of the Lich King",
                         self.bookstore.sell_book("Rise of the Lich King", 6))
        self.bookstore.receive_book("Star Wars", 11)
        self.assertEqual(f"Sold 11 copies of Star Wars", self.bookstore.sell_book("Star Wars", 11))
        self.assertEqual(5, self.bookstore.availability_in_store_by_book_titles["Rise of the Lich King"])
        self.assertEqual(17, self.bookstore.total_sold_books)

    def test__str__and_total_sold_books(self):
        bookstore = Bookstore(30)
        bookstore.receive_book("Rise of the Lich King", 5)
        bookstore.receive_book("Star Wars", 5)
        bookstore.receive_book("Harry Potter", 5)
        bookstore.sell_book("Harry Potter", 2)

        self.assertEqual("Total sold books: 2\n"
                         "Current availability: 13\n"
                         " - Rise of the Lich King: 5 copies\n"
                         " - Star Wars: 5 copies\n"
                         " - Harry Potter: 3 copies", str(bookstore))


if __name__ == "__main__":
    main()
