from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    DEFAULT_PORTION = 250

    def __init__(self, name: str, price: float, portion=DEFAULT_PORTION):
        super().__init__(name, portion, price)
        self.type = 'Stolen'

    def details(self, ):
        return f"{self.type} {self.name}: {self.portion}g - {self.price:0.2f}lv."