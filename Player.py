
class Player:
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
    def __init__(self):
        self.dollars = 0
        self.diamants = 0
        self.niveau = 1
        self.electricite = 0
        self.eau = 0 

    def getDollars(self):
        return self.dollars
    
    def getDiamants(self):
        return self.diamants
    
    def getNiveau(self):
        return self.niveau
    
    def getElectricite(self):
        return self.electricite
    
    def getEau(self, newEau):
        self.eau = newEau
    
    def setDollars(self, newDollars):
        self.dollars = newDollars
    
    def setDiamants(self, newDiamants):
        self.diamants = newDiamants
    
    def setNiveau(self, newNiveau):
        self.niveau = newNiveau
    
    def setElectricite(self, newElectricite):
        self.electricite = newElectricite
    
    def setEau(self, newEau):
        self.eau = newEau