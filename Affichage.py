import pygame
import pytmx
import pyscroll
from Button import *
import Game
from GameStep import *
from MapStep import *
from Player import *
import Backup

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

        player = game.player

        game.backup.loadMap(game)
        if game.getMapStep()==MapStep.MAP1:   
            self.tmx_data = pytmx.util_pygame.load_pygame('assets/map/ville1.tmx')
            car = self.tmx_data.get_object_by_name("car")
            self.carRect = pygame.Rect(car.x, car.y, car.width, car.height)
            signTuto = self.tmx_data.get_object_by_name("signTuto")
            self.signTutoRect = pygame.Rect(signTuto.x, signTuto.y, signTuto.width, signTuto.height)
            self.signTutoImg = pygame.image.load("assets/Images/signTuto.png")

            map_data = pyscroll.data.TiledMapData(self.tmx_data)
            map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
            game.start(self.tmx_data)
            self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=42)
            self.group.add(game.player)

        elif game.getMapStep()==MapStep.MAP2:
            self.tmx_data = pytmx.util_pygame.load_pygame('assets/map/ville2.tmx')
            boat = self.tmx_data.get_object_by_name("boat")
            self.boatRect = pygame.Rect(boat.x, boat.y, boat.width, boat.height)
            car2 = self.tmx_data.get_object_by_name("car2")
            self.car2Rect = pygame.Rect(car2.x, car2.y, car2.width, car2.height)

            map_data = pyscroll.data.TiledMapData(self.tmx_data)
            map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
            game.start(self.tmx_data)
            self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=53)
            self.group.add(game.player)

        elif game.getMapStep()==MapStep.MAP3:

            game.player.sprite_sheet = pygame.image.load('assets/Images/playerMap3.png')
            game.player.image = game.player.get_imageMap3(0,0)
            game.player.image.set_colorkey([0,0,0]) #fait en sorte que ça soit transparent
            game.player.rect = game.player.image.get_rect()
            game.player.images = {
                'down': game.player.get_imageMap3(0,0),
                'left': game.player.get_imageMap3(1,49),
                'right': game.player.get_imageMap3(1,96),
                'up': game.player.get_imageMap3(0,145)
            }

            self.tmx_data = pytmx.util_pygame.load_pygame('assets/map/ville3.tmx')
            
            map_data = pyscroll.data.TiledMapData(self.tmx_data)
            map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
            game.start(self.tmx_data)
            self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=53)
            self.group.add(game.player)

            house1Rect = self.tmx_data.get_object_by_name("house1")
            self.house1Rect = pygame.Rect(house1Rect.x, house1Rect.y, house1Rect.width, house1Rect.height)
            boatMap3Rect = self.tmx_data.get_object_by_name("boatMap3")
            self.boatMap3Rect = pygame.Rect(boatMap3Rect.x, boatMap3Rect.y, boatMap3Rect.width, boatMap3Rect.height)

        elif game.getMapStep()==MapStep.HOUSE1:

            game.player.sprite_sheet = pygame.image.load('assets/Images/player.png')
            game.player.image = game.player.get_image(0,0)
            game.player.image.set_colorkey([0,0,0]) #fait en sorte que ça soit transparent
            game.player.rect = game.player.image.get_rect()
            player.images = {
            'down': player.get_image(0,0),
            'left': player.get_image(2,82),
            'right': player.get_image(3,163),
            'up': player.get_image(0,246)
            }

            self.tmx_data = pytmx.util_pygame.load_pygame('assets/map/house1.tmx')
            map_data = pyscroll.data.TiledMapData(self.tmx_data)
            map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
            game.start(self.tmx_data)
            self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=42)
            self.group.add(game.player)

            enterHouse1 = self.tmx_data.get_object_by_name("enter_house1")
            self.enterHouse1 = pygame.Rect(enterHouse1.x, enterHouse1.y, enterHouse1.width, enterHouse1.height)

        self.music = pygame.mixer.music.load('assets/music/music.mp3')
        pygame.mixer.music.play(-1)

        

        self.walls = []
        
        for obj in self.tmx_data.objects:
            if obj.name == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=33)
        self.group.add(game.player)
        
        self.cashDiamond = pygame.image.load("assets/Images/cashDiamond.png").convert_alpha()
        self.acheterBatimentImg = pygame.image.load("assets/Images/acheterBatiment.png")
        self.ameliorerBatimentImg = pygame.image.load("assets/Images/ameliorerBatiment.png")
        self.videoDiamondImg = pygame.image.load("assets/Images/videoDiamond.png")
        self.pubImg = pygame.image.load("assets/Images/buttonPub.png")
        self.buttonYesImg = pygame.image.load("assets/Images/buttonYes.png")
        self.buttonNoImg = pygame.image.load("assets/Images/buttonNo.png")
        #self.afficheChangementVilleImg = pygame.image.load("assets/Images/afficheChangementVille.png")

        self.boutonAcheter = Bouton(self.screen, -129,125,self.acheterBatimentImg,1)
        self.boutonAmeliorer = Bouton(self.screen,-129,125,self.ameliorerBatimentImg,1)
        self.boutonDiamondVideo = Bouton(self.screen,725,125,self.videoDiamondImg,1)
        self.boutonPub = Bouton(self.screen,125,125,self.pubImg,1.5)
        self.boutonYes = Bouton(self.screen,450,550,self.buttonYesImg,1)
        self.boutonNo = Bouton(self.screen,250,550,self.buttonNoImg,1)
                
        


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
        
        textRevenuPassif = pygame.font.SysFont('comicsansms', 50).render(player.strRevenuPassif(game), True, self.green)
        self.screen.blit(textRevenuPassif,(85,25))

        
        textDollars = pygame.font.SysFont('comicsansms', 50).render(player.strDollars(), True, self.green)
        self.screen.blit(textDollars,(330,25))
        textDiamonds = pygame.font.SysFont('comicsansms', 50).render(player.strDiamonds(), True, self.green)
        self.screen.blit(textDiamonds,(575,25))
        
        self.boutonDiamondVideo.draw()
        if self.boutonDiamondVideo.touched():
            print("la video")
            game.setGameStep(GameStep.BUTTONVIDEO)
        
        if game.getGameStep() == GameStep.BUTTONVIDEO:
            print("fonctionne")
            self.boutonPub.draw()
            self.boutonYes.draw()
            self.boutonNo.draw()
            if self.boutonYes.touched():
                print("oooooh")
                game.setGameStep(GameStep.BUTTONVIDEO)
            if self.boutonNo.touched() :
                print("purééeeee")
                game.setGameStep(GameStep.IDLE)

        if game.getGameStep() == GameStep.IDLE:
            if game.getMapStep() == MapStep.MAP1:
                for building in game.listBuildingVille1:
                    buildingImg = pygame.image.load(building.getImagePath())
                    buildingImg = pygame.transform.scale(buildingImg,(180,180))
                    
                    tmxObject = self.tmx_data.get_object_by_name(building.getLibelle())
                    building.setCollideArea(tmxObject.x, tmxObject.y, tmxObject.width, tmxObject.height)

                    if(player.feet.colliderect(building.getCollideArea())):
                        self.screen.blit(buildingImg,(40,560))
                        #print("player entering in building " + str(building.libelle))
                        # afficher prix batiment.price
                        textPrice = pygame.font.SysFont('comicsansms', 45).render(str(building.strPrice()), True, self.colorWood)
                        if building.getLvl() == building.getLvlMax():
                            textLvl = pygame.font.SysFont('comicsansms', 50).render("MAX", True, self.colorWood)
                            self.boutonAmeliorer.draw()
                            #self.screen.blit(textPrice,(380,727))
                            #self.screen.blit(self.cashDiamond,(380,727)) # Faire un détourage pour la piece et le diamant
                            self.screen.blit(textLvl,(600,712))
                            
                        else:
                            textLvl = pygame.font.SysFont('comicsansms', 50).render(str(building.getLvl()), True, self.colorWood)
                            if game.player.ownBuilding(building):
                                #print("player already own the building " + str(building.libelle))
                                self.boutonAmeliorer.draw()
                                self.screen.blit(textPrice,(380,727))
                                self.screen.blit(textLvl,(600,712))

                                if self.boutonAmeliorer.touched():
                                    if player.getDollars()>= building.getPrice():
                                        player.addDollars(-building.getPrice())
                                        building.addLvl()
                                        building.setPrice()
                                        building.setGain()
                                        
                            else:
                                self.boutonAcheter.draw()
                                self.screen.blit(textPrice,(380,727))
                                self.screen.blit(textLvl,(600,712))
                                if self.boutonAcheter.touched():
                                    if player.getDollars()>= building.getPrice():
                                        player.addDollars(-building.getPrice())
                                        player.addListBuilding(building)
                                        building.addLvl() 
                                        building.setPrice()                  
                #Verification de la collision pour la voiture
                if player.feet.colliderect(self.carRect):
                    self.switchMap("car",game)
                    

            elif game.getMapStep() == MapStep.MAP2:
                for building in game.listBuildingVille2:
                    buildingImg = pygame.image.load(building.getImagePath())
                    buildingImg = pygame.transform.scale(buildingImg,(175,175))

                    tmxObject = self.tmx_data.get_object_by_name(building.getLibelle())
                    building.setCollideArea(tmxObject.x, tmxObject.y, tmxObject.width, tmxObject.height)

                    #building.setCollideArea(self.tmx_data.get_object_by_name(building.libelle).x,self.tmx_data.get_object_by_name(building.libelle).y,self.tmx_data.get_object_by_name(building.libelle).width,self.tmx_data.get_object_by_name(building.libelle).height)
                    if(player.feet.colliderect(building.getCollideArea())):
                        #print("player entering in building " + str(building.libelle))
                        # afficher prix batiment.price
                        textPrice = pygame.font.SysFont('comicsansms', 45).render(str(building.strPrice()), True, self.colorWood)
                        if building.getLvl() == building.getLvlMax():
                            textLvl = pygame.font.SysFont('comicsansms', 50).render("MAX", True, self.colorWood)
                            self.boutonAmeliorer.draw()
                            #self.screen.blit(textPrice,(380,727))
                            #self.screen.blit(self.cashDiamond,(380,727)) # Faire un détourage pour la piece et le diamant
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
                                        building.addLvl() 
                                        building.setPrice()
                                        building.setGain()
                            else:
                                self.boutonAcheter.draw()
                                self.screen.blit(textPrice,(380,727))
                                self.screen.blit(textLvl,(600,712))
                                self.screen.blit(buildingImg,(40,560))
                                if self.boutonAcheter.touched():
                                    if player.getDollars()>= building.getPrice():
                                        player.addDollars(-building.getPrice())
                                        player.addListBuilding(building)
                                        building.addLvl()
                                        building.setPrice()

                #Verification de la collision pour le boat
                if player.feet.colliderect(self.boatRect):
                    self.switchMap("boat",game)

                if player.feet.colliderect(self.car2Rect):
                    self.switchMap("car2",game)

            elif game.getMapStep() == MapStep.MAP3:
                for building in game.listBuildingVille3:
                    buildingImg = pygame.image.load(building.getImagePath())
                    buildingImg = pygame.transform.scale(buildingImg,(175,175))

                    tmxObject = self.tmx_data.get_object_by_name(building.getLibelle())
                    building.setCollideArea(tmxObject.x, tmxObject.y, tmxObject.width, tmxObject.height)

                    #building.setCollideArea(self.tmx_data.get_object_by_name(building.libelle).x,self.tmx_data.get_object_by_name(building.libelle).y,self.tmx_data.get_object_by_name(building.libelle).width,self.tmx_data.get_object_by_name(building.libelle).height)
                    if(player.feet.colliderect(building.getCollideArea())):
                        #print("player entering in building " + str(building.libelle))
                        # afficher prix batiment.price
                        textPrice = pygame.font.SysFont('comicsansms', 45).render(str(building.strPrice()), True, self.colorWood)
                        if building.getLvl() == building.getLvlMax():
                            textLvl = pygame.font.SysFont('comicsansms', 50).render("MAX", True, self.colorWood)
                            self.boutonAmeliorer.draw()
                            #self.screen.blit(textPrice,(380,727))
                            #self.screen.blit(self.cashDiamond,(380,727)) # Faire un détourage pour la piece et le diamant
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
                                        building.addLvl()
                                        building.setPrice()
                                        building.setGain()
                            else:
                                self.boutonAcheter.draw()
                                self.screen.blit(textPrice,(380,727))
                                self.screen.blit(textLvl,(600,712))
                                self.screen.blit(buildingImg,(40,560))
                                if self.boutonAcheter.touched():
                                    if player.getDollars()>= building.getPrice():
                                        player.addDollars(-building.getPrice())
                                        player.addListBuilding(building)
                                        building.addLvl()
                                        building.setPrice()   

                
                if player.feet.colliderect(self.house1Rect) and game.listBuildingVille3[0].getLvl() == game.listBuildingVille3[0].getLvlMax():
                    self.switchMap("house1Entry",game)

                if player.feet.colliderect(self.boatMap3Rect):
                    self.switchMap("boatMap3",game)

            elif game.getMapStep() == MapStep.HOUSE1:
                if player.feet.colliderect(self.enterHouse1):
                    self.switchMap("enterHouse1",game)

        player.revenuPassif(game)
            
            
    def switchMap(self, object, game:Game):
        player = game.player

        #Liste qui va stocker les rectangles de collision 
        self.walls = []
        for obj in self.tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        #Dessiner les calques
        #self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=4)
        #self.group.add(game.player)

        #Changement de map
        if game.getMapStep() == MapStep.MAP1:
            self.tmx_data = pytmx.util_pygame.load_pygame('assets/map/ville2.tmx')
            map_data = pyscroll.data.TiledMapData(self.tmx_data)
            map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
            self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=6)
            self.group.add(game.player)
            self.walls=[]
            for obj in self.tmx_data.objects:
                if obj.type == "collision":
                    self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
                
            #rectangle de collision pour le boat
            boat = self.tmx_data.get_object_by_name("boat")
            self.boatRect = pygame.Rect(boat.x, boat.y, boat.width, boat.height)
            car2 = self.tmx_data.get_object_by_name("car2")
            self.car2Rect = pygame.Rect(car2.x, car2.y, car2.width, car2.height)
            spawnMap2 = self.tmx_data.get_object_by_name("spawn_map2")
            game.player.position[0] = spawnMap2.x
            game.player.position[1] = spawnMap2.y
            if object == "car":
                game.setMapStep(MapStep.MAP2)

        elif game.getMapStep() == MapStep.MAP2:

            if object == "car2":
                
                self.tmx_data = pytmx.util_pygame.load_pygame('assets/map/ville1.tmx')
                map_data = pyscroll.data.TiledMapData(self.tmx_data)
                map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
                self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
                self.group.add(game.player)
                self.walls=[]
                for obj in self.tmx_data.objects:
                    if obj.type == "collision":
                        self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
                

                #rectangle de collision pour la voiture
                car = self.tmx_data.get_object_by_name("car")
                self.carRect = pygame.Rect(car.x, car.y, car.width, car.height)
                spawnMap1 = self.tmx_data.get_object_by_name("spawn_map1")
                game.player.position[0] = spawnMap1.x
                game.player.position[1] = spawnMap1.y
                game.setMapStep(MapStep.MAP1)

            if object == "boat":

                game.player.sprite_sheet = pygame.image.load('assets/Images/playerMap3.png')
                game.player.image = game.player.get_imageMap3(0,0)
                game.player.image.set_colorkey([0,0,0]) #fait en sorte que ça soit transparent
                game.player.rect = game.player.image.get_rect()
                game.player.images = {
                    'down': game.player.get_imageMap3(0,0),
                    'left': game.player.get_imageMap3(1,49),
                    'right': game.player.get_imageMap3(1,96),
                    'up': game.player.get_imageMap3(0,145)
                }

                self.tmx_data = pytmx.util_pygame.load_pygame('assets/map/ville3.tmx')
                map_data = pyscroll.data.TiledMapData(self.tmx_data)
                map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
                self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=53)
                self.group.add(game.player)
                self.walls=[]
                for obj in self.tmx_data.objects:
                    if obj.name == "collision":
                        self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
                
                house1Rect = self.tmx_data.get_object_by_name("house1")
                self.house1Rect = pygame.Rect(house1Rect.x, house1Rect.y, house1Rect.width, house1Rect.height)
                boatMap3Rect = self.tmx_data.get_object_by_name("boatMap3")
                self.boatMap3Rect = pygame.Rect(boatMap3Rect.x, boatMap3Rect.y, boatMap3Rect.width, boatMap3Rect.height)

                spawnMap3 = self.tmx_data.get_object_by_name("spawn_map3")
                game.player.position[0] = spawnMap3.x
                game.player.position[1] = spawnMap3.y

                game.setMapStep(MapStep.MAP3)
        
        elif game.getMapStep() == MapStep.MAP3:
            if object == "house1Entry":

                game.player.sprite_sheet = pygame.image.load('assets/Images/player.png')
                game.player.image = game.player.get_image(0,0)
                game.player.image.set_colorkey([0,0,0]) #fait en sorte que ça soit transparent
                game.player.rect = game.player.image.get_rect()
                player.images = {
                'down': player.get_image(0,0),
                'left': player.get_image(2,82),
                'right': player.get_image(3,163),
                'up': player.get_image(0,246)
                }

                self.tmx_data = pytmx.util_pygame.load_pygame('assets/map/house1.tmx')
                map_data = pyscroll.data.TiledMapData(self.tmx_data)
                map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
                self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=53)
                self.group.add(game.player)
                self.walls=[]
                for obj in self.tmx_data.objects:
                    if obj.name == "collision":
                        self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
                
                enterHouse1 = self.tmx_data.get_object_by_name("enter_house1")
                self.enterHouse1 = pygame.Rect(enterHouse1.x, enterHouse1.y, enterHouse1.width, enterHouse1.height)
                

                spawnHouse1 = self.tmx_data.get_object_by_name("spawn_house1")
                game.player.position[0] = spawnHouse1.x
                game.player.position[1] = spawnHouse1.y

                game.setMapStep(MapStep.HOUSE1)

            if object == "boatMap3":

                self.tmx_data = pytmx.util_pygame.load_pygame('assets/map/ville2.tmx')
                map_data = pyscroll.data.TiledMapData(self.tmx_data)
                map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
                self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=6)
                self.group.add(game.player)
                self.walls=[]
                for obj in self.tmx_data.objects:
                    if obj.type == "collision":
                        self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
                    
                #rectangle de collision pour le boat
                boat = self.tmx_data.get_object_by_name("boat")
                self.boatRect = pygame.Rect(boat.x, boat.y, boat.width, boat.height)
                car2 = self.tmx_data.get_object_by_name("car2")
                self.car2Rect = pygame.Rect(car2.x, car2.y, car2.width, car2.height)
                spawnMap2 = self.tmx_data.get_object_by_name("spawn_map2")
                game.player.position[0] = spawnMap2.x
                game.player.position[1] = spawnMap2.y
                game.setMapStep(MapStep.MAP2)

        elif game.getMapStep() == MapStep.HOUSE1:
            if object == "enterHouse1":

                game.player.sprite_sheet = pygame.image.load('assets/Images/playerMap3.png')
                game.player.image = game.player.get_imageMap3(0,0)
                game.player.image.set_colorkey([0,0,0]) #fait en sorte que ça soit transparent
                game.player.rect = game.player.image.get_rect()
                game.player.images = {
                    'down': game.player.get_imageMap3(0,0),
                    'left': game.player.get_imageMap3(1,49),
                    'right': game.player.get_imageMap3(1,96),
                    'up': game.player.get_imageMap3(0,145)
                }


                self.tmx_data = pytmx.util_pygame.load_pygame('assets/map/ville3.tmx')
                map_data = pyscroll.data.TiledMapData(self.tmx_data)
                map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
                self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=53)
                self.group.add(game.player)
                self.walls=[]
                for obj in self.tmx_data.objects:
                    if obj.name == "collision":
                        self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
                
                house1Rect = self.tmx_data.get_object_by_name("house1")
                self.house1Rect = pygame.Rect(house1Rect.x, house1Rect.y, house1Rect.width, house1Rect.height)

                spawnMap3 = self.tmx_data.get_object_by_name("spawn_map3")
                game.player.position[0] = spawnMap3.x
                game.player.position[1] = spawnMap3.y

                game.setMapStep(MapStep.MAP3)
                

            
            
            
            
            
            
