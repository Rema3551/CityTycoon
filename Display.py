import pygame
from Button import *
from Game import *

class Display:
    """
    Attributs:
        -map
    Méthodes:
        -draw
        -flip
    """
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("City Tycoon")
        self.screen = pygame.display.set_mode((1920,1080))

        tmx_data = pytmx.util_pygame.load_pygame('assets/map/testMap.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

        
        


    def flip(self):
        pygame.display.flip()

    def draw(self):
        """
        affichage du jeu
        """
        self.group.draw(self.screen)
        