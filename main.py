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
    #from Constants import *

except ImportError:
    print("ImportError >> Please run 'pip install -r requirements.txt' in this project's directory.")
    exit()



running = True
i = 0


while running and i < 1000000:
    i = i + 1
    print(i)

