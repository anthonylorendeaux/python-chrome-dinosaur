import pygame
import os
import random

from Dinosaur import Dinosaur
from Cloud import Cloud
from SmallCactus import SmallCactus
from LargeCactus import LargeCactus
from Bird import Bird

pygame.init()
pygame.display.set_caption("Chrome Dinosaur") 

# Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#TODO - To Remove
SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

#* Main function
def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    game_speed = 14

    # BG Constants
    x_pos_bg = 0
    y_pos_bg = 380

    # Score and Font
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)

    # Instanciate Classes
    cloud = Cloud(SCREEN_WIDTH)
    player = Dinosaur()
    obstacles = []

    # Score
    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    # Background
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    # Game Loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        # Draw and Update the Dino
        player.draw(SCREEN)
        player.update(userInput)

        # Obstacles
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS, SCREEN_WIDTH))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS, SCREEN_WIDTH))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD, SCREEN_WIDTH))
        
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(game_speed, obstacles) 
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.draw.rect(SCREEN, (255, 0, 0), player.dino_rect, 2)

        # Background
        background()

        # Draw and Update Cloud
        cloud.draw(SCREEN)
        cloud.update(SCREEN_WIDTH, game_speed)

        # Score display
        score()

        clock.tick(30)
        pygame.display.update()
main()