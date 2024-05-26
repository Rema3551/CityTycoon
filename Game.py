from Building import *
from Affichage import *
from BuildingType import *
from Backup import *
from GameStep import *
from MapStep import *
from random import *
from Ad import *

class Game:
    """
    Attributs :
        -player
        -backup
        -gameEnum
        -mapStep
        -affichage
    Méthodes :
        -mutateurs  (set...())
        -accesseurs (get...())
        -start(self,tmx_data)
        -createPlayer(self, tmx_data)
        -createBuildings(self, tmx_data)
        -createBuildingsCollideArea(self,tmx_data)
        -onInputJoueur(self)
        -printGame(self)
        -restoreMap(self, savedMap)
        -restoreMapData(self,restored_data)
        -restoreBuildings(self, savedBuildings)
        -restorePlayer(self,savedPlayer)
        -restoreData(self, restored_data)
    """
    def __init__(self):
        self.player = Player()
        self.backup = Backup()
        self.ad = Ad()
        self.gameEnum = GameStep.IDLE
        self.mapStep = MapStep.MAP1
        self.affichage = Affichage(self)
        
    def getGameStep(self):
        """renvoie l'étape du jeu"""
        return self.gameEnum
    
    def setGameStep(self, newGameStep):
        """change l'étape du jeu"""
        self.gameEnum = newGameStep
        
    def getMapStep(self):
        """renvoie l'étape des maps (quelle map)"""
        return self.mapStep
    
    def setMapStep(self, newMapStep):
        """change l'étape des maps (quelle map)"""
        self.mapStep = newMapStep

    def start(self, tmx_data):
        """fonction pour initialiser le jeu"""
        self.createPlayer(tmx_data)
        self.createBuildings(tmx_data)
        self.backup.load(self)
        self.createBuildingsCollideArea(tmx_data)
        
    def createPlayer(self, tmx_data):
        """fonction de création du joueur"""
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
        """fonction de création des buildings (il faut les recréer à chaque lancement du jeu)"""
        # TODO : lvl max building
                         #Exemple : Building(price,nextPrice,gain,nexGain,lvlMax,name,type)
        #Map1 Buildings
        self.roc_map1 =             Building(5,5,1,1,6,"roc_map1",BuildingType.ROC_MAP1)
        self.campfire_map1 =        Building(75,25,3,3,1,"campfire_map1",BuildingType.CAMPFIRE_MAP1)
        self.flowers_map1 =         Building(30,20,4,4,9,"flowers_map1",BuildingType.FLOWERS_MAP1)
        self.house1_map1 =          Building(100,50,8,6,2,"house1_map1",BuildingType.HOUSE1_MAP1)
        self.house2_map1 =          Building(400,200,10,8,3,"house2_map1",BuildingType.HOUSE2_MAP1)
        self.house3_map1 =          Building(1000,500,14,10,3,"house3_map1",BuildingType.HOUSE3_MAP1)
        self.house4_map1 =          Building(2500,1000,40,20,3,"house4_map1",BuildingType.HOUSE4_MAP1)
        #Map2 Buildings
        self.maisonette =           Building(10000,2500,100,35,1,"maisonette",BuildingType.MAISONETTE)
        self.ecurie =               Building(15000,5000,150,50,1,"ecurie",BuildingType.ECURIE)
        self.cabane =               Building(25000,6500,300,50,2,"cabane",BuildingType.CABANE)
        self.maison =               Building(35000,2500,400,75,3,"maison",BuildingType.MAISON)
        self.forge =                Building(40000,6500,500,100,2,"forge",BuildingType.FORGE)
        self.terrainDentrainement = Building(50000,50000,600,150,1,"terrainDentrainement",BuildingType.TERRAINDENTRAINEMENT)
        self.tourDeGuet =           Building(75000,30000,1000,500,3,"tourDeGuet",BuildingType.TOURDEGUET)
        self.hdv =                  Building(100000,50000,2500,5000,5,"hdv",BuildingType.HDV)
        #Map3 Buildings
        self.house1 =               Building(2000000,100000,5000,25000,1,"house1",BuildingType.HOUSE1)
        self.house2 =               Building(5000000,150000,10000,30000,1,"house2",BuildingType.HOUSE2)
        self.house3 =               Building(10000000,200000,50000,50000,1,"house3",BuildingType.HOUSE3)

        #Listes des buildings en fonction des villes
        self.listBuildingVille1 = [self.flowers_map1, self.campfire_map1,self.roc_map1, self.house1_map1, self.house2_map1, self.house3_map1, self.house4_map1]
        self.listBuildingVille2 = [self.hdv, self.maisonette, self.maison, self.tourDeGuet,self.cabane,self.ecurie,self.terrainDentrainement,self.forge]
        self.listBuildingVille3 = [self.house1,self.house2,self.house3]

    def createBuildingsCollideArea(self,tmx_data):
        """fonction de création de la collideArea des buildings (en fonction de la map)"""
        if self.mapStep == MapStep.MAP1: 
            for building1 in self.listBuildingVille1:
                tmxObject1 = tmx_data.get_object_by_name(building1.getLibelle())
                building1.setCollideArea(tmxObject1.x, tmxObject1.y, tmxObject1.width, tmxObject1.height)       
        elif self.mapStep == MapStep.MAP2:
            for building2 in self.listBuildingVille2:
                tmxObject2 = tmx_data.get_object_by_name(building2.getLibelle())
                building2.setCollideArea(tmxObject2.x, tmxObject2.y, tmxObject2.width, tmxObject2.height)
        elif self.mapStep == MapStep.MAP3:
            for building3 in self.listBuildingVille3:
                tmxObject3 = tmx_data.get_object_by_name(building3.getLibelle())
                building3.setCollideArea(tmxObject3.x, tmxObject3.y, tmxObject3.width, tmxObject3.height)

    def onInputJoueur(self):
        """fonction qui vérifie les actions du joueur"""
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_UP]:
            self.player.bougerHaut()
            self.player.animation('up')
            self.player.setDollars(self.player.getDollars() + 0.01)
            self.player.setDiamonds(self.player.getDiamonds() +0.0001)
        elif pressedKeys[pygame.K_DOWN]:
            self.player.bougerBas()
            self.player.animation('down')
            self.player.setDollars(self.player.getDollars() + 0.01)
            self.player.setDiamonds(self.player.getDiamonds() +0.0001)
        elif pressedKeys[pygame.K_LEFT]:
            self.player.bougerGauche()
            self.player.animation('left')
            self.player.setDollars(self.player.getDollars() + 0.01)
            self.player.setDiamonds(self.player.getDiamonds() +0.0001)
        elif pressedKeys[pygame.K_RIGHT]:
            self.player.bougerDroite()
            self.player.animation('right')
            self.player.setDollars(self.player.getDollars() + 0.01)
            self.player.setDiamonds(self.player.getDiamonds() + 0.0001)


    def printGame(self):
        """fonction du  jeu (affichage, save backup, input du joueur)"""
        self.player.sauvegardeLocation()
        self.onInputJoueur()
        self.affichage.update(self.player)
        self.affichage.draw(self)
        self.affichage.flip()
        self.backup.save(self)
    
    def restoreMap(self, savedMap):
        """fonction qui change self.mapStep en fonction de la map enregistrée dans la Backup"""
        self.mapStep = savedMap

    def restoreMapData(self,restored_data):
        """fonction qui change self mapStep en fonction de la map enregistrée dans la Backup"""
        self.restoreMap(restored_data['map'])

    def restoreBuildings(self, savedBuildings):
        """fonction restoreBuilding : restaure les buildings au lancement du jeu grâce à la backup"""
        for building in savedBuildings:
            for i in range (len(self.listBuildingVille1)):
                if building.libelle == self.listBuildingVille1[i].libelle:
                    self.listBuildingVille1[i] = building
            for i in range (len(self.listBuildingVille2)):
                if building.libelle == self.listBuildingVille2[i].libelle:
                    self.listBuildingVille2[i] = building
            for i in range (len(self.listBuildingVille3)):
                if building.libelle == self.listBuildingVille3[i].libelle:
                    self.listBuildingVille3[i] = building
        self.player.setListBuilding(savedBuildings)

    def restorePlayer(self,savedPlayer):
        """fonction restorePlayer : restaure le joueur en fonction des enregistrements fait avec la backup"""
        self.player.setDollars(savedPlayer['dollars'])
        self.player.setDiamonds(savedPlayer['diamonds'])
        self.player.verificationFinVille1(savedPlayer['condition1'])
        self.player.verificationFinVille2(savedPlayer['condition2'])
        self.player.setPosition(
            savedPlayer['position_x'],
            savedPlayer['position_y']
        )

    def restoreData(self, restored_data):
        """fonction restoreData : prend les élements de la Backup et les utilise dans les fonctions permettant de les restaurer"""
        self.restoreMap(restored_data['map'])
        self.restoreBuildings(restored_data['listBuildingsPlayer'])
        self.restorePlayer(restored_data['player'])

    def getAd(self):
        return self.ad.randomAd()



        
