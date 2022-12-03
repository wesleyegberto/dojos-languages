import pygame
from pygame.locals import *

resolution = (400, 300)

# RGB
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# initialize the screen
screen = pygame.display.set_mode(resolution)

# game loop
while True:
    screen.fill(white)

    pygame.display.flip()

    # handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

