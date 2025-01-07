# 3D Basketball Game

A simple 3D basketball game built using **Pygame**, where the objective is to shoot the basketball into the hoop. The game dynamically tracks the ball's direction and velocity based on mouse movement, simulating gravity and ball movement.

## Features

- **3D Basketball Hoop**: Includes a 3D perspective for the backboard, rim, and net.
- **Ball Physics**: Gravity affects the ball's movement, with mouse-controlled shot velocity.
- **Score Tracking**: The game tracks your score as you successfully make shots.
- **Responsive Screen**: The screen adjusts to your display's resolution.

## Requirements

- **Python 3.x**: Make sure you have Python installed on your system.
- **Pygame**: You need to have the Pygame library installed.

To install Pygame, run:

```bash
pip install pygame
```

## Game Instructions

1. **Start the Game**: Run the script to launch the game.
2. **Aim the Shot**: Move your mouse to adjust the direction of the shot.
3. **Shoot**: Click the mouse to shoot the ball. The ball will follow the direction and velocity based on your mouse position.
4. **Score**: Every time the ball passes through the rim, you score a point.
5. **Game Over**: The ball resets to the starting position either after a successful shot or if it falls below the screen.

## Game Controls

- **Mouse Movement**: Adjust the direction of the ball throw.
- **Mouse Click**: Shoot the ball.

## Code Overview

- **Ball Physics**: The ball's velocity is calculated based on the mouse's position, and gravity is applied to simulate a realistic shot trajectory.
- **Hoop**: The hoop is drawn with a 3D effect, with a backboard, rim, and net.
- **Game Loop**: The game continuously updates the ball's position, checks for scoring, and redraws the game objects on the screen.

## Customization

- **Ball Properties**: Modify the `ball_radius`, `ball_gravity`, or other properties to adjust the ball's behavior.
- **Hoop Properties**: You can adjust the hoop's position, size, and other aspects.
- **Score System**: Modify how the score is calculated or displayed.

## License

This project is open source and free to use. Feel free to modify and share it!

---

Let me know if you'd like to adjust or add anything to the README!
