import random
import os 
import pygame

class Ad:

    def __init__(self):

        self.path = os.getcwd()
        self.adMouse = self.path+"/website/adMouse.html"
        self.adPiano = self.path+"/website/adPiano.html"
        self.adScreen = self.path+"/website/adScreen.html"
        self.listAd = [self.adMouse,self.adPiano,self.adScreen]
    
    def randomAd(self):
        ad = random.choice(self.listAd)
        return ad

