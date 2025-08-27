import pygame
from player import Player

pygame.init()

from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
dt = 0


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    updatable_objects = pygame.sprite.Group(player)
    drawable_objects = pygame.sprite.Group(player)

    global dt
    # Main game loop
    running = True
    while running:
        # Delta time
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update all objects
        updatable_objects.update(dt)

        # Black screen
        screen.fill((0, 0, 0))

        # Draw all objects
        for drawable in drawable_objects:
            drawable.draw(screen)

        pygame.display.flip()

    

    pygame.quit()


if __name__ == "__main__":
    main()

