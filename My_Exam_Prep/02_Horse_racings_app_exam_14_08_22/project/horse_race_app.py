from project.func.validators import Validation
from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def find_jockey_by_name(self, name):
        jockey = [inst for inst in self.jockeys if inst.name == name]
        if jockey:
            return jockey[0]

    def find_available_horse_by_type(self, horse_type):
        horses = [horse for horse in self.horses if horse.__class__.__name__ == horse_type and horse.is_taken is False]
        if horses:
            return horses

    def find_race_by_type(self, race_type):
        race = [r for r in self.horse_races if r.race_type == race_type]
        if race:
            return race[0]

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type != "Appaloosa" and horse_type != "Thoroughbred":
            return None
        Validation.horse_name_in_list_check(self.horses, horse_name)
        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
            self.horses.append(horse)
        elif horse_type == "Thoroughbred":
            horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        Validation.jockey_name_in_list_check(self.jockeys, jockey_name)
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.find_race_by_type(race_type):
            raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_jockey_by_name(jockey_name)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        available_horses = self.find_available_horse_by_type(horse_type)
        if not available_horses:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        last_added_horse = available_horses[-1]

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = last_added_horse
        jockey.horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {jockey.horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.find_race_by_type(race_type)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.find_jockey_by_name(jockey_name)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.find_race_by_type(race_type)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        fastest_jockeys = [jockey for jockey in sorted(race.jockeys, key=lambda x: -x.horse.speed)][0:1]

        return f"The winner of the {race_type} race, with a speed of {fastest_jockeys[0].horse.speed}km/h is {fastest_jockeys[0].name}! Winner's horse: {fastest_jockeys[0].horse.name}."
