from pygame.sprite import Sprite
import pygame
stars = []
class Stars(Sprite):
    """Class to manage stars displayed on the screen."""
    
    def __init__(self, display):
        #initialising sprite and its resources 

        super().__init__()
        self.screen = display.screen

        #load stars image and set rect 
        self.image = pygame.image.load("Star 1.bmp")
        self.rect = self.image.get_rect()

        #start each star at the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height //2

        #store star in horizontal position
        self.x = float(self.rect.x)
