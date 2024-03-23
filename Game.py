from Building import * 
from Affichage import *
from BuildingType import *
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
        # TODO : lvl max building
        self.poubelle1 = Building(5,1,1,"poubelle1",BuildingType.POUBELLE)
        self.poubelle2 = Building(15,1,1,"poubelle2",BuildingType.POUBELLE)
        self.poubelle3 = Building(20,1,1,"poubelle3",BuildingType.POUBELLE)
        self.poubelle4 = Building(25,1,1,"poubelle4",BuildingType.POUBELLE)
        self.poubelle5 = Building(30,1,1,"poubelle5",BuildingType.POUBELLE)
        self.poubelle6 = Building(35,1,1,"poubelle6",BuildingType.POUBELLE)
        self.poubelle7 = Building(40,1,1,"poubelle7",BuildingType.POUBELLE)
        self.poubelle8 = Building(45,1,1,"poubelle8",BuildingType.POUBELLE)
        self.poubelle9 = Building(50,1,1,"poubelle9",BuildingType.POUBELLE)
        self.poubelle10 = Building(55,1,1, "poubelle10",BuildingType.POUBELLE)
        self.rouge = Building(100,10,1,"rouge", BuildingType.ROUGE)
        self.help = Building(1000,50,1,"help",BuildingType.HELP)
        self.orange = Building(500,25,1,"orange",BuildingType.ORANGE)
        self.buildings = [self.poubelle1, self.poubelle2, self.poubelle3, self.poubelle4, self.poubelle5, self.poubelle6, self.poubelle7, self.poubelle8, self.poubelle9, self.poubelle10, self.rouge, self.help, self.orange]
        
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
