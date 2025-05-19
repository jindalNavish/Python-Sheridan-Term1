import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
size = 400
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("Rebel Emoji")

# Fill background with transparent-ish white
screen.fill((255, 255, 255))

# Center and radius
center = (size // 2, size // 2)
radius = 150

# Draw pastel left half
for angle in range(90, 270):
    x = center[0] + radius * math.cos(math.radians(angle))
    y = center[1] + radius * math.sin(math.radians(angle))
    pygame.draw.polygon(screen, (255, 182, 193), [center, (x, y), (center[0], center[1] - radius)])

pygame.draw.circle(screen, (255, 182, 193), center, radius, draw_top_right=False)

# Draw glitchy right half
for x in range(center[0], center[0] + radius):
    dx = x - center[0]
    if dx**2 > radius**2:
        continue
    dy = int((radius**2 - dx**2)**0.5)
    y1 = center[1] - dy
    y2 = center[1] + dy
    color = (0, random.randint(200, 255), 255)
    pygame.draw.line(screen, color, (x, y1), (x, y2))

# Border
pygame.draw.circle(screen, (0, 0, 0), center, radius, 4)

# Left eye
left_eye_center = (center[0] - 50, center[1] - 40)
pygame.draw.circle(screen, (0, 0, 0), left_eye_center, 15)

# Right eye (pixel glitch)
for _ in range(30):
    x = random.randint(center[0] + 20, center[0] + 50)
    y = random.randint(center[1] - 50, center[1] - 20)
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 4, 4))

# Smile (arc - left side only)
rect = pygame.Rect(center[0] - 90, center[1] - 10, 100, 70)
pygame.draw.arc(screen, (0, 0, 0), rect, math.radians(20), math.radians(160), 3)

# Display the result
pygame.display.flip()

# Keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
