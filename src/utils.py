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
    """Check if two rectangles collide."""
    # Collision detection logic will go here
    pass

def draw_text(screen, text, size, x, y, color=(255, 255, 255)):
    """Draw text on the screen at specified position."""
    # Text rendering logic will go here
    pass

def clamp(value, min_value, max_value):
    """Keep value within specified bounds."""
    return max(min_value, min(value, max_value))
