import sys
import pygame
from tree import *

black = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((700, 600))
screen.fill(black)


class Ball(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.top = []
        self.bottom = []
        self.left = []
        self.right = []
        self.speed = None

    def check_collision(self):
        pass


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            color = (255, 255, 255)

    pygame.display.flip()
