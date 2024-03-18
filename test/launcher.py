from Game import *
import pygame
game = Game()

clock = pygame.time.Clock()

running = True

while running:

    game.printGame()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            print("Fermeture du jeu")
    
    clock.tick(60)