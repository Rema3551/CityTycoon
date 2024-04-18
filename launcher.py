from Game import *

import pygame

game = Game()

clock = pygame.time.Clock()
#pip install pygame
#pip install pytmx
#pip install pyscroll


running = True

while running:

    game.printGame()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            print("Fermeture du jeu")
            
    
    clock.tick(60)