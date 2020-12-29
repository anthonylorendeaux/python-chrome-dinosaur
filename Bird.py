import random

from Obstacles import Obstacles

class Bird(Obstacles):
    def __init__(self, image, SCREEN_WIDTH):
        self.type = 0
        super().__init__(image, self.type, SCREEN_WIDTH)
        self.rect.y = 250
        self.index = 0
    
    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1
