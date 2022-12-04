from project.team import Team
from unittest import TestCase, main


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.team = Team("Levski")

    def test__init__(self):
        self.assertEqual("Levski", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_successful_name_set(self):
        self.team.name = "Levski"
        self.assertEqual("Levski", self.team.name)

    def test_not_only_letters_name(self):
        with self.assertRaises(ValueError) as error:
            self.team.name = "Levski1"
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

    def test_successful_add_one_member(self):
        self.team = Team("Levski")
        self.assertEqual("Levski", self.team.name)
        self.assertEqual(0, len(self.team.members))

        self.team.add_member(name_age={"Ivan": 20})
        self.assertEqual(1, len(self.team.members))

    def test_successful_add_second_member(self):
        self.team = Team("Levski")
        self.team.members = {"Ivan": 20}
        self.assertEqual("Levski", self.team.name)
        self.assertEqual(1, len(self.team.members))

        self.team.add_member(Dimitar= 21)
        self.assertEqual(2, len(self.team.members))

    def test_unsuccessful_add_second_member(self):
        self.team = Team("Levski")
        self.team.members = {"Ivan": 20}
        self.assertEqual("Levski", self.team.name)
        self.assertEqual(1, len(self.team.members))

        self.assertEqual("Successfully added: ", self.team.add_member(Ivan=20))
        self.assertEqual(1, len(self.team.members))

    def test_successful_two_member(self):
        self.team = Team("Levski")
        self.team.members = {"Ivan": 20}
        self.assertEqual("Levski", self.team.name)
        self.assertEqual(1, len(self.team.members))

        self.team.add_member(Dimitar= 21, Georgi=22)
        self.assertEqual(3, len(self.team.members))

    def test_successful_remove_member(self):
        self.team = Team("Levski")
        self.team.members = {"Ivan": 20, "Dimitar": 21,}
        self.assertEqual("Levski", self.team.name)
        self.assertEqual(2, len(self.team.members))

        self.assertEqual("Member Ivan removed", self.team.remove_member("Ivan"))
        self.assertEqual(1, len(self.team.members))

    def test__gt__successful(self):
        self.team1 = Team("Levski")
        self.team1.members = {"Ivan": 20, "Dimitar": 21,}
        self.team2 = Team("CSKA")
        self.team2.members = {"Pesho": 22,}

        self.assertEqual(True, self.team1 > self.team2)

    def test__gt__unsuccessful(self):
        self.team1 = Team("Levski")
        self.team1.members = {"Ivan": 20, "Dimitar": 21, }
        self.team2 = Team("CSKA")
        self.team2.members = {"Pesho": 22, }

        self.assertEqual(False, self.team2 > self.team1)

    def test__len__(self):
        self.team1 = Team("Levski")
        self.team1.members = {"Ivan": 20, "Dimitar": 21, }

        self.assertEqual(2, len(self.team1))

    def test__add__(self):
        self.team1 = Team("Levski")
        self.team1.members = {"Ivan": 20, "Dimitar": 21, }
        self.team2 = Team("CSKA")
        self.team2.members = {"Pesho": 22, }


        self.assertEqual("LevskiCSKA", (self.team1+self.team2).name)
        self.assertEqual(3, len((self.team1+self.team2).members))

    def test__str__(self):
        self.team1 = Team("Levski")
        self.team1.members = {"Ivan": 20, "Dimitar": 21, }

        check = f"Team name: Levski\n" \
                f"Member: Dimitar - 21-years old\n" \
                f"Member: Ivan - 20-years old"

        self.assertEqual(check, str(self.team1))


if __name__ == "__main__":
    main()