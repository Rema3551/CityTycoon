class Building:
    """
    Attributs :
        -seuil
        -gain
        -niveau
        -multiplicateur
    Méthodes :
        -mutateurs  (set...())
        -accesseurs (get...())
    """
    def __init__(self, seuil : int , gain : int):
        self.seuil = seuil
        self.gain = gain
        self.niveau = 0
        self.multiplicateur = 0

    def getSeuil(self):
        return self.seuil
    
    def getGain(self):
        return self.gain
    
    def getNiveau(self):
        return self.niveau
    
    def getMultiplicateur(self):
        return self.multiplicateur
    
    def setSeuil(self, nouveauSeuil):
        self.seuil = nouveauSeuil
    
    def setGain(self, nouveauGain):
        self.gain = nouveauGain
    
    def setNiveau(self, nouveauNiveau):
        self.niveau = nouveauNiveau
    
    def setMultiplicateur(self, nouveauMultiplicateur):
        self.multiplicateur = nouveauMultiplicateur