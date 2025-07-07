# Obstacle class - Represents falling obstacles
"""
This file contains the Obstacle class that manages:
- Obstacle position and movement
- Obstacle rendering
- Obstacle spawning logic
- Obstacle removal when off-screen
"""

class Obstacle:
    """Falling obstacle that the player must avoid."""
    
    def __init__(self, x, y):
        # Obstacle initialization will go here
        pass
    
    def update(self):
        """Update obstacle position (falling down)."""
        pass
    
    def draw(self, screen):
        """Draw the obstacle on the screen."""
        pass
    
    def is_off_screen(self, screen_height):
        """Check if obstacle has fallen off the bottom of the screen."""
        pass
    
    def get_rect(self):
        """Get obstacle rectangle for collision detection."""
        pass
