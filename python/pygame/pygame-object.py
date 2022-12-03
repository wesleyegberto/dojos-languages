import sys
import pygame
from pygame.locals import *

resolution = (400, 300)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

class Ball:
    def __init__(self, x, y):
        # pygame uses it
        self.type = 'BALL'
        self.x = x
        self.y = y
        self.dx = 1
        self.dy = 1
        self.radius = 10

    def draw(self, surface):
        pygame.draw.circle(surface, black, (self.x, self.y), self.radius)

    def update(self):
        # keep the ball in the screen (hit edge)
        if (self.x <= 0 or self.x >= resolution[0]):
            self.dx *= -1;
        if (self.y <= 0 or self.y >= resolution[1]):
            self.dy *= -1;

        self.x += self.dx
        self.y += self.dy

screen = pygame.display.set_mode(resolution)
# FPS controller
clock = pygame.time.Clock()

ball = Ball(200, 150)

while True:
    screen.fill(white)

    ball.draw(screen)
    ball.update()

    pygame.display.flip()
    # controls the FPS
    clock.tick(60)

    # handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

