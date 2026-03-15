import pygame
import numpy as np
import sys

# --- SETUP ---
pygame.init()
W, H = 600, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Robot Sim")
clock = pygame.time.Clock()

# --- TRACK ---
t = np.linspace(0, 2 * np.pi, 200)
track = np.column_stack([np.cos(t) * 150, np.sin(t) * 150])

# --- ROBOT ---
pos = np.array([150.0, 0.0])
heading = np.pi / 2
speed = 2.0

# --- PID ---
Kp, Ki, Kd = Kp=0.5, Ki=0.0, Kd=0.5
integral = 0.0
prev_error = 0.0

def to_screen(p):
    return (int(p[0] + W//2), int(-p[1] + H//2))

def get_error(pos):
    diffs = track - pos
    dists = np.linalg.norm(diffs, axis=1)
    closest = track[np.argmin(dists)]
    error_vec = closest - pos
    right = np.array([np.cos(heading - np.pi/2), np.sin(heading - np.pi/2)])
    true_error = np.dot(error_vec, right)
    noise = np.random.normal(0, 0.5)
    return true_error + noise

# --- MAIN LOOP ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    # Sense
    error = get_error(pos)

    # PID think
    integral += error * 0.02
    derivative = (error - prev_error) / 0.02
    steering = Kp * error + Ki * integral + Kd * derivative
    prev_error = error

    # Act
    heading += steering * 0.05
    pos[0] += np.cos(heading) * speed
    pos[1] += np.sin(heading) * speed

    # Draw
    screen.fill((20, 20, 20))
    for p in track:
        pygame.draw.circle(screen, (100, 100, 100), to_screen(p), 2)
    pygame.draw.circle(screen, (255, 60, 60), to_screen(pos), 8)

    pygame.display.flip()
    clock.tick(60)