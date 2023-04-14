import pygame
import random
from maze_generation import hunt_n_kill

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_SIZE = (400 , 400)  # Adjusted for smaller cells
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Variable Grid")

# Set up the game clock
clock = pygame.time.Clock()

# Define the grid
grid_width = 9
grid_height = 9
cell_size = 16
grid = hunt_n_kill(grid_width, grid_height)

# Generate random colors for each cell
for x in range(0, grid_width*2-1, 1):
    for y in range(0,grid_height*2-1, 1):
        if grid[x][y]== 0:
            grid[x][y] = (0, 0 , 0)
        elif grid[x][y] == 1: 
            grid[x][y] = (254,255,255)
        else:
            grid[x][y]= (251, 185,255)

# Game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill((100, 100, 100))

    # Draw the grid
    for x in range(0, grid_width*2-1, 1):
        for y in range(0,grid_height*2-1, 1):
            cell = grid[x][y]
            cell_x, cell_y = x * cell_size, y * cell_size
            pygame.draw.rect(screen, cell, (cell_x, cell_y, cell_size, cell_size))

    # Update the screen
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)

# Quit Pygame
pygame.quit()