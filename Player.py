import pygame

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
        self.diamants = 0
        self.niveau = 1
        self.electricite = 0
        self.eau = 0 
        
        super().__init__()
        self.sprite_sheet = pygame.image.load('assets/Images/player.png')
        self.image = self.get_image(0,0)
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
    
    def update(self):
        self.rect.topleft = self.position
        
    def get_image(self,x,y):
        image=pygame.Surface([49,69])
        image.blit(self.sprite_sheet,(0,0),(x,y,49,69))
        return image
        
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
    
    def inputJoueur(self):
        pressed = pygme.key.get_pressed()
        
        if pressed[pygame.K_UP]:
            print("haut")
        elif pressed[pygame.K_DOWN]:
            print("bas")
        elif pressed[pygame.K_LEFT]:
            print("gauche")
        elif pressed[pygame.K_RIGHT]:
            print("droite")