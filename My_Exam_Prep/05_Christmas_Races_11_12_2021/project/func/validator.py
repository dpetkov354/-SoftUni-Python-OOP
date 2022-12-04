class Validator:
    @staticmethod
    def input_lenght_check(value):
        if len(value) > 3:
            return True
        raise ValueError(f"Model {value} is less than 4 symbols!")

    @staticmethod
    def speed_limit_check(model, value):
        max_speed = 0
        min_speed = 0
        if model == "MuscleCar":
            max_speed = 450
            min_speed = 250
        elif model == "SportsCar":
            max_speed = 600
            min_speed = 400

        if max_speed >= value >= min_speed:
            return True
        raise ValueError(f"Invalid speed limit! Must be between {min_speed} and {max_speed}!")

    @staticmethod
    def empty_string(value):
        if value.strip() != "":
            return True
        raise ValueError("Name should contain at least one character!")

    @staticmethod
    def car_model_in_list_check(data_models, car_model):
        if any(x.model == car_model for x in data_models):
            raise Exception(f"Car {car_model} is already created!")

    @staticmethod
    def driver_name_in_list_check(data_drivers, driver_name):
        if any(x.name == driver_name for x in data_drivers):
            raise Exception(f"Driver {driver_name} is already created!")

    @staticmethod
    def race_name_in_list_check(data_races, race_name):
        if any(x.name == race_name for x in data_races):
            raise Exception(f"Race {race_name} is already created!")




