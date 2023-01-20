import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math

# Initialize Pygame
pygame.init()

# Set the screen size
size = (700, 500)
screen = pygame.display.set_mode(size, DOUBLEBUF|OPENGL)

# Set the title of the window
pygame.display.set_caption("Galaxy Simulator")

# Define the properties of a star
class Star:
    def __init__(self, position, size, color):
        self.position = position
        self.size = size
        self.color = color

    # Update the position of the star
    def update(self, dt):
        self.position[0] += 0.1 * dt
        self.position[1] += 0.1 * dt 


# Create an empty list to hold the stars
stars = []

# Create a random number of stars
num_stars = 1000
for i in range(num_stars):
    # Generate a random angle
    angle = random.uniform(0, 2 * math.pi)

    # Generate a random distance from the center
    distance = random.uniform(0.1, 1)

    # Convert the polar coordinates to Cartesian coordinates
    x = distance * math.cos(angle)
    y = distance * math.sin(angle)
    z = 0
    position = [x, y, z]

    # Generate a random size and color for the star
    size = random.uniform(0.1, 0.5)
    color = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]

    # Create a new star object and add it to the list
    stars.append(Star(position, size, color))

# Set the frame rate
clock = pygame.time.Clock()

# Run the game loop
running = True
while running:
    dt = clock.tick(30) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the position of each star
    for star in stars:
        star.update(dt)

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw the stars
    for star in stars:
        glColor3f(*star.color)
        glPointSize(star.size)
        glBegin(GL_POINTS)
        glVertex3f(*star.position)
        glEnd()

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
