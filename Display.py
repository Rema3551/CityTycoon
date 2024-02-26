import pygame
from Button import *
import Game

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


    def flip(self):
        pygame.display.flip()

    def draw(self, game:Game):
        """
        affichage du jeu
        """
        pass