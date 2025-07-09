# Obstacle class - Represents falling obstacles
"""
This file contains the Obstacle class that manages:
- Obstacle position and movement
- Obstacle rendering
- Obstacle spawning logic
- Obstacle removal when off-screen
"""

import pygame
import random
from .config import *

class Obstacle:
    """
    Falling obstacle that the player must avoid.
    
    Obstacles spawn at the top of the screen and fall downward at a constant speed.
    They are removed when they fall off the bottom of the screen.
    """
    
    def __init__(self, x, y):
        """
        Initialize an obstacle.
        
        Args:
            x (int): Starting X position
            y (int): Starting Y position (usually top of screen)
        """
        self.x = x
        self.y = y
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT
        self.speed = OBSTACLE_SPEED
        self.color = RED
    
    def update(self):
        """
        Update obstacle position (falling down).
        
        The obstacle moves downward by its speed value each frame.
        """
        self.y += self.speed
    
    def draw(self, screen):
        """
        Draw the obstacle on the screen as a colored rectangle.
        
        Args:
            screen (pygame.Surface): The screen surface to draw on
        """
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def is_off_screen(self, screen_height):
        """
        Check if obstacle has fallen off the bottom of the screen.
        
        Args:
            screen_height (int): Height of the game screen
        
        Returns:
            bool: True if obstacle is completely below the screen
        """
        return self.y > screen_height
    
    def get_rect(self):
        """
        Get obstacle rectangle for collision detection.
        
        Returns:
            pygame.Rect: Rectangle representing the obstacle's position and size
        """
        return pygame.Rect(self.x, self.y, self.width, self.height)

    @staticmethod
    def spawn_random(screen_width):
        """
        Create a new obstacle at a random X position at the top of the screen.
        
        Args:
            screen_width (int): Width of the game screen
        
        Returns:
            Obstacle: New obstacle instance
        """
        x = random.randint(0, screen_width - OBSTACLE_WIDTH)
        return Obstacle(x, -OBSTACLE_HEIGHT)
