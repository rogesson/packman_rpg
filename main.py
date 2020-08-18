import pygame

from pygame.locals import *
import sys
from vector2 import *
from character import *

def main():
    SCREEN_SIZE = (640, 480)

    pygame.init()
    pygame.display.set_caption("Pack-Man RPG")
    screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
    clock = pygame.time.Clock()

    hero = Character(0, 0)

    hero_skin = pygame.Surface((32, 32))
    hero_skin.fill((255, 255, 255))
    wall_skin = pygame.Surface((32, 32))
    wall_skin.fill((255, 0, 0))

    path = pygame.Surface((32, 32))
    path.fill((0, 255, 0))

    walls = [
            [False, False, False, False, False,  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [True,  True,  True,  True,  False, False,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True ],
            [False, False, False, True,  True,  True, True, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    ]

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

        for y, wall in enumerate(walls):
            for x, w in enumerate(wall):
                position = (x * 32, y * 32)
                hpos = hero.position()

                if w is True:
                    position = (x * 32, y * 32)
                    screen.blit(path, position)
                    continue
                screen.blit(wall_skin, position)

        screen.blit(hero_skin, (hero.x, hero.y))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
