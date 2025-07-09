# Utility functions for the game
"""
This file contains utility functions that can be used throughout the game:
- Collision detection
- Score management
- Text rendering helpers
- Other common functions
"""

import pygame

def check_collision(rect1, rect2):
    """
    Check if two rectangles collide using pygame's built-in collision detection.
    
    Args:
        rect1 (pygame.Rect): First rectangle
        rect2 (pygame.Rect): Second rectangle
    
    Returns:
        bool: True if rectangles overlap, False otherwise
    """
    return rect1.colliderect(rect2)

def draw_text(screen, text, size, x, y, color=(255, 255, 255)):
    """
    Draw text on the screen at specified position.
    
    Args:
        screen (pygame.Surface): The screen surface to draw on
        text (str): Text to display
        size (int): Font size
        x (int): X coordinate (center of text)
        y (int): Y coordinate (center of text)
        color (tuple): RGB color tuple
    """
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def clamp(value, min_value, max_value):
    """
    Keep value within specified bounds.
    
    Args:
        value (float): Value to clamp
        min_value (float): Minimum allowed value
        max_value (float): Maximum allowed value
    
    Returns:
        float: Clamped value
    """
    return max(min_value, min(value, max_value))
