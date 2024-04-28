import pygame
from BuildingType import *
class Building:
    """
    Attributs :
        -price
        -gain
        -lvl
        -newGain
    Méthodes :
        -mutateurs  (set...())
        -accesseurs (get...())
    """
    def __init__(self, price : int ,nextPrice :int, gain : int, nextGain : int, lvlMax : int, libelle: str, buildingType: BuildingType):
        self.price = price
        self.nextPrice = nextPrice
        self.gain = gain
        self.nextGain = nextGain
        self.lvl = 0
        self.lvlMax = lvlMax
        self.libelle = libelle
        self.collideArea = 0
        self.buildingType = buildingType
        self.multiplicator = 1

    def getMultiplicator(self):
        return self.multiplicator
    
    def setMultiplicator(self):
        self.multiplicator = self.multiplicator * 1.5

    def getLibelle(self):
        return self.libelle
    
    def getPrice(self):
        return self.price
    
    def getGain(self):
        return self.gain
    
    def getLvl(self):
        return self.lvl
    
    def getNextPrice(self):
        return self.nextPrice
    
    def getNextGain(self):
        return self.nextGain
    
    def setPrice(self):
        self.setMultiplicator()
        self.price = self.price + (self.nextPrice * self.multiplicator)
    
    def setGain(self):
        self.gain = self.gain + self.nextGain
    
    def setLvl(self, nouveauLvl):
        self.lvl = nouveauLvl

    def addLvl(self):
        self.setLvl((self.getLvl()+1))

    def setCollideArea(self, x, y, width, height):
        self.collideArea = pygame.Rect(x, y, width, height)

    def getCollideArea(self):
        return self.collideArea
    
    def getImagePath(self):
        return "assets/Images/buildings/" + self.buildingType.value
    
    def getLvlMax(self):
        return self.lvlMax
    
    def strPrice(self):
        priceStr = str(int(self.price))
        if self.price<1000:
            return priceStr
        elif self.price<1000000:
            return str(int(self.price/1000)) + "K" + priceStr[len(priceStr)-3]
        elif self.price<1000000000 : 
            return str(int(self.price/1000000)) + "M" + priceStr[len(priceStr)-6]
        elif self.price<1000000000000 :
            return str(int(self.price/1000000000)) + "G" + priceStr[len(priceStr)-9]