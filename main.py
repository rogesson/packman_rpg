import pygame

from pygame.locals import *
import sys
from vector2 import *

def main():
    SCREEN_SIZE = (640, 480)

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
    clock = pygame.time.Clock()
    
    x = 0
    y = 0
    speed = 133

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        time_passed = clock.tick()
        
        time_passed_seconds = time_passed / 1000.0
        #x += speed * time_passed_seconds
        
        screen.fill((0, 0, 0))

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            x -= speed * time_passed_seconds

        if pressed_keys[K_RIGHT]:
            x += speed * time_passed_seconds

        if pressed_keys[K_UP]:
            y -= speed * time_passed_seconds

        if pressed_keys[K_DOWN]:
            y += speed * time_passed_seconds

        pygame.draw.circle(screen, (0, 0, 255), (int(x) + 10, int(y) + 10), 10)

        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()
