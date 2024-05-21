import pygame
from BuildingType import *
class Building:
    """
    Attributs :
        -price
        -nextPrice
        -gain
        -nextGain
        -lvlgetNextPrice
        -lvlMax
        -libelle
        -collideArea
        -buildingType
        -multiplicator
    Méthodes :
        -mutateurs  (set...())
        -accesseurs (get...())
        -strPrice()
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
        """renvoie le multiplicateur du building"""
        return self.multiplicator
    
    def setMultiplicator(self):
        """change le multiplicateur du building"""
        self.multiplicator = self.multiplicator * 1.5

    def getLibelle(self):
        """renvoie le libelle du building"""
        return self.libelle
    
    def getPrice(self):
        """renvoie le price du building"""
        return self.price
    
    def getGain(self):
        """renvoie le gain du building"""
        return self.gain
    
    def getLvl(self):
        """renvoie le level du building"""
        return self.lvl
    
    def getNextPrice(self):
        """renvoie le nextPrice du building"""
        return self.nextPrice
    
    def getNextGain(self):
        """renvoie le nextGain du building"""
        return self.nextGain
    
    def setPrice(self):
        """change le prix du building"""
        self.setMultiplicator()
        self.price = self.price + (self.nextPrice * self.multiplicator)
    
    def setGain(self):
        """change le gain du building"""
        self.gain += self.getNextGain()
    
    def setLvl(self, nouveauLvl):
        """change le lvl du building"""
        self.lvl = nouveauLvl

    def addLvl(self):
        """ajoute un level au building"""
        self.setLvl((self.getLvl()+1))

    def setCollideArea(self, x, y, width, height):
        """change la collideArea du building"""
        self.collideArea = pygame.Rect(x, y, width, height)

    def getCollideArea(self):
        """renvoie la collideArea du building"""
        return self.collideArea
    
    def getImagePath(self):
        """renvoie le chemin de l'image du building"""
        return "assets/Images/buildings/" + self.buildingType.value
    
    def getLvlMax(self):
        """renvoie le lvlMax du building"""
        return self.lvlMax
    
    def strPrice(self):
        """str pour le prix du Building"""
        priceStr = str(int(self.price))
        if self.price<1000:
            return priceStr
        elif self.price<10000:
            return str(int(self.price/1000)) + "K" + priceStr[len(priceStr)-3] + priceStr[len(priceStr)-2]
        elif self.price<1000000:
            return str(int(self.price/1000)) + "K" + priceStr[len(priceStr)-3]
        elif self.price<10000000 : 
            return str(int(self.price/1000000)) + "M" + priceStr[len(priceStr)-6] + priceStr[len(priceStr)-5]
        elif self.price<1000000000 : 
            return str(int(self.price/1000000)) + "M" + priceStr[len(priceStr)-6]
        elif self.price<10000000000 :
            return str(int(self.price/1000000000)) + "G" + priceStr[len(priceStr)-9] + priceStr[len(priceStr)-8]
        elif self.price<1000000000000 :
            return str(int(self.price/1000000000)) + "G" + priceStr[len(priceStr)-9]