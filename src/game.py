# Game class - Main game engine and loop
"""
This file contains the main Game class that manages:
- Game state (playing, game over, paused)
- Main game loop
- Event handling
- Screen updates
- Coordination between all game objects
"""

import pygame
import random
import sys
from .config import *
from .player import Player
from .obstacle import Obstacle
from .utils import check_collision, draw_text

class Game:
    """
    Main game class that handles the game loop and state management.
    
    This class coordinates all game objects and manages the overall game flow,
    including player input, obstacle spawning, collision detection, and rendering.
    """
    
    def __init__(self):
        """Initialize the game and all its components."""
        # Initialize Pygame
        pygame.init()
        
        # Set up the display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        
        # Initialize game state
        self.running = True
        self.game_over = False
        self.score = 0
        
        # Initialize game objects
        self.player = Player(PLAYER_START_X, PLAYER_START_Y)
        self.obstacles = []
        
        # Obstacle spawning timer
        self.obstacle_spawn_timer = 0
        self.next_spawn_time = random.randint(OBSTACLE_MIN_SPAWN_TIME, OBSTACLE_MAX_SPAWN_TIME)
    
    def run(self):
        """
        Main game loop.
        
        This is the heart of the game - it continuously processes events,
        updates game state, and draws everything to the screen.
        """
        while self.running:
            self.handle_events()
            
            if not self.game_over:
                self.update()
            
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()
    
    def handle_events(self):
        """
        Handle user input and pygame events.
        
        Processes keyboard input for player movement and game controls.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.move_left()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.move_right()
                elif event.key == pygame.K_r and self.game_over:
                    self.restart_game()
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.stop_left()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.stop_right()
    
    def update(self):
        """
        Update game state, positions, collisions, etc.
        
        This method is called every frame to update all game objects
        and check for game events like collisions.
        """
        # Update player
        self.player.update(SCREEN_WIDTH)
        
        # Spawn new obstacles
        self.obstacle_spawn_timer += 1
        if self.obstacle_spawn_timer >= self.next_spawn_time:
            self.obstacles.append(Obstacle.spawn_random(SCREEN_WIDTH))
            self.obstacle_spawn_timer = 0
            self.next_spawn_time = random.randint(OBSTACLE_MIN_SPAWN_TIME, OBSTACLE_MAX_SPAWN_TIME)
        
        # Update obstacles
        for obstacle in self.obstacles[:]:  # Use slice copy to safely modify list
            obstacle.update()
            
            # Remove obstacles that have fallen off screen
            if obstacle.is_off_screen(SCREEN_HEIGHT):
                self.obstacles.remove(obstacle)
                self.score += SCORE_INCREMENT
        
        # Check collisions
        player_rect = self.player.get_rect()
        for obstacle in self.obstacles:
            if check_collision(player_rect, obstacle.get_rect()):
                self.game_over = True
                break
    
    def draw(self):
        """
        Draw all game objects to the screen.
        
        Renders the player, obstacles, UI elements, and game over screen.
        """
        # Clear screen
        self.screen.fill(BLACK)
        
        if not self.game_over:
            # Draw game objects
            self.player.draw(self.screen)
            
            for obstacle in self.obstacles:
                obstacle.draw(self.screen)
            
            # Draw UI
            draw_text(self.screen, f"Score: {self.score}", 36, 100, 30, WHITE)
            draw_text(self.screen, "Use A/D or Arrow Keys to Move", 24, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30, WHITE)
        
        else:
            # Draw game over screen
            draw_text(self.screen, "GAME OVER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, RED)
            draw_text(self.screen, f"Final Score: {self.score}", 36, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, WHITE)
            draw_text(self.screen, "Press R to Restart or ESC to Quit", 24, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50, WHITE)
        
        # Update display
        pygame.display.flip()
    
    def restart_game(self):
        """
        Restart the game to initial state.
        
        Resets all game variables and objects to their starting conditions.
        """
        self.game_over = False
        self.score = 0
        self.player = Player(PLAYER_START_X, PLAYER_START_Y)
        self.obstacles = []
        self.obstacle_spawn_timer = 0
        self.next_spawn_time = random.randint(OBSTACLE_MIN_SPAWN_TIME, OBSTACLE_MAX_SPAWN_TIME)
