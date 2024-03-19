from Building import * 
from Affichage import *

class Game:
    def __init__(self):
        self.poubelle1 = Building(20,0.0004)
        self.poubelle2 = Building(30,10)
        self.bidonville = [self.poubelle1, self.poubelle2]
        
        self.affichage = Affichage()
        #self.player = Player()

    def printGame(self):
        self.affichage.player.sauvegardeLocation()
        self.affichage.inputJoueur()
        self.affichage.update()
        self.affichage.draw(self)
        self.affichage.flip()
        
        
        