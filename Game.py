import pygame
from Building import * 
from Display import *
from Player import * 

class Game:
    def __init__(self):
        self.bidonville1 = Building(0,10)
        self.bidonville2 = Building(30,10)
        self.bidonville = [self.bidonville1, self.bidonville2]
        
        self.display = Display()
        self.player = Player()

    def print(self):
        self.display.draw()
        self.display.flip()