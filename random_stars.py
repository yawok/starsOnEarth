import pygame
import sys

class Star:
    """Class to manage all app resources."""

    def __init__(self):
        #initialising resources
        pygame.init()
        self.screen = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Stars")
        self.bg_colour = (0, 20, 0)

    def run_app(self):
        #running app when started
        while True:
            self._update_screen()
            self._check_events()

    def _check_events(self):
        #check for keyboard and mouse inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events()

    def _check_keydown_events(self):
        #check for key pressed on keyboard
        if event.type == pygame.K_q:
            sys.exit()
        
    def _update_screen(self):
        self.screen.fill(self.bg_colour)
        pygame.display.flip()


if __name__ == "__main__":
    run = Star()
    run.run_app()

