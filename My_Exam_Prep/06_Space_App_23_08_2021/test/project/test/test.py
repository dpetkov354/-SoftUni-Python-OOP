from project.library import Library
from unittest import TestCase, main


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.library = Library("Sofia")

    def test__init__(self):
        self.assertEqual("Sofia", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_successful_name_creation(self):
        self.library.name = "Plovdiv"
        self.assertEqual("Plovdiv", self.library.name)

    def test_unsuccessful_name_creation(self):
        with self.assertRaises(ValueError) as error:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(error.exception))

    def test__add_book__with_author(self):
        self.library.name = "Plovdiv"
        self.library.books_by_authors["Ivan Vazov"] = []

        self.library.add_book("Ivan Vazov", "Pod Igoto")

        self.assertEqual({"Ivan Vazov": ["Pod Igoto"]}, self.library.books_by_authors)

    def test__add_book__with_author_and_an_existing_book(self):
        self.library.name = "Plovdiv"
        self.library.books_by_authors["Ivan Vazov"] = ["Pod Igoto"]

        self.library.add_book("Ivan Vazov", "Shipka")

        self.assertEqual({"Ivan Vazov": ["Pod Igoto", "Shipka"]}, self.library.books_by_authors)

    def test__add_book__without_author(self):
        self.library.name = "Plovdiv"
        self.library.books_by_authors = {}

        self.library.add_book("Ivan Vazov", "Pod Igoto")

        self.assertEqual({"Ivan Vazov": ["Pod Igoto"]}, self.library.books_by_authors)

    def test__add_book__with_author_and_same_book(self):
        self.library.name = "Plovdiv"
        self.library.books_by_authors["Ivan Vazov"] = ["Pod Igoto"]

        self.library.add_book("Ivan Vazov", "Pod Igoto")

        self.assertEqual({"Ivan Vazov": ["Pod Igoto"]}, self.library.books_by_authors)

    def test__add_reader_successful(self):
        self.library.name = "Plovdiv"
        self.library.readers = {}
        self.assertEqual(0, len(self.library.readers))

        self.library.add_reader("Gosho")

        self.assertEqual(1, len(self.library.readers))
        self.assertEqual([], self.library.readers["Gosho"])

    def test__add_reader_unsuccessfully(self):
        self.library.name = "Plovdiv"
        self.library.readers = {}
        self.library.add_reader("Gosho")

        self.assertEqual("Gosho is already registered in the Plovdiv library.", self.library.add_reader("Gosho"))

    def test__rent_book_unsuccessfully_no_registered_reader(self):
        self.library.name = "Plovdiv"
        self.library.readers = {"Gosho": []}
        self.assertEqual("Pesho is not registered in the Plovdiv Library.", self.library.rent_book("Pesho", "Ivan Vazov", "Pod Igoto"))

    def test__rent_book_unsuccessfully_no_author(self):
        self.library.name = "Plovdiv"
        self.library.readers = {"Pesho": []}
        self.library.books_by_authors["Dimitar Dimov"] = ["Tiutiun"]
        self.assertEqual("Plovdiv Library does not have any Ivan Vazov's books.",
                         self.library.rent_book("Pesho", "Ivan Vazov", "Pod Igoto"))

    def test__rent_book_unsuccessfully_no_book(self):
        self.library.name = "Plovdiv"
        self.library.readers = {"Pesho": []}
        self.library.books_by_authors["Dimitar Dimov"] = ["Tiutiun"]
        self.assertEqual("""Plovdiv Library does not have Dimitar Dimov's "Osadeni dushi".""",
                         self.library.rent_book("Pesho", "Dimitar Dimov", "Osadeni dushi"))

    def test__rent_book_successfully(self):
        self.library.name = "Plovdiv"
        self.library.readers = {"Pesho": []}
        self.library.books_by_authors["Dimitar Dimov"] = ["Tiutiun", "Osadeni dushi"]

        self.assertEqual([], self.library.readers["Pesho"])
        self.assertEqual(1, len(self.library.readers))

        self.assertEqual(["Tiutiun", "Osadeni dushi"], self.library.books_by_authors["Dimitar Dimov"])
        self.assertEqual(1, len(self.library.books_by_authors))

        self.library.rent_book("Pesho", "Dimitar Dimov", "Tiutiun")

        self.assertEqual([{'Dimitar Dimov': 'Tiutiun'}], self.library.readers["Pesho"])
        self.assertEqual(["Osadeni dushi"], self.library.books_by_authors["Dimitar Dimov"])

if __name__ == "__main__":
    main()
