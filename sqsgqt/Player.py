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
    def __init__(self,x,y):
        self.dollars = 0
        self.diamonds = 0
        self.niveau = 1
        self.electricite = 0
        self.eau = 0 
        self.speed = 3
        self.listeBatiment = []
        
        super().__init__()
        self.sprite_sheet = pygame.image.load('assets/Images/player.png')
        self.image = self.get_image(0,0)
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            'down': self.get_image(0,0),
            'left': self.get_image(2,82),
            'right': self.get_image(3,163),
            'up': self.get_image(0,246)
        }
        self.feet = pygame.Rect(0,0,self.rect.width*0.5,12)
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
        
    def get_image(self,x,y):
        image=pygame.Surface([49,69])
        image.blit(self.sprite_sheet,(0,0),(x,y,49,69))
        return image
        
    def getDollars(self):
        return self.dollars
        
    def strDollars(self):
        if self.dollars<1000:
            return str(int(self.dollars))
        elif self.dollars<1000000:
            return str(int(self.dollars/1000)) + "K"
        elif self.dollars<1000000000 :
            return str(int(self.dollars/1000000)) + "M"
    
    def getDiamonds(self):
        return self.diamonds
    
    def strDiamonds(self):
        if self.diamonds<1000:
            return str(int(self.diamonds))
        elif self.diamonds<1000000:
            return str(int(self.diamonds/1000)) + "k"
        elif self.diamonds<1000000000 :
            return str(int(self.diamonds/1000000)) + "M"
    
    def getNiveau(self):
        return self.niveau
    
    def getElectricite(self):
        return self.electricite
    
    def getEau(self, newEau):
        self.eau = newEau
    
    def setDollars(self, newDollars):
        self.dollars = newDollars
    
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
        
    def getListeBatiment(self):
        self.listeBatiment
    
    def setListeBatiment(self, nouveauBatiment):
        self.listeBatiment.append(nouveauBatiment)
        
    def revenuPassif(self,game:Game):
        for i in range (len(self.listeBatiment)):
            if self.listeBatiment[i] == game.poubelle1:
                self.setDollars(self.getDollars()+game.poubelle1.gain)
                
    