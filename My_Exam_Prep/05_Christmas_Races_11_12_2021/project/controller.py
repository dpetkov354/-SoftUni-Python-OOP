from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.func.validator import Validator
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __find_driver_by_name(self, name):
        driver = [inst for inst in self.drivers if inst.name == name]
        if  driver:
            return  driver[0]

    def __find_race_by_name(self, name):
        race = [inst for inst in self.races if inst.name == name]
        if race:
            return race[0]

    def __find_car_by_type(self, car_type):
        car = [inst for inst in self.cars if inst.type == car_type and inst.is_taken == False]
        if car:
            return car[-1]

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type != "MuscleCar" and car_type != "SportsCar":
            return None
        Validator.car_model_in_list_check(self.cars, model)
        if car_type == "MuscleCar":
            car = MuscleCar(model, speed_limit)
            self.cars.append(car)
        elif car_type == "SportsCar":
            car = SportsCar(model, speed_limit)
            self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        Validator.driver_name_in_list_check(self.drivers, driver_name)
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        Validator.race_name_in_list_check(self.races, race_name)
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        car = self.__find_car_by_type(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")
        if driver.car is not None:
            driver.car.is_taken = False
            change = driver.car
            self.cars.remove(change)
            self.cars.append(change)
            old_car = driver.car.model
            driver.car = car
            return f"Driver {driver_name} changed his car from {old_car} to {driver.car.model}."
        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        driver = self.__find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_drivers = [driver for driver in sorted(race.drivers, key=lambda x: -x.car.speed_limit)][0:3]

        result = []
        for driver in fastest_drivers:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return "\n".join(result)
