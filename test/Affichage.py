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

        tmx_data = pytmx.util_pygame.load_pygame('assets/map/ville1.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        
        
        
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        self.walls = []
        
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))


        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=2)
        self.group.add(self.player)
        

        
        self.cashDiamond = pygame.image.load("assets/Images/cashDiamond.png").convert_alpha()


    def inputJoueur(self):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]:
            self.player.bougerHaut()
            self.player.animation('up')
            
            self.player.setDollars(self.player.getDollars()+900)
            #self.player.setDollars(self.player.getDollars()+0.01)
            self.player.setDiamonds(self.player.getDollars()+90)
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
            if sprite.pieds.collidelist(self.walls) > -1:
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