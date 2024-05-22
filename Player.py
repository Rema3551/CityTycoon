import pygame
import Game

class Player(pygame.sprite.Sprite):
    """
    Attributs:
        -self.dollars
        -self.diamonds
        -self.niveau
        -self.electricite 
        -self.eau         
        -self.speed
        -self.listBuilding
        -self.sprite_sheet
        -self.image
        -self.rect
        -self.position
        -self.images
        -self.feet
        -self.anciennePosition
        -self.conditionCar
        -self.conditionBoat
    Méthodes :
        -mutateurs  (set...())
        -accesseurs (get...())
        -sauvegardeLocation
        -sauvegardeLocation(self)
        -animation(self, name)
        -update(self)
        -revenirEnArriere(self)
        -verificationFinVille1(self, verif)
        -verificationFinVille2(self, verif)
        -strDollars(self)
        -strDiamonds(self)
        -bougerDroite(self)
        -bougerGauche(self)
        -bougerHaut(self)
        -bougerBas(self)
        -revenuPassif(self,game:Game)
        -ownBuilding(self, building)
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
        
        self.sprite_sheet = pygame.image.load('assets/Images/player.png')
        self.image = self.get_image(0,0)
        self.image.set_colorkey([0,0,0]) #fait en sorte que ça soit transparent
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            'down': self.get_image(0,0),
            'left': self.get_image(2,82),
            'right': self.get_image(3,163),
            'up': self.get_image(0,246)
        }
        self.feet = pygame.Rect(0,0,self.rect.width*0.5,8)
        self.anciennePosition = self.position.copy()
        self.conditionCar = False
        self.conditionBoat = False

    def sauvegardeLocation(self):
        """fonction de sauvegarde de location du joueur"""
        self.anciennePosition = self.position.copy()
        
    def animation(self, name):
        """fonction qui permet à l'animation de l'affichage du joueur"""
        self.image = self.images[name]
        self.image.set_colorkey([0,0,0])

    def update(self):
        """met à jour la position du joueur"""
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def revenirEnArriere(self):
        """fonction qui permet de revenir en arrière, c'est à dire de mettre le joueur dans la position d'avant"""
        self.position = self.anciennePosition
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
        
    def get_image(self,x,y):
        """renvoie l'image du joueur (pour map1 et map2)"""
        image=pygame.Surface([49,69])
        image.blit(self.sprite_sheet,(0,0),(x,y,49,69))
        return image
    
    def get_imageMap3(self,x,y):
        """renvoie l'image du joueur (pour map3)"""
        image=pygame.Surface([29,41])
        image.blit(self.sprite_sheet,(0,0),(x,y,29,41))
        return image
    
    def getVerificationFinVille1(self):
        """retourne self.conditionCar (True or False)"""
        return self.conditionCar

    def verificationFinVille1(self, verif):
        """fonction de verification pour le changement de map1 à map2"""
        self.conditionCar = verif
    
    def getVerificationFinVille2(self):
        """retourne self.conditionBoat (True or False)"""
        return self.conditionBoat
    
    def verificationFinVille2(self, verif):
        """fonction de verification pour le changement de map2 à map3"""
        self.conditionBoat = verif
        
    def getDollars(self):
        """retourne self.dollars"""
        return self.dollars
        
    def strDollars(self):
        """str pour le print les dollars du joueur"""
        dollarsStr = str(int(self.dollars))
        if self.dollars<1000:
            return dollarsStr
        elif self.dollars<10000:
            return str(int(self.dollars/1000)) + "K" + dollarsStr[len(dollarsStr)-3] + dollarsStr[len(dollarsStr)-2]
        elif self.dollars<1000000:
            return str(int(self.dollars/1000)) + "K" + dollarsStr[len(dollarsStr)-3]
        elif self.dollars<10000000 :
            return str(int(self.dollars/1000000)) + "M" + dollarsStr[len(dollarsStr)-6] + dollarsStr[len(dollarsStr)-5]
        elif self.dollars<1000000000 :
            return str(int(self.dollars/1000000)) + "M" + dollarsStr[len(dollarsStr)-6]
        
        
    
    def getDiamonds(self):
        """retourne le nombre de diamants du joueur"""
        return self.diamonds
    
    def strDiamonds(self):
        """str pour le print les diamants du joueur"""
        diamondsStr = str(int(self.diamonds))
        if self.diamonds<1000:
            return diamondsStr
        elif self.diamonds<10000:
            return str(int(self.diamonds/1000)) + "K" + diamondsStr[len(diamondsStr)-3] + diamondsStr[len(diamondsStr)-2]
        elif self.diamonds<strDiamonds(self):
            return str(int(self.diamonds/1000)) + "K" + diamondsStr[len(diamondsStr)-3]
        elif self.diamonds<10000000 :
            return str(int(self.diamonds/1000000)) + "M" + diamondsStr[len(diamondsStr)-6] + diamondsStr[len(diamondsStr)-5]
        elif self.diamonds<1000000000 : 
            return str(int(self.diamonds/1000000)) + "M" + diamondsStr[len(diamondsStr)-6]
    
    def getNiveau(self):
        """retourne le niveau du joueur"""
        return self.niveau
    
    def getElectricite(self):
        """retourne le nb d'électricité du joueur"""
        return self.electricite
    
    def getEau(self, newEau):
        """retourne le nb d'eau du joueur"""
        self.eau = newEau
    
    def setDollars(self, newDollars):
        """change les dollars du joueur"""
        self.dollars = newDollars

    def addDollars(self, newDollars):
        """ajoute des dollars au joueur"""
        self.dollars+=newDollars
    
    def setDiamonds(self, newDiamants):
        """change les diamants du joueur"""
        self.diamonds = newDiamants
    
    def setNiveau(self, newNiveau):
        """change le niveau du joueur"""
        self.niveau = newNiveau
    
    def setElectricite(self, newElectricite):
        """change le nb d'électricité du joueur"""
        self.electricite = newElectricite
    
    def setEau(self, newEau):
        """change le nb d'eau du joueur"""
        self.eau = newEau
    
    def bougerDroite(self):
        """change la position du joueur vers la droite"""
        self.position[0] += self.speed

    def bougerGauche(self):
        """change la position du joueur vers la gauche"""
        self.position[0] -= self.speed

    def bougerHaut(self):
        """change la position du joueur vers le haut"""
        self.position[1] -= self.speed

    def bougerBas(self):
        """change la position du joueur vers le bas"""
        self.position[1] += self.speed

    def setPosition(self, x, y):
        """change la position du joueur"""
        self.position[0] = x
        self.position[1] = y
        
    def getListBuilding(self):
        """retourne la liste de batiments du joueur"""
        return self.listBuilding
    
    def setListBuilding(self, newListBuilding):
        """change la liste de batiments du joueur"""
        self.listBuilding = newListBuilding

    def addListBuilding(self, nouveauBatiment):
        """ajoute un batiment à la liste de batiments du joueur"""
        self.listBuilding.append(nouveauBatiment)
        
    def revenuPassif(self,game:Game):
        """fonction  permettant de calculer le revenu passif du joueur (/s)"""
        for batiment in self.listBuilding:
            #print("le batiment rapporte " + str(batiment.getGain()))
            self.addDollars(batiment.getGain()/60)

            #print(self.dollars)
    def strRevenuPassif(self,game:Game):
        """fonction str pour afficher le revenu passif par seconde du joueur"""
        revenuPassif = 0
        for batiment in self.listBuilding:
            revenuPassif += batiment.getGain()
        revenusPassifStr = str(int(revenuPassif))
        if revenuPassif <1000 :
            return revenusPassifStr + "/s"
        elif revenuPassif <10000 :
            return str(int(revenuPassif/1000)) + "K" + revenusPassifStr[len(revenusPassifStr)-3] + revenusPassifStr[len(revenusPassifStr)-2] + "/s"
        elif revenuPassif <1000000 :
            return str(int(revenuPassif/1000)) + "K" + revenusPassifStr[len(revenusPassifStr)-3] + "/s"
        elif revenuPassif <10000000 :
            return str(int(revenuPassif/1000000)) + "M" + revenusPassifStr[len(revenusPassifStr)-6] + revenusPassifStr[len(revenusPassifStr)-5] + "/s"
        elif revenuPassif <1000000000 :
            return str(int(revenuPassif/1000000)) + "M" + revenusPassifStr[len(revenusPassifStr)-6] + "/s"
            """
            return str(revenuPassif)[len(str(revenuPassif))-2] + "/s" 
        else:
            return str(int(revenuPassif/2)) + "/s"
            """

    def ownBuilding(self, building)->bool:
        """fonction qui permet de savoir si le joueur possède un batiment ou non"""
        for i in range (len(self.listBuilding)):
            return self.listBuilding[i].libelle == building.libelle
        return False