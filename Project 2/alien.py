import os 
import pygame 
from pygame.sprite import Sprite 

"""pg.257,263,265"""

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen

        #Load the alien image and set its rect attribute.
        self.image = pygame.image.load(
            os.path.join(os.path.dirname(__file__), 'UFO_2.png'))
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen 
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height 

        #store the alien's exact horizontal position 
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of scrren."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien to the right"""
        self.x += self.ai_game.settings.alien_speed * self.ai_game.settings.fleet_direction
        self.rect.x = self.x 


