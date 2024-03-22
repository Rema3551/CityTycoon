import pygame
import pytmx
import pyscroll
from Button import *
import Game
from Player import *

class Affichage:
    """
    Attributs:
        -map
    Méthodes:
        -draw
        -flip
    """
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("City Tycoon")
        icon = pygame.image.load('assets/pdp.png')
        pygame.display.set_icon(icon)
        self.screen = pygame.display.set_mode((800,800))
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)

        self.tmx_data = pytmx.util_pygame.load_pygame('assets/map/ville1.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        
        
        
        player_position = self.tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        self.walls = []
        
        for obj in self.tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=2)
        self.group.add(self.player)
        
        
        self.cashDiamond = pygame.image.load("assets/Images/cashDiamond.png").convert_alpha()

        signTuto = self.tmx_data.get_object_by_name("signTuto")
        self.signTutoRect = pygame.Rect(signTuto.x, signTuto.y, signTuto.width, signTuto.height)
        self.signTutoImg = pygame.image.load("assets/Images/signTuto.png")
        
        
        poubelle1Tmx = self.tmx_data.get_object_by_name("poubelle1")
        self.poubelle1TmxRect = pygame.Rect(poubelle1Tmx.x, poubelle1Tmx.y, poubelle1Tmx.width, poubelle1Tmx.height)
        self.payementPoubelleImg = pygame.image.load("assets/Images/signTuto.png")
        
        poubelle2Tmx = self.tmx_data.get_object_by_name("poubelle2")
        self.poubelle2TmxRect = pygame.Rect(poubelle2Tmx.x, poubelle2Tmx.y, poubelle2Tmx.width, poubelle2Tmx.height)
        
        
        poubelle3Tmx = self.tmx_data.get_object_by_name("poubelle3")
        self.poubelle3TmxRect = pygame.Rect(poubelle3Tmx.x, poubelle3Tmx.y, poubelle3Tmx.width, poubelle3Tmx.height)
        
        
        poubelle4Tmx = self.tmx_data.get_object_by_name("poubelle4")
        self.poubelle4TmxRect = pygame.Rect(poubelle4Tmx.x, poubelle4Tmx.y, poubelle4Tmx.width, poubelle4Tmx.height)
        self.payementPoubelleImg = pygame.image.load("assets/Images/signTuto.png")
        
        poubelle5Tmx = self.tmx_data.get_object_by_name("poubelle5")
        self.poubelle5TmxRect = pygame.Rect(poubelle2Tmx.x, poubelle5Tmx.y, poubelle5Tmx.width, poubelle5Tmx.height)
        
        
        poubelle6Tmx = self.tmx_data.get_object_by_name("poubelle6")
        self.poubelle6TmxRect = pygame.Rect(poubelle6Tmx.x, poubelle6Tmx.y, poubelle6Tmx.width, poubelle6Tmx.height)
        
        
        poubelle7Tmx = self.tmx_data.get_object_by_name("poubelle7")
        self.poubelle7TmxRect = pygame.Rect(poubelle7Tmx.x, poubelle7Tmx.y, poubelle7Tmx.width, poubelle7Tmx.height)
        
        
        poubelle8Tmx = self.tmx_data.get_object_by_name("poubelle8")
        self.poubelle8TmxRect = pygame.Rect(poubelle8Tmx.x, poubelle8Tmx.y, poubelle8Tmx.width, poubelle8Tmx.height)
        self.payementPoubelleImg = pygame.image.load("assets/Images/signTuto.png")
        
        poubelle9Tmx = self.tmx_data.get_object_by_name("poubelle9")
        self.poubelle9TmxRect = pygame.Rect(poubelle9Tmx.x, poubelle9Tmx.y, poubelle9Tmx.width, poubelle9Tmx.height)
        
        
        poubelle10Tmx = self.tmx_data.get_object_by_name("poubelle10")
        self.poubelle10TmxRect = pygame.Rect(poubelle10Tmx.x, poubelle10Tmx.y, poubelle10Tmx.width, poubelle10Tmx.height)
        
        HelpTmx = self.tmx_data.get_object_by_name("help")
        self.HelpTmxRect = pygame.Rect(HelpTmx.x, HelpTmx.y, HelpTmx.width, HelpTmx.height)
        self.payementHelpImg = pygame.image.load("assets/Images/signTuto.png")
        
        OrangeTmx = self.tmx_data.get_object_by_name("orange")
        self.OrangeTmxRect = pygame.Rect(OrangeTmx.x, OrangeTmx.y, OrangeTmx.width, OrangeTmx.height)
        self.payementOrangeImg = pygame.image.load("assets/Images/signTuto.png")
        
        
        self.acheterBatimentImg = pygame.image.load("assets/Images/acheterBatiment.png")
        self.ameliorerBatimentImg = pygame.image.load("assets/Images/ameliorerBatiment.png")
        
        self.boutonAcheter = Bouton(self.screen, 1,1,self.acheterBatimentImg,1)
        self.boutonAmeliorer = Bouton(self.screen,1,1,self.ameliorerBatimentImg,1)
        

    def inputJoueur(self):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]:
            self.player.bougerHaut()
            self.player.animation('up')
        
            self.player.setDollars(self.player.getDollars()+0.01)
            self.player.setDiamonds(self.player.getDiamonds()+0.0001)
        elif pressed[pygame.K_DOWN]:
            self.player.bougerBas()
            self.player.animation('down')
            
            self.player.setDollars(self.player.getDollars()+0.01)
            self.player.setDiamonds(self.player.getDiamonds()+0.0001)
        elif pressed[pygame.K_LEFT]:
            self.player.bougerGauche()
            self.player.animation('left')
            
            self.player.setDollars(self.player.getDollars()+0.01)
            self.player.setDiamonds(self.player.getDiamonds()+0.0001)
        elif pressed[pygame.K_RIGHT]:
            self.player.bougerDroite()
            self.player.animation('right')
            
            self.player.setDollars(self.player.getDollars()+0.01)
            self.player.setDiamonds(self.player.getDiamonds()+0.0001)
            
        

    def flip(self):
        pygame.display.flip()
    
    def update(self):
        self.group.update()
        self.group.center(self.player.rect)

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.revenirEnArriere()
        
        

    def draw(self, game:Game):
        """
        affichage du jeu
        """
        self.group.draw(self.screen)
        self.screen.blit(self.cashDiamond,(0,0))
        
        
        textDollars = pygame.font.SysFont('comicsansms', 50).render(self.player.strDollars(), True, self.green)
        self.screen.blit(textDollars,(350,25))
        textDiamonds = pygame.font.SysFont('comicsansms', 50).render(self.player.strDiamonds(), True, self.green)
        self.screen.blit(textDiamonds,(575,25))
        
        if self.player.feet.colliderect(self.signTutoRect):
            self.screen.blit(self.signTutoImg,(100,100))
            
        if self.player.feet.colliderect(self.poubelle1TmxRect):
            if self.player.verificationListe(game.poubelle1) == False :
                if self.boutonAcheter.draw():
                    self.player.setListeBatiment(game.poubelle1)
            else :
                if self.boutonAmeliorer.draw():
                    pass
                
        if self.player.feet.colliderect(self.poubelle2TmxRect):
            if self.player.verificationListe(game.poubelle2) == False :
                self.screen.blit(self.acheterBatimentImg,(0,500))
                self.player.setListeBatiment(game.poubelle2)
            else :
                self.screen.blit(self.ameliorerBatimentImg,(0,500))
                
        if self.player.feet.colliderect(self.poubelle3TmxRect):
            if self.player.verificationListe(game.poubelle3) == False :
                self.screen.blit(self.acheterBatimentImg,(0,500))
                self.player.setListeBatiment(game.poubelle3)
            else :
                self.screen.blit(self.ameliorerBatimentImg,(0,500))
                
        if self.player.feet.colliderect(self.poubelle4TmxRect):
            if self.player.verificationListe(game.poubelle4) == False :
                self.screen.blit(self.acheterBatimentImg,(0,500))
                self.player.setListeBatiment(game.poubelle4)
            else :
                self.screen.blit(self.ameliorerBatimentImg,(0,500))
                
        if self.player.feet.colliderect(self.poubelle5TmxRect):
            if self.player.verificationListe(game.poubelle5) == False :
                self.screen.blit(self.acheterBatimentImg,(0,500))
                self.player.setListeBatiment(game.poubelle5)
            else :
                self.screen.blit(self.ameliorerBatimentImg,(0,500))
                
        if self.player.feet.colliderect(self.poubelle6TmxRect):
            if self.player.verificationListe(game.poubelle6) == False :
                self.screen.blit(self.acheterBatimentImg,(0,500))
                self.player.setListeBatiment(game.poubelle6)
            else :
                self.screen.blit(self.ameliorerBatimentImg,(0,500))
                
        if self.player.feet.colliderect(self.poubelle7TmxRect):
            if self.player.verificationListe(game.poubelle7) == False :
                self.screen.blit(self.acheterBatimentImg,(0,500))
                self.player.setListeBatiment(game.poubelle7)
            else :
                self.screen.blit(self.ameliorerBatimentImg,(0,500))
                
        if self.player.feet.colliderect(self.poubelle8TmxRect):
            if self.player.verificationListe(game.poubelle8) == False :
                self.screen.blit(self.acheterBatimentImg,(0,500))
                self.player.setListeBatiment(game.poubelle8)
            else :
                self.screen.blit(self.ameliorerBatimentImg,(0,500))
                
        if self.player.feet.colliderect(self.poubelle9TmxRect):
            if self.player.verificationListe(game.poubelle9) == False :
                self.screen.blit(self.acheterBatimentImg,(0,500))
                self.player.setListeBatiment(game.poubelle9)
            else :
                self.screen.blit(self.ameliorerBatimentImg,(0,500))
                
        if self.player.feet.colliderect(self.poubelle10TmxRect):
            if self.player.verificationListe(game.poubelle10) == False :
                self.screen.blit(self.acheterBatimentImg,(0,500))
                self.player.setListeBatiment(game.poubelle10)
            else :
                self.screen.blit(self.ameliorerBatimentImg,(0,500))
        
        if self.player.feet.colliderect(self.HelpTmxRect):
            if self.player.verificationListe(game.Help) == False :
                self.screen.blit(self.acheterBatimentImg,(0,500))
                self.player.setListeBatiment(game.Help)
            else :
                self.screen.blit(self.ameliorerBatimentImg,(0,500))
        
        self.player.revenuPassif(game)
            
                