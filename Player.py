import pygame
import Game

class Player(pygame.sprite.Sprite):
    """
    Attributs:
        -dollars 
        -diamants 
        -niveau 
        -electricité 
        -eau
    Méthodes :
        -mutateur
        -accesseur
    """
    def __init__(self,x=0,y=0):
        super().__init__()
        self.dollars = 0
        self.diamonds = 0
        self.niveau = 1
        self.electricite = 0
        self.eau = 0 
        self.speed = 3
        self.listBuilding = []
        
        self.sprite_sheetOtherMaps = pygame.image.load('assets/Images/player.png')
        self.sprite_sheetMap3 = pygame.image.load('assets/Images/playerMap3.png')
        self.imageOtherMaps = self.get_imageOtherMaps(0,0).set_colorkey([0,0,0])
        self.imageMap3 = self.get_imageMap3(0,0).set_colorkey([0,0,0])
        self.rect = self.imageOtherMaps.get_rect()
        self.position = [x, y]
        self.imagesOtherMaps = {
            'down': self.get_imageOtherMaps(0,0),
            'left': self.get_imageOtherMaps(2,82),
            'right': self.get_imageOtherMaps(3,163),
            'up': self.get_imageOtherMaps(0,246)
        }
        self.imagesMap3 = {
            'down': self.get_imageMap3(0,0),
            'left': self.get_imageMap3(1,49),
            'right': self.get_imageMap3(1,96),
            'up': self.get_imageMap3(0,145)
        }
        self.feet = pygame.Rect(0,0,self.rect.width*0.5,8)
        self.anciennePosition = self.position.copy()

    def sauvegardeLocation(self):
        self.anciennePosition = self.position.copy()
        
    def animation(self, name):
        self.image = self.images[name]
        self.image.set_colorkey([0,0,0])

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def revenirEnArriere(self):
        self.position = self.anciennePosition
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
        
    def get_imageOtherMaps(self,x,y):
        image=pygame.Surface([49,69])
        image.blit(self.sprite_sheetOtherMaps,(0,0),(x,y,49,69))
        return image
    
    def get_imageMap3(self,x,y):
        image=pygame.Surface([29,41])
        image.blit(self.sprite_sheetMap3,(0,0),(x,y,29,41))
        return image
        
    def getDollars(self):
        return self.dollars
        
    def strDollars(self):
        dollarsStr = str(int(self.dollars))
        if self.dollars<1000:
            return dollarsStr
        elif self.dollars<1000000:
            return str(int(self.dollars/1000)) + "K" + dollarsStr[len(dollarsStr)-3]
        elif self.dollars<1000000000 :
            return str(int(self.dollars/1000000)) + "M" + dollarsStr[len(dollarsStr)-3]
        
    
    def getDiamonds(self):
        return self.diamonds
    
    def strDiamonds(self):
        diamondsStr = str(int(self.diamonds))
        if self.diamonds<1000:
            return diamondsStr
        elif self.diamonds<1000000:
            return str(int(self.diamonds/1000)) + "K" + diamondsStr[len(diamondsStr)-3]
        elif self.diamonds<1000000000 : 
            return str(int(self.diamonds/1000000)) + "M" + diamondsStr[len(diamondsStr)-3]
    
    def getNiveau(self):
        return self.niveau
    
    def getElectricite(self):
        return self.electricite
    
    def getEau(self, newEau):
        self.eau = newEau
    
    def setDollars(self, newDollars):
        self.dollars = newDollars

    def addDollars(self, newDollars):
        self.dollars+=newDollars
    
    def setDiamonds(self, newDiamants):
        self.diamonds = newDiamants
    
    def setNiveau(self, newNiveau):
        self.niveau = newNiveau
    
    def setElectricite(self, newElectricite):
        self.electricite = newElectricite
    
    def setEau(self, newEau):
        self.eau = newEau
    
    def bougerDroite(self) : 
        self.position[0] += self.speed

    def bougerGauche(self) : 
        self.position[0] -= self.speed

    def bougerHaut(self) : 
        self.position[1] -= self.speed

    def bougerBas(self) : 
        self.position[1] += self.speed

    def setPosition(self, x, y):
        self.position[0] = x
        self.position[1] = y
        
    def getListBuilding(self):
        return self.listBuilding
    
    def setListBuilding(self, newListBuilding):
        self.listBuilding = newListBuilding

    def addListBuilding(self, nouveauBatiment):
        self.listBuilding.append(nouveauBatiment)
        
    def revenuPassif(self):
        for batiment in self.listBuilding:
            #print("le batiment rapporte " + str(batiment.getGain()))
            self.addDollars(batiment.getGain()/60)

            #print(self.dollars)
    def strRevenuPassif(self):
        revenuPassif = 0
        for batiment in self.listBuilding:
            revenuPassif += batiment.getGain()
        if revenuPassif <10:
            return str(revenuPassif)[len(str(revenuPassif))-2] + "/s" 
        else:
            return str(int(revenuPassif/2)) + "/s"

    def ownBuilding(self, building)->bool:
        for i in range (len(self.listBuilding)):
            return self.listBuilding[i].libelle == building.libelle
        return False

                
    