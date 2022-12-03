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
        self.radius = 10

    def draw(self, surface):
        pygame.draw.circle(surface, black, (self.x, self.y), self.radius)

    def update(self, dx, dy):
        # keep the ball in the screen (hit edge)
        if (self.x <= 0 or self.x >= resolution[0]):
            dx = 0;
        if (self.y <= 0 or self.y >= resolution[1]):
            dy = 0;

        self.x += dx
        self.y += dy

def quit():
    pygame.quit()
    sys.exit()


screen = pygame.display.set_mode(resolution)
# FPS controller
clock = pygame.time.Clock()

ball = Ball(200, 150)
v_ball = 5

while True:
    screen.fill(white)

    # reset variables
    dx = 0
    dy = 0

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            print('Key has been pressed:', event.key)
            if event.key == pygame.K_UP:
                dy = -v_ball
            elif event.key == pygame.K_DOWN:
                dy = v_ball
            elif event.key == pygame.K_RIGHT:
                dx = v_ball
            elif event.key == pygame.K_LEFT:
                dx = -v_ball

    ball.draw(screen)
    ball.update(dx, dy)

    pygame.display.flip()
    clock.tick(60)

