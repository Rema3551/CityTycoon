from Building import * 
from Affichage import *

class Game:
    def __init__(self):
        self.poubelle1 = Building(20,0.0004)
        self.poubelle2 = Building(50,0.0004)
        self.poubelle3 = Building(100,0.0004)
        self.poubelle4 = Building(150,0.0004)
        self.poubelle5 = Building(200,0.0004)
        self.poubelle6 = Building(250,0.0004)
        self.poubelle7 = Building(300,0.0004)
        self.poubelle8 = Building(350,0.0004)
        self.poubelle9 = Building(400,0.0004)
        self.poubelle10 = Building(450,0.0004)
        self.Help = Building(600,0.001)
        self.Orange = Building(1000,0.002)
        self.bidonville = [self.poubelle1, self.poubelle2, self.poubelle3, self.poubelle4, self.poubelle5, self.poubelle6, self.poubelle7, self.poubelle8, self.poubelle9, self.poubelle10, self.Help, self.Orange]
        
        self.affichage = Affichage()
        #self.player = Player()

    def printGame(self):
        self.affichage.player.sauvegardeLocation()
        self.affichage.inputJoueur()
        self.affichage.update()
        self.affichage.draw(self)
        self.affichage.flip()
        
        
        