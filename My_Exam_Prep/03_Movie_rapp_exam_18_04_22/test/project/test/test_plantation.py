from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(20)

    def test_successful_initialization(self):
        self.assertEqual(20, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_unsuccessful_setter(self):
        with self.assertRaises(ValueError) as error:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(error.exception))

    def test_successful_hiring_worker_in_a_empty_list(self):
        self.plantation.hire_worker("Dimitar")
        self.assertEqual("Dimitar", self.plantation.workers[0])

    def test_successful_hiring_worker_in_a_populated_list(self):
        self.plantation.workers = ["Georgi"]
        self.assertEqual(1, len(self.plantation.workers))

        result = self.plantation.hire_worker("Dimitar")
        self.assertEqual("Dimitar successfully hired.", result)
        self.assertEqual(2, len(self.plantation.workers))

    def test_unsuccessful_hiring_of_worker(self):
        self.plantation.workers = ["Georgi"]
        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker("Georgi")

        self.assertEqual("Worker already hired!", str(error.exception))

    def test__len__function(self):
        self.plantation.plants = {
            "Dimitar": "Bonsai",
            "Zornitsa": "Orchid",
        }

        self.assertEqual(12, len(self.plantation))

    def test__planting__worker_missing(self):
        self.plantation.workers = ["Georgi"]
        with self.assertRaises(ValueError) as error:
            self.plantation.planting("Ivan", "Rose")

        self.assertEqual("Worker with name Ivan is not hired!", str(error.exception))

    def test_full_plantation_planting_func(self):
        plantation = Plantation(12)
        plantation.workers = ["Dimitar", "Zornitsa"]
        plantation.plants = {
            "Dimitar": "Bonsai",
            "Zornitsa": "Orchid",
        }
        with self.assertRaises(ValueError) as error:
            plantation.planting("Dimitar", "Rose")

        self.assertEqual("The plantation is full!", str(error.exception))

    def test_successful__planting(self):
        self.plantation.hire_worker("Dimitar")
        self.plantation.planting("Dimitar", "Rose")
        result = self.plantation.planting("Dimitar", "Orchid")

        self.assertEqual("Dimitar planted Orchid.", result)
        self.assertEqual(2, len(self.plantation.plants["Dimitar"]))

    def test_successful__planting_first_plant(self):
        self.plantation.hire_worker("Dimitar")
        result = self.plantation.planting("Dimitar", "Orchid")

        self.assertEqual("Dimitar planted it's first Orchid.", result)
        self.assertEqual(1, len(self.plantation.plants["Dimitar"]))

    def test__str__(self):
        self.plantation.workers = ["Dimitar", "Zornitsa"]
        self.plantation.plants = {
            "Dimitar": "Bonsai",
            "Zornitsa": "Orchid",
        }

        self.assertEqual("Plantation size: 20\n"
                         "Dimitar, Zornitsa\n"
                         "Dimitar planted: B, o, n, s, a, i\n"
                         "Zornitsa planted: O, r, c, h, i, d", str(self.plantation))

    def test__repr(self):
        self.plantation.workers = ["Dimitar", "Zornitsa"]

        self.assertEqual("Size: 20\n"
                         "Workers: Dimitar, Zornitsa", repr(self.plantation))


if __name__ == "__main__":
    main()
