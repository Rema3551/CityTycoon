import pygame

class Building:
    """
    Attributs :
        -price
        -gain
        -lvl
        -multiplicateur
    Méthodes :
        -mutateurs  (set...())
        -accesseurs (get...())
    """
    def __init__(self, price : int , gain : int, libelle: str, image: str):
        self.price = price
        self.gain = gain
        self.lvl = 0
        self.multiplicateur = 0
        self.libelle = libelle
        self.collideArea = 0
        self.image = image

    def getPrice(self):
        return self.price
    
    def getGain(self):
        return self.gain
    
    def getLvl(self):
        return self.lvl
    
    def getMultiplicateur(self):
        return self.multiplicateur
    
    def setPrice(self, nouveauSeuil):
        self.price = nouveauSeuil
    
    def setGain(self, nouveauGain):
        self.gain = nouveauGain
    
    def setLvl(self, nouveauLvl):
        self.lvl = nouveauLvl

    def addLvl(self):
        self.setLvl((self.getLvl()+1))
    
    def setMultiplicateur(self, nouveauMultiplicateur):
        self.multiplicateur = nouveauMultiplicateur

    def setCollideArea(self, x, y, width, height):
        self.collideArea = pygame.Rect(x, y, width, height)

    def getCollideArea(self):
        return self.collideArea
    
    def newPrice(self,multiple):
        self.price = self.price * multiple
    
    def newGain(self, multiple):
        self.gain = self.gain * multiple
    
    def getImage(self):
        return self.image