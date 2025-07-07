# Game configuration and constants
"""
This file contains all the game constants and configuration settings:
- Screen dimensions
- Colors
- Game speeds
- Player/obstacle sizes
- Other game parameters
"""

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (RGB values)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5

# Obstacle settings
OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = 30
OBSTACLE_SPEED = 3
OBSTACLE_SPAWN_RATE = 60  # frames between obstacle spawns

# Game settings
INITIAL_LIVES = 3
SCORE_INCREMENT = 10
