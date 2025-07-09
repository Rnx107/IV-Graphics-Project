# Player class - Represents the player character
"""
This file contains the Player class that manages:
- Player position and movement
- Player rendering
- Player input handling
- Player boundaries (staying within screen)
"""

import pygame
from .config import *
from .utils import clamp

class Player:
    """
    Player character that can be controlled by human or AI.
    
    The player is represented as a colored rectangle that can move left and right
    at the bottom of the screen to avoid falling obstacles.
    """
    
    def __init__(self, x, y):
        """
        Initialize the player.
        
        Args:
            x (int): Starting X position
            y (int): Starting Y position
        """
        self.x = x
        self.y = y
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.speed = PLAYER_SPEED
        self.color = BLUE
        
        # Movement flags
        self.moving_left = False
        self.moving_right = False
    
    def update(self, screen_width):
        """
        Update player position based on movement flags.
        
        Args:
            screen_width (int): Width of the game screen for boundary checking
        """
        # Apply movement based on flags
        if self.moving_left:
            self.x -= self.speed
        if self.moving_right:
            self.x += self.speed
        
        # Keep player within screen boundaries
        self.x = clamp(self.x, 0, screen_width - self.width)
    
    def draw(self, screen):
        """
        Draw the player on the screen as a colored rectangle.
        
        Args:
            screen (pygame.Surface): The screen surface to draw on
        """
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def move_left(self):
        """Start moving the player left."""
        self.moving_left = True
    
    def move_right(self):
        """Start moving the player right."""
        self.moving_right = True
    
    def stop_left(self):
        """Stop moving the player left."""
        self.moving_left = False
    
    def stop_right(self):
        """Stop moving the player right."""
        self.moving_right = False
    
    def get_rect(self):
        """
        Get player rectangle for collision detection.
        
        Returns:
            pygame.Rect: Rectangle representing the player's position and size
        """
        return pygame.Rect(self.x, self.y, self.width, self.height)
