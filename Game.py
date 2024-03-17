from Building import * 
from Player import *
from Affichage import *

class Game:
    def __init__(self):
        self.bidonville1 = Building(0,10)
        self.bidonville2 = Building(30,10)
        self.bidonville = [self.bidonville1, self.bidonville2]
        
        self.affichage = Affichage()
        #self.player = Player()

    def printGame(self):
        self.inputGame()
        self.affichage.draw(self)
        self.affichage.flip()
        
    def inputGame(self):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]:
            print("haut")
        elif pressed[pygame.K_DOWN]:
            print("bad")
        elif pressed[pygame.K_LEFT]:
            print("gauche")
        elif pressed[pygame.K_RIGHT]:
            print("droite")
        
        
        