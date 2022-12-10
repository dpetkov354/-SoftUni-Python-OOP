from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_successful_initialization(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)

    def test_successful_return_of__add_toy(self):
        self.assertEqual("Toy:Transformer placed successfully!", self.toy_store.add_toy("A", "Transformer"))

    def test_successful_adding_to_the_shelf__add_toy(self):
        self.toy_store.add_toy("A", "Transformer")
        self.assertEqual("Transformer", self.toy_store.toy_shelf["A"])

    def test_unsuccessful__add_toy_no_such_shelf(self):
        with self.assertRaises(Exception) as error:
            self.toy_store.add_toy("Z", "Transformer")

        self.assertEqual("Shelf doesn't exist!", str(error.exception))

    def test_unsuccessful__add_toy_toy_exists(self):
        self.toy_store.add_toy("A", "Transformer")
        with self.assertRaises(Exception) as error:
            self.toy_store.add_toy("A", "Transformer")
        self.assertEqual("Toy is already in shelf!", str(error.exception))

    def test_unsuccessful__add_toy_shelf_taken(self):
        self.toy_store.add_toy("A", "Transformer")
        with self.assertRaises(Exception) as error:
            self.toy_store.add_toy("A", "HotWheels Car")
        self.assertEqual("Shelf is already taken!", str(error.exception))

    def test_successful_return_of__remove_toy(self):
        self.toy_store.add_toy("A", "Transformer")
        self.assertEqual("Remove toy:Transformer successfully!", self.toy_store.remove_toy("A", "Transformer"))

    def test_successful_of__remove_toy(self):
        self.toy_store.add_toy("A", "Transformer")
        self.assertEqual("Transformer", self.toy_store.toy_shelf["A"])
        self.toy_store.remove_toy("A", "Transformer")
        self.assertEqual(None, self.toy_store.toy_shelf["A"])

    def test_unsuccessful__remove_toy_no_such_shelf(self):
        self.toy_store.add_toy("A", "Transformer")
        with self.assertRaises(Exception) as error:
            self.toy_store.remove_toy("Z", "Transformer")
        self.assertEqual("Shelf doesn't exist!", str(error.exception))

    def test_unsuccessful__remove_toy_no_such_toy_in_shelf(self):
        self.toy_store.add_toy("A", "Transformer")
        with self.assertRaises(Exception) as error:
            self.toy_store.remove_toy("A", "HotWheels Car")
        self.assertEqual("Toy in that shelf doesn't exists!", str(error.exception))

if __name__ == "__main__":
    main()
