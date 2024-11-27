from screeninfo import get_monitors

try:
    import os
    import time
    import pygame
    import colored
    import sys
    import screeninfo
    #import json
    #import resources.pygameResources as assets
    #import threading
    #from random import *
    #from screeninfo import get_monitors
    #from resources.pygameResources import sfx
    #from keywords import *
    from Constants import *

except ImportError:
    print("ImportError >> Please run 'pip install -r requirements.txt' in this project's directory.")
    exit()


                                                          ##### WINDOW INIT ######
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Dino2')

MONITORS = get_monitors()
primary_monitor = MONITORS[0]

W_WIDTH = primary_monitor.width
W_HEIGHT = primary_monitor.height
FLAGS = pygame.HWSURFACE | pygame.DOUBLEBUF

clock = pygame.time.Clock()
screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT), FLAGS)


                                                          ##### RUNNING TRUE #####
running = True
while running:

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

    pygame.display.update()
    clock.tick(TPS)
    print(TPS)