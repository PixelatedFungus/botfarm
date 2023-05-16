import pygame, os
from bots.Bot import Bot
from util import Util

class LightBot(Bot):

    light_bot_folder = os.path.join("sprites", "bot_light")

    def __init__(self) -> None:
        self.frames = Util.load_frames(self.light_bot_folder, "bot_light", "png", 1, 4)