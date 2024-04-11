import pygame
import moviepy.editor
import random

class Video:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("PUB")
        icon = pygame.image.load('assets/pdp.png')
        pygame.display.set_icon(icon)
        self.screenPUB = pygame.display.set_mode((800,800))
        
        self.adMouse = moviepy.editor.VideoFileClip("assets/pub/pub1.mp4")
        self.adList = [self.adMouse]
        
    def randomAd(self):
        random.shuffle(self.adList)
        return self.adList[0]
        
    
    def draw(self):
        return self.randomAd().preview()

video = Video()

running = True

while running:

    video.draw()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            print("Fermeture du jeu")
    clock.tick(120)