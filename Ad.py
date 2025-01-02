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
        self.waitTime=0
    def randomAd(self):
        ad = random.choice(self.listAd)
        if ad == self.adMouse:
            self.waitTime = 18000
        if ad == self.adPiano:
            self.waitTime = 78000
        if ad == self.adScreen:
            self.waitTime = 23000
            
        return ad

    def getWaitTime(self):
        return self.waitTime

