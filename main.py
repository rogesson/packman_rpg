import pygame

from pygame.locals import *
import sys
from vector2 import *
from character import *

def main():
    SCREEN_SIZE = (640, 480)

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
    clock = pygame.time.Clock()

    hero = Character(0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        time_passed = clock.tick()
        
        time_passed_seconds = time_passed / 1000.0
        
        screen.fill((0, 0, 0))

        pressed_keys = pygame.key.get_pressed()

        direction = None
        if pressed_keys[K_LEFT]:
            direction = "left"
        elif pressed_keys[K_RIGHT]:
            direction = "right"
        elif pressed_keys[K_UP]:
            direction = "up"
        elif pressed_keys[K_DOWN]:
            direction = "down"

        if direction:
            hero.walk(direction, time_passed_seconds)

        pygame.draw.circle(screen, (0, 0, 255), (int(hero.x) + 10, int(hero.y) + 10), 10)

        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()
