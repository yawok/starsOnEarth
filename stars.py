import random
from pygame.sprite import Sprite

class Stars(Sprite):
    """Class to manage stars displayed on the screen."""
    
    def __init__(self, display):
        
        super().__init__()
