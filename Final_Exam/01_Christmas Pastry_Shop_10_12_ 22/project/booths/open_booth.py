from project.booths.booth import Booth

DEFAULT_PRICE_PER_PERSON = 2.5

class OpenBooth(Booth):


    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)
        self.number_of_people = 0
        self.price_for_reservation = 0
        self.type = 'OpenBooth'

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.price_for_reservation = number_of_people * DEFAULT_PRICE_PER_PERSON
        self.is_reserved = True

