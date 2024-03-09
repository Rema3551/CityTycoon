from Game import *
import pygame
game = Game()



running = True

while running:

    game.print()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            print("Fermeture du jeu")