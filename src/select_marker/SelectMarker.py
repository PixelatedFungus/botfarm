import pygame, os

class SelectMarker():

    select_marker_folder = os.path.join("sprites", "select_marker")

    def __init__(self) -> None:
        self.select_marker_surface = pygame.image.load(os.path.join(self.select_marker_folder, "select_marker.png"))
        pass