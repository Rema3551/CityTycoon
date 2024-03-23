from Building import * 
from Affichage import *

class Game:
    def __init__(self):
        self.player = Player()
        self.affichage = Affichage(self)

    
    def start(self, tmx_data):
        self.createPlayer(tmx_data)
        self.createBuildings(tmx_data)
        
    def createPlayer(self, tmx_data):
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

    def createBuildings(self, tmx_data):
        self.poubelle1 = Building(5,0.004, "poubelle1")
        self.poubelle2 = Building(50,0.004, "poubelle2")
        self.poubelle3 = Building(100,0.004, "poubelle3")
        self.poubelle4 = Building(150,0.004, "poubelle4")
        self.poubelle5 = Building(200,0.004, "poubelle5")
        self.poubelle6 = Building(250,0.004, "poubelle6")
        self.poubelle7 = Building(300,0.004, "poubelle7")
        self.poubelle8 = Building(350,0.004, "poubelle8")
        self.poubelle9 = Building(400,0.004, "poubelle9")
        self.poubelle10 = Building(450,0.004, "poubelle10")
        self.Help = Building(600,0.001, "help")
        self.Orange = Building(1000,0.002, "orange")
        self.buildings = [self.poubelle1, self.poubelle2, self.poubelle3, self.poubelle4, self.poubelle5, self.poubelle6, self.poubelle7, self.poubelle8, self.poubelle9, self.poubelle10, self.rouge, self.Help, self.Orange]
        
        for building in self.buildings:
            tmxObject = tmx_data.get_object_by_name(building.libelle)
            building.setCollideArea(tmxObject.x, tmxObject.y, tmxObject.width, tmxObject.height)

    def onInputJoueur(self):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_UP]:
            self.player.bougerHaut()
            self.player.animation('up')
            self.player.setDollars(self.player.getDollars()+0.01)
            self.player.setDiamonds(self.player.getDiamonds()+0.0001)
        elif pressedKeys[pygame.K_DOWN]:
            self.player.bougerBas()
            self.player.animation('down')
            self.player.setDollars(self.player.getDollars()+0.01)
            self.player.setDiamonds(self.player.getDiamonds()+0.0001)
        elif pressedKeys[pygame.K_LEFT]:
            self.player.bougerGauche()
            self.player.animation('left')
            self.player.setDollars(self.player.getDollars()+0.01)
            self.player.setDiamonds(self.player.getDiamonds()+0.0001)
        elif pressedKeys[pygame.K_RIGHT]:
            self.player.bougerDroite()
            self.player.animation('right')
            self.player.setDollars(self.player.getDollars()+0.01)
            self.player.setDiamonds(self.player.getDiamonds()+0.0001)


    def printGame(self):
        self.player.sauvegardeLocation()
        self.onInputJoueur()
        self.affichage.update(self.player)
        self.affichage.draw(self)
        self.affichage.flip()
