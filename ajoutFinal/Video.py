import pygame
import moviepy.editor
import random
from moviepy.editor import *

class Video:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("PUB")
        icon = pygame.image.load('assets/pdp.png')
        pygame.display.set_icon(icon)
        self.screenPUB = pygame.display.set_mode((800,800))
        
        self.adMouse = VideoFileClip("assets/pub/pub1.mp4").subclip(0,19.90)
        self.adList = [self.adMouse]        
        
        txt_clip = (TextClip("Ad",fontsize=70,color='white')
             .set_position('center')
             .set_duration(10) )
        IMAGEMAGICK_BINARY = "assets/pubImageMagick-7.1.1-30-Q16-HDRI-x64-dll.exe"
        
    def randomAd(self):
        random.shuffle(self.adList)
        return self.adList[0]
        
    
    def draw(self):
        
        self.result = moviepy.editor.CompositeVideoClip([self.randomAd(), txt_clip])
        self.result.write_videofile("assets/pub/pub1.mp4",fps=25)

        #return self.randomAd().preview()

video = Video()

running = True

while running:

    video.draw()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            print("Fermeture du jeu")