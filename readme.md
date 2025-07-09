# Obstacle Avoidance AI Mini-Game

A Python Pygame project where players dodge falling obstacles, with optional AI agent functionality.

## 🎮 **Current Status: WORKING PROTOTYPE COMPLETE!**

**Last Updated: July 9, 2025**

The game is fully playable! A blue player dodges red falling obstacles in a black space environment.

## Project Structure

```
IV-Graphics-Project/
├── main.py              # Main entry point - starts the game
├── requirements.txt     # Python dependencies (pygame>=2.6.0)
├── README.txt          # This file
├── myenv/              # Virtual environment (Python 3.13.3)
├── src/                # Source code folder
│   ├── game.py         # ✅ Main game engine and loop (COMPLETE)
│   ├── player.py       # ✅ Player character class (COMPLETE)
│   ├── obstacle.py     # ✅ Obstacle class (COMPLETE)
│   ├── config.py       # ✅ Game constants and settings (COMPLETE)
│   ├── utils.py        # ✅ Utility functions (COMPLETE)
│   └── ai_agent.py     # 🔲 AI agent (Stage 3 - skeleton ready)
└── assets/             # Game assets (directories created)
    ├── images/         # Image files (future use)
    └── sounds/         # Sound files (future use)
```

## Development Stages

### ✅ Stage 1: Core Game (Manual Play) - **COMPLETED**
- [x] Set up project structure
- [x] Pygame window and main game loop
- [x] Player object and movement (A/D and Arrow Keys)
- [x] Falling obstacles with random spawning
- [x] Collision detection using pygame rectangles
- [x] Basic scoring system (points for dodged obstacles)
- [x] Game Over and Restart system (R to restart, ESC to quit)

### 🔲 Stage 2: Clean & Polish - **NEXT**
- [ ] Graphics and visual improvements
- [ ] Dynamic difficulty adjustment
- [ ] Sound effects (optional)

### 🔲 Stage 3: AI Agent (Optional) - **FUTURE**
- [ ] Rule-based AI for obstacle avoidance
- [ ] Advanced AI approaches (optional)

### 🔲 Stage 4: Documentation & Submission - **FUTURE**
- [x] Complete README documentation
- [x] Code comments and documentation
- [ ] Final testing and cleanup

## 🚀 How to Run

### Prerequisites:
- Python 3.13+ (virtual environment already set up in `myenv/`)
- Pygame 2.6.1 (already installed in virtual environment)

### Running the Game:
```bash
# Navigate to project directory
cd "IV-Graphics-Project"

# Activate virtual environment (if not already active)
source myenv/bin/activate

# Run the game
python main.py
```

## 🎮 Controls

- **A / Left Arrow**: Move player left
- **D / Right Arrow**: Move player right
- **R**: Restart game (when game over)
- **ESC**: Quit game

## ✨ Features

### Current Features (v1.0 Prototype):
- **Smooth Player Movement**: Blue rectangle player with boundary checking
- **Random Obstacle Spawning**: Red rectangles fall from random positions
- **Real-time Collision Detection**: Game ends on player-obstacle collision
- **Live Scoring System**: Points increase as obstacles are successfully dodged
- **Game Over & Restart**: Instant restart capability with R key
- **60 FPS Gameplay**: Smooth animations and responsive controls
- **Clean UI**: Score display and control instructions

### Technical Highlights:
- **Object-Oriented Design**: Separate classes for Player, Obstacle, Game, and utilities
- **Modular Code Architecture**: Each file has clear responsibilities
- **Configurable Settings**: All game constants centralized in config.py
- **Event-Driven Input**: Responsive keyboard handling with pygame events
- **Memory Management**: Automatic cleanup of off-screen obstacles

## 🧠 Code Architecture

The project follows clean coding principles with:

- **`config.py`**: Centralized constants (screen size, colors, speeds, etc.)
- **`utils.py`**: Reusable functions (collision detection, text rendering)
- **`player.py`**: Player class with movement logic and boundary checking
- **`obstacle.py`**: Obstacle class with falling behavior and spawn methods
- **`game.py`**: Main game loop coordinating all components
- **`main.py`**: Entry point with error handling and setup

## 📈 Performance

- **Frame Rate**: Stable 60 FPS
- **Memory Usage**: Efficient obstacle cleanup prevents memory leaks
- **Responsiveness**: Real-time input handling with no lag

## 🎯 Next Development Phase

Ready for Stage 2 improvements:
1. Enhanced graphics and visual effects
2. Progressive difficulty scaling
3. Sound effects and background music
4. Particle effects for collisions

---

**Game Status**: ✅ **FULLY FUNCTIONAL PROTOTYPE**  
**Development Time**: 1 day  
**Lines of Code**: ~300 (well-documented)  
**Ready for**: Stage 2 Polish & Enhancement