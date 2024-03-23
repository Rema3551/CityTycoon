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
    def __init__(self, game: Game):
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
        
        game.start(self.tmx_data)

        self.walls = []
        
        for obj in self.tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=2)
        self.group.add(game.player)
        
        self.cashDiamond = pygame.image.load("assets/Images/cashDiamond.png").convert_alpha()

        signTuto = self.tmx_data.get_object_by_name("signTuto")
        self.signTutoRect = pygame.Rect(signTuto.x, signTuto.y, signTuto.width, signTuto.height)
        self.signTutoImg = pygame.image.load("assets/Images/signTuto.png")
        
        self.acheterBatimentImg = pygame.image.load("assets/Images/acheterBatiment.png")
        self.ameliorerBatimentImg = pygame.image.load("assets/Images/ameliorerBatiment.png")
        
        self.boutonAcheter = Bouton(self.screen, 0,525,self.acheterBatimentImg,1)
        self.boutonAmeliorer = Bouton(self.screen,0,525,self.ameliorerBatimentImg,1)

    def flip(self):
        pygame.display.flip()
    
    def update(self, player):
        self.group.update()
        self.group.center(player.rect)

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.revenirEnArriere()
        
        

    def draw(self, game:Game):
        """
        affichage du jeu
        """
        self.group.draw(self.screen)
        self.screen.blit(self.cashDiamond,(0,0))
        player = game.player
        
        textDollars = pygame.font.SysFont('comicsansms', 50).render(player.strDollars(), True, self.green)
        self.screen.blit(textDollars,(350,25))
        textDiamonds = pygame.font.SysFont('comicsansms', 50).render(player.strDiamonds(), True, self.green)
        self.screen.blit(textDiamonds,(575,25))
        
        for building in game.buildings: 
            buildingImg = pygame.image.load("assets/Images/buildings/"+building.getImage()+".png")
            buildingImg = pygame.transform.scale(buildingImg,(175,175))
            if(player.feet.colliderect(building.getCollideArea())):
                #print("player entering in building " + str(building.libelle))
                # afficher prix batiment.price   
                textPrice = pygame.font.SysFont('comicsansms', 50).render("Price : " + str(building.getPrice()), True, self.green)
                self.screen.blit(textPrice,(5,500))
                if game.player.ownBuilding(building):
                    #print("player already own the building " + str(building.libelle))
                    self.boutonAmeliorer.draw()
                    self.screen.blit(textPrice,(5,500))
                    self.screen.blit(buildingImg,(40,575))

                    if self.boutonAmeliorer.touched():
                        if player.getDollars()>= building.getPrice():
                            player.addDollars(-building.getPrice())
                            building.newPrice(5)
                            building.newGain(5)
                else:
                    self.boutonAcheter.draw()
                    self.screen.blit(textPrice,(5,500))
                    self.screen.blit(buildingImg,(40,575))
                    if self.boutonAcheter.touched():
                        if player.getDollars()>= building.getPrice():
                            player.addDollars(-building.getPrice())
                            player.setListeBatiment(building)
                            building.newPrice(5)
                        

        if player.feet.colliderect(self.signTutoRect):
            self.screen.blit(self.signTutoImg,(100,100))
            
        player.revenuPassif(game)
            
                