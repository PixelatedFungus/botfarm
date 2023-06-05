import pygame, sys, os
from bots.DarkBot import DarkBot
from bots.LightBot import LightBot

class GameState():



    def __init__(self) -> None:
        self.bot_dark = None
        self.bot_light = None
        self.load_sprites()

    def load_sprites(self) -> None:
        # Loading in the sprites
        # Soil sprites
        self.neutral_soil = pygame.image.load(os.path.join("sprites", "neutral_soil", "neutral_soil.png"))
        self.light_soil = pygame.image.load(os.path.join("sprites", "light_soil", "light_soil1.png"))
        self.dark_soil = pygame.image.load(os.path.join("sprites", "dark_soil", "dark_soil1.png"))

        # Plant sprites
        self.neutral_plant = pygame.image.load(os.path.join("sprites", "plants", "plant1.png"))
        self.light_plant = pygame.image.load(os.path.join("sprites", "plants", "plant2.png"))
        self.dark_plant = pygame.image.load(os.path.join("sprites", "plants", "plant3.png"))

        # Bot sprites
        self.bot_dark = pygame.image.load(os.path.join("sprites", "bot_dark", "bot_dark1.png"))
        self.bot_light = pygame.image.load(os.path.join("sprites", "bot_light", "bot_light1.png"))

        # Marker sprite
        self.select_marker = pygame.image.load(os.path.join("sprites", "select_marker", "select_marker.png"))

    def main(self) -> None:
        pygame.init()

        DISPLAYSIZE = (1536, 1024)
        DISPLAYSURF = pygame.display.set_mode(DISPLAYSIZE)
        pygame.display.set_caption("BotFarm")

        # If scale is 1, each sprite is 8x8. If scale is 2, each sprite is 16x16. etc.
        # sprite dimension = (2 ^ (scale + 2)) x (2 ^ (scale + 2))
        scale = 8
        SIZE = [coord // scale for coord in DISPLAYSIZE]
        SURF = pygame.Surface(SIZE)

        darkBotTest = DarkBot()
        lightBotTest = LightBot()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for column in range(SIZE[0] // 16):
                for row in range(SIZE[1] // 16):
                    SURF.blit(self.neutral_soil, (column * 16, row * 16))
            
            for column in range(8, SIZE[0] // 16):
                for row in range(SIZE[1] // 16):
                    SURF.blit(self.dark_soil, (column * 16, row * 16))

            for column in range(4):
                for row in range(SIZE[1] // 16):
                    SURF.blit(self.light_soil, (column * 16, row * 16))

            SURF.blit(self.neutral_plant, (4 * 16, 0 * 16))
            SURF.blit(self.light_plant, (0, 0))
            SURF.blit(self.dark_plant, (8 * 16, 0 * 16))

            SURF.blit(self.bot_dark, (8 * 16, 2 * 16))
            SURF.blit(self.bot_light, (0, 2 * 16))

            SURF.blit(self.select_marker, (8 * 16, 2 * 16))

            pygame.transform.scale(SURF, DISPLAYSIZE, DISPLAYSURF)
            pygame.display.update()

game = GameState()
game.main()