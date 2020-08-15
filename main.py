import pygame

from pygame.locals import *
from sys import exit

SCREEN_SIZE = (640, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
clock = pygame.time.Clock()

speed_x = 133
x = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    time_passed = clock.tick()
    
    time_passed_seconds = time_passed / 1000.0
    x += speed_x * time_passed_seconds
    
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (0, 0, 255), (int(x) + 10, 0 + 10), 10)

    pygame.display.flip()

pygame.quit()
