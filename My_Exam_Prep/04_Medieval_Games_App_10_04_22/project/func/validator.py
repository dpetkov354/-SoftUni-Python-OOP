class Validator:
    @staticmethod
    def empty_string(value):
        if value.strip() != "":
            return True

        raise ValueError("Name cannot be an empty string.")

    @staticmethod
    def less_than_zero(value):
        if value >= 0:
            return True

        raise ValueError("Energy cannot be less than zero.")

    @staticmethod
    def empty_name(value):
        if value.strip() != "":
            return True

        raise ValueError("Name not valid!")

    @staticmethod
    def check_age(num):
        if num > 11:
            return True

        raise ValueError("The player cannot be under 12 years old!")

    @staticmethod
    def check_stamina(num):
        if 100 >= num >= 0:
            return True

        raise ValueError("Stamina not valid!")
