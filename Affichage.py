import pygame
import pytmx
import pyscroll
from Button import *
import Game
from GameStep import *
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
        self.colorWood = (144,51,42)

        self.tmx_data = pytmx.util_pygame.load_pygame('assets/map/ville2.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        
        self.music = pygame.mixer.music.load('assets/music/music.mp3')
        pygame.mixer.music.play(-1)

        game.start(self.tmx_data)

        self.walls = []
        
        for obj in self.tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=4)
        self.group.add(game.player)
        
        self.cashDiamond = pygame.image.load("assets/Images/cashDiamond.png").convert_alpha()

        #signTuto = self.tmx_data.get_object_by_name("signTuto")
        #self.signTutoRect = pygame.Rect(signTuto.x, signTuto.y, signTuto.width, signTuto.height)
        #self.signTutoImg = pygame.image.load("assets/Images/signTuto.png")
        
        #car = self.tmx_data.get_object_by_name("car")
        #self.carRect = pygame.Rect(car.x, car.y, car.width, car.height)

        self.acheterBatimentImg = pygame.image.load("assets/Images/acheterBatiment.png")
        self.ameliorerBatimentImg = pygame.image.load("assets/Images/ameliorerBatiment.png")
        self.videoImg = pygame.image.load("assets/Images/video.png")


        self.boutonAcheter = Bouton(self.screen, 0,510,self.acheterBatimentImg,1)
        self.boutonAmeliorer = Bouton(self.screen,0,510,self.ameliorerBatimentImg,1)
        self.boutonVideo = Bouton(self.screen,725,125,self.videoImg,1)

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
        player = game.player

        self.group.draw(self.screen)
        self.screen.blit(self.cashDiamond,(0,0))
        if game.getGameStep() == GameStep.IDLE :
            textDollars = pygame.font.SysFont('comicsansms', 50).render(player.strDollars(), True, self.green)
            self.screen.blit(textDollars,(350,25))
            textDiamonds = pygame.font.SysFont('comicsansms', 50).render(player.strDiamonds(), True, self.green)
            self.screen.blit(textDiamonds,(575,25))
            
            self.boutonVideo.draw()
            if self.boutonVideo.touched():
                print("la video")
                game.setGameStep(GameStep.BUTTONVIDEO) 

            for building in game.buildings: 
                buildingImg = pygame.image.load(building.getImagePath())
                buildingImg = pygame.transform.scale(buildingImg,(175,175))
                if(player.feet.colliderect(building.getCollideArea())):
                    #print("player entering in building " + str(building.libelle))
                    # afficher prix batiment.price   
                    textPrice = pygame.font.SysFont('comicsansms', 50).render(str(building.getPrice()), True, self.colorWood)
                    if building.getLvl() == building.getLvlMax():
                        textLvl = pygame.font.SysFont('comicsansms', 50).render("MAX", True, self.colorWood)
                        self.boutonAmeliorer.draw()
                        self.screen.blit(textPrice,(380,727))
                        self.screen.blit(textLvl,(600,712))
                        self.screen.blit(buildingImg,(40,560))
                    else:
                        textLvl = pygame.font.SysFont('comicsansms', 50).render(str(building.getLvl()), True, self.colorWood)
                        if game.player.ownBuilding(building):
                            #print("player already own the building " + str(building.libelle))
                            self.boutonAmeliorer.draw()
                            self.screen.blit(textPrice,(380,727))
                            self.screen.blit(textLvl,(600,712))
                            self.screen.blit(buildingImg,(40,560))

                            if self.boutonAmeliorer.touched():
                                if player.getDollars()>= building.getPrice():
                                    player.addDollars(-building.getPrice())
                                    building.newPrice(2)
                                    building.newGain(2)
                                    building.addLvl()
                        else:
                            self.boutonAcheter.draw()
                            self.screen.blit(textPrice,(380,727))
                            self.screen.blit(textLvl,(600,712))
                            self.screen.blit(buildingImg,(40,560))
                            if self.boutonAcheter.touched():
                                if player.getDollars()>= building.getPrice():
                                    player.addDollars(-building.getPrice())
                                    player.addListBuilding(building)
                                    building.newPrice(2)
                                    building.addLvl()


                           
            """
            if player.feet.colliderect(self.signTutoRect):
                self.screen.blit(self.signTutoImg,(100,100))
                
            if player.feet.colliderect(self.carRect):
                if game.verificationFinVille1():
                    print("vous avez assez")
                else:
                    print("pour prendre la voiture et aller à la prochaine ville, vous devez avoir tous les batiments aux niveau maximum et posséder au moins 2000 dollars")
        
        """
            
        if game.getGameStep() == GameStep.BUTTONVIDEO :
            print("fonctionne")
        
        
        
        
        player.revenuPassif(game)
            
                