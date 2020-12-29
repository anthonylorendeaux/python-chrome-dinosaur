import random

from Obstacles import Obstacles

class SmallCactus(Obstacles):
    def __init__(self, image, SCREEN_WIDTH):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type, SCREEN_WIDTH)
        self.rect.y = 325