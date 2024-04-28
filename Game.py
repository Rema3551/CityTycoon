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

        if self.getMapStep()==MapStep.MAP3:

            self.player.sprite_sheet = pygame.image.load('assets/Images/playerMap3.png')
            self.player.image = self.player.get_imageMap3(0,0)
            self.player.image.set_colorkey([0,0,0]) #fait en sorte que ça soit transparent
            self.player.rect = self.player.image.get_rect()
            self.player.images = {
                'down': self.player.get_imageMap3(0,0),
                'left': self.player.get_imageMap3(1,49),
                'right': self.player.get_imageMap3(1,96),
                'up': self.player.get_imageMap3(0,145)
            }

    def createBuildings(self, tmx_data):
        # TODO : lvl max building
        #Map1 Buildings
        self.flowers_map1 = Building(30,20,4,4,9,"flowers_map1",BuildingType.FLOWERS_MAP1)
        self.campfire_map1 = Building(25,25,3,3,1,"campfire_map1",BuildingType.CAMPFIRE_MAP1)
        self.roc_map1 = Building(5,5,1,1,6,"roc_map1",BuildingType.ROC_MAP1)
        self.house1_map1 = Building(100,50,8,6,2,"house1_map1",BuildingType.HOUSE1_MAP1)
        self.house2_map1 = Building(400,200,10,8,3,"house2_map1",BuildingType.HOUSE2_MAP1)
        self.house3_map1 = Building(1000,500,14,10,3,"house3_map1",BuildingType.HOUSE3_MAP1)
        self.house4_map1 = Building(2500,1000,16,12,3,"house4_map1",BuildingType.HOUSE4_MAP1)
        """
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
        """
        #Map2 Buildings
        self.hdv = Building(100000,40000,500,100,5,"hdv",BuildingType.HDV)
        self.maisonette = Building(10000,2500,25,15,1,"maisonette",BuildingType.MAISONETTE)
        self.maison = Building(35000,2500,30,16,3,"maison",BuildingType.MAISON)
        self.tourDeGuet = Building(75000,30000,150,50,3,"tourDeGuet",BuildingType.TOURDEGUET)
        self.cabane = Building(25000,6500,55,20,2,"cabane",BuildingType.CABANE)
        self.ecurie = Building(15000,5000,45,18,2,"ecurie",BuildingType.ECURIE)
        self.terrainDentrainement = Building(50000,50000,46,46,1,"terrainDentrainement",BuildingType.TERRAINDENTRAINEMENT)
        self.forge = Building(40000,6500,55,20,2,"forge",BuildingType.FORGE)
        #Map3 Buildings
        self.house1 = Building(1500000,50000,550,300,1,"house1",BuildingType.HOUSE1)
        self.house2 = Building(2500000,60000,750,500,2,"house2",BuildingType.HOUSE2)
        self.house3 = Building(3000000,75000,1000,750,3,"house3",BuildingType.HOUSE3)

        #Listes des buildings en fonction des villes
        self.listBuildingVille1 = [self.flowers_map1, self.campfire_map1,self.roc_map1, self.house1_map1, self.house2_map1, self.house3_map1, self.house4_map1]
        self.listBuildingVille2 = [self.hdv, self.maisonette, self.maison, self.tourDeGuet,self.cabane,self.ecurie,self.terrainDentrainement,self.forge]
        self.listBuildingVille3 = [self.house1,self.house2,self.house3]
        #self.listBuildingVille1 = [self.poubelle1, self.poubelle2, self.poubelle3, self.poubelle4, self.poubelle5, self.poubelle6, self.poubelle7, self.poubelle8, self.poubelle9, self.poubelle10, self.rouge, self.help, self.orange]
        #self.buildings = [self.poubelle1, self.poubelle2, self.poubelle3, self.poubelle4, self.poubelle5, self.poubelle6, self.poubelle7, self.poubelle8, self.poubelle9, self.poubelle10, self.rouge, self.help, self.orange,self.hdv, self.maisonette, self.maison, self.tourDeGuet,self.cabane,self.ecurie]

    def createBuildingsCollideArea(self,tmx_data):
        if self.mapStep == MapStep.MAP1:
            for building1 in self.listBuildingVille1:
                tmxObject1 = tmx_data.get_object_by_name(building1.getLibelle())
                if tmxObject1 == "house1_map1" or tmxObject1 == "house2_map1" or tmxObject1 == "house3_map1" or tmxObject1 == "house4_map1":
                    building1.setCollideArea(tmxObject1.x, tmxObject1.y, tmxObject1.width, tmxObject1.height + 150)
                else:
                    building1.setCollideArea(tmxObject1.x, tmxObject1.y, tmxObject1.width, tmxObject1.height)
        if self.mapStep == MapStep.MAP2:
            for building2 in self.listBuildingVille2:
                tmxObject2 = tmx_data.get_object_by_name(building2.getLibelle())
                building2.setCollideArea(tmxObject2.x, tmxObject2.y, tmxObject2.width, tmxObject2.height)
        if self.mapStep == MapStep.MAP3:
            for building3 in self.listBuildingVille3:
                tmxObject3 = tmx_data.get_object_by_name(building3.getLibelle())
                building3.setCollideArea(tmxObject3.x, tmxObject3.y, tmxObject3.width, tmxObject3.height)

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



        
