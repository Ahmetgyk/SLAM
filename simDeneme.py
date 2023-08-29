import pygame, sys
from pygame.locals import *

window = pygame.display.set_mode((640, 600))

red = (230, 30, 30)
blue = (30, 30, 230)
green = (20, 220, 10)

pygame.draw.line(window, red, (60, 60), (100, 60), 6)
pygame.draw.circle(window, blue, (100, 300), 10)
pygame.draw.line(window, green, (400, 400), (440, 490), 7)

window.set_at((300, 400), green)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()