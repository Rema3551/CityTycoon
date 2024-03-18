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
        self.affichage.player.sauvegardeLocation()
        self.affichage.inputJoueur()
        self.affichage.update()
        self.affichage.draw(self)
        self.affichage.flip()
        
        
        