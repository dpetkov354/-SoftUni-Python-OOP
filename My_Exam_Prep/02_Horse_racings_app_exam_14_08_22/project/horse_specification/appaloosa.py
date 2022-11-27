from project.horse_specification.horse import Horse

TRAINING_INCREASE = 2


class Appaloosa(Horse):
    def __init__(self, name: str, speed: int):
        self.breed = 'Appaloosa'
        super().__init__(name, speed)

    def train(self):
        if self.speed > 118:
            self.speed = 118
        self.speed += TRAINING_INCREASE
        return self.speed
