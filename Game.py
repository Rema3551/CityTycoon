from Building import *
from Affichage import *
from BuildingType import *
from Backup import *
from GameStep import *
from MapStep import *
from random import *

class Game:
    def __init__(self):
        self.player = Player()
        self.backup = Backup()
        self.gameEnum = GameStep.IDLE
        self.mapStep = MapStep.MAP1
        self.affichage = Affichage(self)
        
    def getGameStep(self):
        return self.gameEnum
    
    def setGameStep(self, newGameStep):
        self.gameEnum = newGameStep
        
    def getMapStep(self):
        return self.mapStep
    
    def setMapStep(self, newMapStep):
        self.mapStep = newMapStep

    def start(self, tmx_data):
        self.createPlayer(tmx_data)
        self.createBuildings(tmx_data)
        self.backup.load(self)
        self.createBuildingsCollideArea(tmx_data)
        
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
        self.rouge = Building(100,10,3,"rouge", BuildingType.ROUGE)
        self.help = Building(750,30,3,"help",BuildingType.HELP)
        self.orange = Building(500,25,3,"orange",BuildingType.ORANGE)
        
        self.hdv = Building(100000,200,2,"hdv",BuildingType.HDV)
        self.maisonette = Building(1000,40,3,"maisonette",BuildingType.MAISONETTE)
        self.maison = Building(5000,45,3,"maison",BuildingType.MAISON)
        self.tourDeGuet = Building(20000,65,3,"tourDeGuet",BuildingType.TOURDEGUET)
        self.cabane = Building(17500,55,3,"cabane",BuildingType.CABANE)
        self.ecurie = Building(15000,45,3,"ecurie",BuildingType.ECURIE)
        self.terrainDentrainement = Building(15000,45,3,"terrainDentrainement",BuildingType.TERRAINDENTRAINEMENT)
        self.forge = Building(15000,45,3,"forge",BuildingType.FORGE)

        self.listBuildingVille1 = [self.poubelle1, self.poubelle2, self.poubelle3, self.poubelle4, self.poubelle5, self.poubelle6, self.poubelle7, self.poubelle8, self.poubelle9, self.poubelle10, self.rouge, self.help, self.orange]
        self.listBuildingVille2 = [self.hdv, self.maisonette, self.maison, self.tourDeGuet,self.cabane,self.ecurie,self.terrainDentrainement,self.forge]
        
        #self.buildings = [self.poubelle1, self.poubelle2, self.poubelle3, self.poubelle4, self.poubelle5, self.poubelle6, self.poubelle7, self.poubelle8, self.poubelle9, self.poubelle10, self.rouge, self.help, self.orange,self.hdv, self.maisonette, self.maison, self.tourDeGuet,self.cabane,self.ecurie]
        #Faire une liste pour moyen de deplacement changement de ville

    def createBuildingsCollideArea(self,tmx_data):
        if self.mapStep == MapStep.MAP1:
            for building1 in self.listBuildingVille1:
                tmxObject1 = tmx_data.get_object_by_name(building1.getLibelle())
                building1.setCollideArea(tmxObject1.x, tmxObject1.y, tmxObject1.width, tmxObject1.height)
        if self.mapStep == MapStep.MAP2:
            for building2 in self.listBuildingVille2:
                tmxObject2 = tmx_data.get_object_by_name(building2.getLibelle())
                building2.setCollideArea(tmxObject2.x, tmxObject2.y, tmxObject2.width, tmxObject2.height)

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
        self.backup.save(self)
        

    def verificationFinVille1(self):
        if self.player.listBuilding == self.listBuildingVille1 :
            for building in self.player.listBuilding:
                if building.getLvl() != building.getLvlMax():
                    return False
            return True
        else: 
            return False
    
    def verificationFinVille2(self):
        if self.player.listBuilding == self.listBuildingVille2 :
            for building in self.player.listBuilding:
                if building.getLvl() != building.getLvlMax():
                    return False
            return True
        else: 
            return False

    def restoreMap(self, savedMap):
        self.mapStep = savedMap

    def restoreMapData(self,restored_data):
        self.restoreMap(restored_data['map'])

    def restoreBuildings(self, savedBuildings):
        for building in savedBuildings:
            for i in range (len(self.listBuildingVille1)):
                if building.libelle == self.listBuildingVille1[i].libelle:
                    self.listBuildingVille1[i] = building
            for i in range (len(self.listBuildingVille2)):
                if building.libelle == self.listBuildingVille2[i].libelle:
                    self.listBuildingVille2[i] = building
        self.player.setListBuilding(savedBuildings)

    def restorePlayer(self,savedPlayer):
        self.player.setDollars(savedPlayer['dollars'])
        self.player.setDiamonds(savedPlayer['diamonds'])
        self.player.setPosition(
            savedPlayer['position_x'],
            savedPlayer['position_y']
        )


    def restoreData(self, restored_data):
        self.restoreMap(restored_data['map'])
        self.restoreBuildings(restored_data['listBuildingsPlayer'])
        self.restorePlayer(restored_data['player'])

    """
    def randomAd(self, adList : list):
        ad = random.choice(adList)
        return ad
    """ 


        
