AGE_RESTRICTION = 18
HORSE_NAME_LENGTH = 4


class Validation:

    @staticmethod
    def empty_string(value):
        if value.strip() != "":
            return True
        raise ValueError("Name should contain at least one character!")

    @staticmethod
    def age_above_age_restriction(value):
        if value >= AGE_RESTRICTION:
            return True
        raise ValueError(f"Jockeys must be at least {AGE_RESTRICTION} to participate in the race!")

    @staticmethod
    def horse_name_check(value):
        if len(value) >= HORSE_NAME_LENGTH:
            return True
        raise ValueError(f"Horse name {value} is less than {HORSE_NAME_LENGTH} symbols!")

    @staticmethod
    def horse_max_speed_limit_check(breed, value):
        max_speed = 0
        if breed == "Appaloosa":
            max_speed = 120
        elif breed == "Thoroughbred":
            max_speed = 140

        if value <= max_speed:
            return True
        raise ValueError("Horse speed is too high!")

    @staticmethod
    def horse_name_in_list_check(data_horse_names, horse_name):
        if any(x.name == horse_name for x in data_horse_names):
            raise Exception(f"Horse {horse_name} has been already added!")

    @staticmethod
    def jockey_name_in_list_check(data_jockey_names, jockey_name):
        if any(x.name == jockey_name for x in data_jockey_names):
            raise Exception(f"Jockey {jockey_name} has been already added!")

    @staticmethod  # may raise error to check
    def race_in_list_check(data_races, race):
        if any(x.race_type == race for x in data_races):
            raise Exception(f"Race {race} has been already created!")

    @staticmethod
    def check_race_type(value):
        if value == "Summer":
            return True
        elif value == "Winter":
            return True
        elif value == "Autumn":
            return True
        elif value == "Spring":
            return True
        raise ValueError("Race type does not exist!")
