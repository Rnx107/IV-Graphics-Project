# Obstacle Avoidance AI Mini-Game
# Main entry point for the game

"""
This is the main file that starts the game.
It imports and coordinates all game components.

To run the game:
1. Make sure you have pygame installed: pip install pygame
2. Run this file: python main.py

Controls:
- A/D or Arrow Keys: Move left/right
- R: Restart game (when game over)
- ESC: Quit game
"""

import sys
import os

# Add the src directory to the Python path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.game import Game

def main():
    """
    Main function that starts the game.
    
    Creates a Game instance and starts the main game loop.
    """
    try:
        # Create and run the game
        game = Game()
        print("Starting Obstacle Avoidance Game...")
        print("Controls: A/D or Arrow Keys to move, R to restart, ESC to quit")
        game.run()
        
    except ImportError as e:
        print(f"Error importing game modules: {e}")
        print("Make sure all files are in the correct directories.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check that pygame is installed: pip install pygame")

if __name__ == "__main__":
    main()

"""
This is the main file that starts the game.
It will import and coordinate all game components.
"""

if __name__ == "__main__":
    # Game initialization and main loop will go here
    pass
