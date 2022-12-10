class Validation:
    @staticmethod
    def empty_string(value):
        if value.strip() != "":
            return True

        raise ValueError("Name cannot be null or whitespace!")

    @staticmethod
    def check_positive_number(num):
        if num > 0.0:
            return True

        raise ValueError("Price cannot be less or equal to zero!")

    @staticmethod
    def check_positive_capacity(num):
        if num >= 0:
            return True

        raise ValueError("Capacity cannot be a negative number!")

    @staticmethod
    def delicacy_food_duplicate(name: str, delicacy_list: list):
        if any(name == f.name for f in delicacy_list):
            raise Exception(f"{name} already exists!")

    @staticmethod
    def booth_number_duplicate(booth_number: int, booth_list: list):
        if any(booth_number == f.booth_number for f in booth_list):
            raise Exception(f"Booth number {booth_number} already exists!")
