########################## MAIN FILE #################################

try:
    import os
    import time
    import pygame
    import colored
    import sys
    import screeninfo
    import json
    #import resources.pygameResources as assets
    import threading
    import random
    from screeninfo import get_monitors
    #from resources.pygameResources import sfx
    from Colors import *
    from Constants import *

except ImportError:
    print("ImportError >> Please run 'pip install -r requirements.txt' in this project's directory.")
    exit()

#######################################################################################################################

                                                       ###################### WINDOW INIT #########################
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Dino2')

MONITORS = get_monitors()
primary_monitor = MONITORS[0]

W_WIDTH = primary_monitor.width # * W_PERC
W_HEIGHT = primary_monitor.height # * W_PERC
FLAGS = pygame.HWSURFACE | pygame.DOUBLEBUF

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

clock = pygame.time.Clock()
#screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT), FLAGS)
#screen = pygame.display.set_mode((W_WIDTH // 2.0, W_HEIGHT // 2.8))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]

JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))

DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]


LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))



class Dinosaur:
    X_POS = 80
    Y_POS = 310

    def __init__(self):
        self.run_img = RUNNING
        self.duck_img = DUCKING
        self.jump_img = JUMPING

        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 100:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        pass

    def run(self):
        self.image = self.run_img[self.step_index // 50]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        pass

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))








class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))









                                                          ################### RUNNING TRUE #####################
running = True
player = Dinosaur()
cloud = Cloud()
game_begun = False
game_speed = 3

while running:
    screen.fill(Colors.ALMOST_WHITE)
    userInput = pygame.key.get_pressed()

    if game_begun is True or game_begun is not True:
        pygame.draw.line(screen, Colors.GRAY, (0, W_HEIGHT // 3.70), (W_WIDTH, W_HEIGHT // 3.70), 2)

    player.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Closing the game...")
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Closing the game...")
                pygame.quit()
                exit()

    if userInput[pygame.K_1] or (game_begun is True):
        player.update(userInput)

        cloud.draw(screen)
        cloud.update()

        game_begun = True






    pygame.display.update()
    clock.tick(TPS)

