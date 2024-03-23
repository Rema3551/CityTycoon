import pygame

class Building:
    """
    Attributs :
        -price
        -gain
        -niveau
        -multiplicateur
    Méthodes :
        -mutateurs  (set...())
        -accesseurs (get...())
    """
    def __init__(self, price : int , gain : int, libelle: str):
        self.price = price
        self.gain = gain
        self.niveau = 0
        self.multiplicateur = 0
        self.libelle = libelle
        self.collideArea = 0

    def getPrice(self):
        return self.price
    
    def getGain(self):
        return self.gain
    
    def getNiveau(self):
        return self.niveau
    
    def getMultiplicateur(self):
        return self.multiplicateur
    
    def setPrice(self, nouveauSeuil):
        self.price = nouveauSeuil
    
    def setGain(self, nouveauGain):
        self.gain = nouveauGain
    
    def setNiveau(self, nouveauNiveau):
        self.niveau = nouveauNiveau

    def ajouterNiveau(self):
        self.setNiveau((self.getNiveau()+1))
    
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