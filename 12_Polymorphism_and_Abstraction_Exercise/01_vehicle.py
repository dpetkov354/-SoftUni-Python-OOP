from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    CONSUMPTION_INCREASE_IN_SUMMER = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        if (self.fuel_consumption + Car.CONSUMPTION_INCREASE_IN_SUMMER) * distance <= self.fuel_quantity:
            self.fuel_quantity -= (self.fuel_consumption + Car.CONSUMPTION_INCREASE_IN_SUMMER) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONSUMPTION_INCRESE_IN_SUMMER = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        if (self.fuel_consumption + Truck.CONSUMPTION_INCRESE_IN_SUMMER) * distance <= self.fuel_quantity:
            self.fuel_quantity -= (self.fuel_consumption + Truck.CONSUMPTION_INCRESE_IN_SUMMER) * distance

    def refuel(self, fuel):
        self.fuel_quantity += (0.95 * fuel)


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
