import pygame
import pytmx
import pyscroll
from Button import *
import Game
from Player import *

class Affichage:
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
        icon = pygame.image.load('assets/pdp.png')
        pygame.display.set_icon(icon)
        self.screen = pygame.display.set_mode((800,800))
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)

        tmx_data = pytmx.util_pygame.load_pygame('assets/map/testMap.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)
        
        
        self.dollars = pygame.image.load("assets/Images/dollars.png").convert_alpha()

    def flip(self):
        pygame.display.flip()
        self.group.update()
        

    def draw(self, game:Game):
        """
        affichage du jeu
        """
        self.group.draw(self.screen)
        self.screen.blit(self.dollars,(0,0))
        
        
        #textDollars = pygame.font.SysFont('comicsansms', 12).render(str(game.player.getDollars()), True, self.green)