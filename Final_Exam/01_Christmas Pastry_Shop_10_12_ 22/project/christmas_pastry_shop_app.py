from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.func.validation import Validation


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    @property
    def __delicacy_types(self):
        return {"Gingerbread": Gingerbread,
                "Stolen": Stolen}

    @property
    def __booth_types(self):
        return {"Open Booth": OpenBooth,
                "Private Booth": PrivateBooth}

    def __find_booth(self, booth_number: int):
        for b in self.booths:
            if b.booth_number == booth_number:
                return b

    def __find_delicacy(self, delicacy_name: str):
        for d in self.delicacies:
            if d.name == delicacy_name:
                return d

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        Validation.delicacy_food_duplicate(name, self.delicacies)
        if type_delicacy not in self.__delicacy_types:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = self.__delicacy_types[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        Validation.booth_number_duplicate(booth_number, self.booths)
        if type_booth not in self.__booth_types:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = self.__booth_types[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        find_booth = [t for t in self.booths if not t.is_reserved and t.capacity >= number_of_people]
        if find_booth:
            find_booth = find_booth[0]
            find_booth.reserve(number_of_people)
            return f"Booth {find_booth.booth_number} has been reserved for {number_of_people} people."
        else:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth(booth_number)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.__find_delicacy(delicacy_name)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        bill = 0
        booth = self.__find_booth(booth_number)
        bill += booth.price_for_reservation
        for ordered_delicacies in booth.delicacy_orders:
            bill += ordered_delicacies.price

        self.income += bill

        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {bill:0.2f}lv."

    def get_income(self):
        return f"Income: {self.income:0.2f}lv."
