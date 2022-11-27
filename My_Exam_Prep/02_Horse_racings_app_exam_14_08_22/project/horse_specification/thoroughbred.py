from project.horse_specification.horse import Horse

TRAINING_INCREASE = 3


class Thoroughbred(Horse):
    def __init__(self, name: str, speed: int):
        self.breed = 'Thoroughbred'
        super().__init__(name, speed)

    def train(self):
        if self.speed > 137:
            self.speed = 137
        self.speed += TRAINING_INCREASE
        return self.speed
