import pygame
import sys
import random
from stars import Stars
from random import randint

class Star:
    """Class to manage all app resources."""

    def __init__(self):
        """initialising resources."""
        #initialising pygame
        pygame.init()
        #setting screen dimension to fullscreen 
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #retriving screen dimensions 
        self.screen_width, self.screen_height = self.screen.get_rect().width, self.screen.get_rect().height
        #settng display caption
        pygame.display.set_caption("Stars")
        #setting background colour
        self.bg_colour = (0, 20, 0)
        #creating sprite group
        self.stars = pygame.sprite.Group()
        #creating initial cluster of stars
        self._create_cluster()


    def run_app(self):
        """running app when started"""
        while True:
            self._update_screen()
            self._check_events()

    def _check_events(self):
        """check for keyboard and mouse inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #terminate window when close button is pressed
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #responds to keyboard presses
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """check for key pressed on keyboard"""
        if event.key == pygame.K_q:
            #exits window when Q is pressed
            sys.exit()
        elif event.key == pygame.K_SPACE:
            #changes star constellation when spacebar is pressed
            self._screen_clear()
            self._create_cluster()


    def _create_star(self, star_number, row_number):
        """create stars and place it in row"""
        #creating an instance of star
        star = Stars(self)
        #getting dimentions of star 
        star_width, star_height = star.rect.size
        #setting x and y positions to place star in window
        star.rect.x = star_width + star_width*2 * star_number
        star.rect.y = star_height + star_height*2 * row_number
        #adding star sprite to sprite group
        self.stars.add(star)


    def _create_cluster(self):
        """create stars"""
        #creating star instance
        star = Stars(self)
        #extracting star dimentions
        star_width, star_height = star.rect.size
        #checking available screen space for stars to be placed
        available_space_x = self.screen_width - star_width
        available_space_y = self.screen_height - star_height
        #checking the number of stars that can fit on screen
        number_star_x = available_space_x // ( star_width)
        number_rows = available_space_y // (star_height * 2)

        #creating random cluster on screen
        for row_number in range(number_rows):
            for star_number in range(number_star_x):
                if randint(0, 1) and randint(0, 1):
                    self._create_star(star_number, row_number)
    
    def _screen_clear(self):
        """removes all stars in the sprite group"""
        for star in self.stars:
            self.stars.remove(star)

    def _update_screen(self):
        """update screen with current sprites"""
        self.screen.fill(self.bg_colour)
        self.stars.draw(self.screen)
        pygame.display.flip()
        

#program's start button 
if __name__ == "__main__":
    run = Star()
    run.run_app()

