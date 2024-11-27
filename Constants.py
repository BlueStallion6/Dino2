import pygame
import json
import requests
pygame.init()

try:
    open("config.json")
except FileNotFoundError:
    print("Config file not found.")
    print("Downloading config file from 'https://raw.githubusercontent.com/BlueStallion6/SuperPong/main/config.json'...")
    url = "https://raw.githubusercontent.com/BlueStallion6/SuperPong/main/config.json"
    config_file = requests.get(url)
    open("config.json", "wb").write(config_file.content)
    print("'config.json' has been created")

with open("config.json", "r") as file:
    CONFIG = json.load(file)
    file.close()


DEBUG_MODE = CONFIG["settings"]["debug_mode"]
TPS = CONFIG["settings"]["tps"]