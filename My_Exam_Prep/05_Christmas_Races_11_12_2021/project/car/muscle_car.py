from project.car.car import Car

class MuscleCar(Car):
    def __init__(self,model: str, speed_limit: int, is_taken=False):
        self.type = "MuscleCar"
        super().__init__(model, speed_limit, is_taken)
