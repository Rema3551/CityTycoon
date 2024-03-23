import pygame


class Bouton():
    def __init__(self, screen, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.screen = screen

    def touched(self):
        action = False
        #prend la position de la souris
        pos = pygame.mouse.get_pos()
        #vérifie la position de la souris quand on clique
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action
    
    def draw(self):
        self.screen.blit(self.image,(self.rect.x, self.rect.y))  
        