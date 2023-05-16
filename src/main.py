import pygame, sys, os
# sys.path.append('..')
from bots.DarkBot import DarkBot
from bots.LightBot import LightBot

class GameState():
    def __init__(self) -> None:
        self.bot_dark
        self.bot_light
        self.light_plants
        self.dark_plants
        self.neutral_plants
        self.light_squares
        self.dark_squares
        self.neutral_squares

print(sys.path)

pygame.init()

DISPLAYSIZE = (768, 512)
DISPLAYSURF = pygame.display.set_mode(DISPLAYSIZE)
pygame.display.set_caption("BotFarm")

SIZE = (192, 128)
SURF = pygame.Surface(SIZE)

neutral_soil = pygame.image.load(os.path.join("sprites", "neutral_soil", "neutral_soil.png"))
light_soil = pygame.image.load(os.path.join("sprites", "light_soil", "light_soil1.png"))
dark_soil = pygame.image.load(os.path.join("sprites", "dark_soil", "dark_soil1.png"))

neutral_plant = pygame.image.load(os.path.join("sprites", "plants", "plant1.png"))
light_plant = pygame.image.load(os.path.join("sprites", "plants", "plant2.png"))
dark_plant = pygame.image.load(os.path.join("sprites", "plants", "plant3.png"))

bot_dark = pygame.image.load(os.path.join("sprites", "bot_dark", "bot_dark1.png"))
bot_light = pygame.image.load(os.path.join("sprites", "bot_light", "bot_light1.png"))

select_marker = pygame.image.load(os.path.join("sprites", "select_marker", "select_marker.png"))

darkBotTest = DarkBot()
lightBotTest = LightBot()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for column in range(SIZE[0] // 16):
        for row in range(SIZE[1] // 16):
            SURF.blit(neutral_soil, (column * 16, row * 16))
    
    for column in range(8, SIZE[0] // 16):
        for row in range(SIZE[1] // 16):
            SURF.blit(dark_soil, (column * 16, row * 16))

    for column in range(4):
        for row in range(SIZE[1] // 16):
            SURF.blit(light_soil, (column * 16, row * 16))

    SURF.blit(neutral_plant, (4 * 16, 0 * 16))
    SURF.blit(light_plant, (0, 0))
    SURF.blit(dark_plant, (8 * 16, 0 * 16))

    SURF.blit(bot_dark, (8 * 16, 2 * 16))
    SURF.blit(bot_light, (0, 2 * 16))

    SURF.blit(select_marker, (0, 0))

    pygame.transform.scale(SURF, DISPLAYSIZE, DISPLAYSURF)
    pygame.display.update()