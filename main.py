import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("3D Basketball Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
GRAY = (169, 169, 169)
DARK_GRAY = (50, 50, 50)

# Game clock
clock = pygame.time.Clock()
FPS = 40

# Ball properties
ball_radius = 20
ball_x, ball_y = (SCREEN_WIDTH // 2) + random.random(), SCREEN_HEIGHT - 2 * ball_radius - 50
ball_vx, ball_vy = 0, 0
ball_gravity = 0.5
ball_shot = False

# Hoop properties
hoop_x, hoop_y = SCREEN_WIDTH // 2, 150
rim_radius = 40

# Game variables
score = 0

# Font
font = pygame.font.Font(None, 36)

def reset_ball():
    """Resets the ball to the initial position."""
    global ball_x, ball_y, ball_vx, ball_vy, ball_shot
    ball_x, ball_y = (SCREEN_WIDTH // 2) * random.random() , SCREEN_HEIGHT - 2 * ball_radius - 50
    ball_vx, ball_vy = 0, 0
    ball_shot = False

# Draw the basketball hoop with a 3D perspective
def draw_basket(x, y):
    """Draws the basketball hoop."""
    # Backboard
    backboard_width, backboard_height = 120, 10
    backboard_x = x - backboard_width // 2
    backboard_y = y - 15
    pygame.draw.rect(screen, DARK_GRAY, (backboard_x, backboard_y, backboard_width, backboard_height))

    # Rim (3D effect with two circles)
    pygame.draw.ellipse(screen, RED, (x - rim_radius, y - 10, rim_radius * 2, 10))  # Top rim
    pygame.draw.ellipse(screen, BLACK, (x - rim_radius, y - 5, rim_radius * 2, 10), 2)  # Bottom rim shadow

    # Net (3D effect)
    net_points = 8
    net_bottom_y = y + 70

    rim_points = [
        (x + int(rim_radius * math.cos(2 * math.pi * i / net_points)),
         y + int(5 * math.sin(2 * math.pi * i / net_points)))
        for i in range(net_points)
    ]

    net_bottom_points = [
        (x + int((rim_radius // 2) * math.cos(2 * math.pi * i / net_points)),
         net_bottom_y)
        for i in range(net_points)
    ]

    for top, bottom in zip(rim_points, net_bottom_points):
        pygame.draw.line(screen, WHITE, top, bottom, 2)
        
    for i in range(net_points):
        next_index = (i + 1) % net_points
        pygame.draw.line(screen, WHITE, rim_points[i], net_bottom_points[next_index], 2)
        pygame.draw.line(screen, WHITE, rim_points[next_index], net_bottom_points[i], 2)

def draw_objects():
    """Draws the game objects."""
    screen.fill(BLACK)
    pygame.draw.circle(screen, ORANGE, (int(ball_x), int(ball_y)), ball_radius)
    draw_basket(hoop_x, hoop_y)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Draw the dotted line for ball direction
    if not ball_shot:
        line_x, line_y = ball_x, ball_y
        line_length = 300  # Length of the dotted line
        gap = 5  # Gap between dots

        # Draw the dotted line
        for i in range(0, line_length, gap):
            line_x += ball_vx * (gap / 10)  # Adjust the horizontal movement
            line_y += ball_vy * (gap / 10)  # Adjust the vertical movement
            pygame.draw.circle(screen, WHITE, (int(line_x), int(line_y)), 2)

def main():
    global ball_x, ball_y, ball_vx, ball_vy, ball_shot, score
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
            # Track mouse motion to adjust the direction of the throw
                if not ball_shot:
                    # Get the mouse position
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Calculate the direction from the ball to the mouse
                    delta_x = mouse_x - ball_x
                    delta_y = mouse_y - ball_y

                    # Limit the angle between 0 and 180 degrees
                    if delta_y > 0:  # Restrict downward movement (angle > 180)
                        delta_y = 0

                    distance = math.sqrt(delta_x ** 2 + delta_y ** 2)

                    # Normalize the direction vector and set the ball's velocity
                    if distance > 0:
                        ball_vx = (delta_x / distance) * 10  # Horizontal velocity
                        ball_vy = (delta_y / distance) * 30  # Vertical velocity

            elif event.type == pygame.MOUSEBUTTONDOWN and not ball_shot:
                # Shoot the ball on mouse click
                ball_shot = True

    # Ball movement
        if ball_shot:
            ball_x += ball_vx
            ball_y += ball_vy
            ball_vy += ball_gravity  # Simulate gravity

        # Check if ball goes through the rim
        if (hoop_x - rim_radius < ball_x < hoop_x + rim_radius and
                hoop_y < ball_y < hoop_y + 10):
            score += 1
            reset_ball()

        # Reset ball if it falls below the screen
        if ball_y > SCREEN_HEIGHT:
            reset_ball()

        draw_objects()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()