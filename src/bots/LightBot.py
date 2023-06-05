import pygame, os
from bots.Bot import Bot

class LightBot(Bot):

    light_bot_folder = os.path.join("sprites", "bot_light")

    def __init__(self) -> None:
        pass