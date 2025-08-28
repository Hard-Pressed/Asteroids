import pygame
from asteroid import Asteroid
from player import Player
import asteroidfield
from shot import Shot

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

    # Create sprite groups
    updatable_objects = pygame.sprite.Group(player)
    drawable_objects = pygame.sprite.Group(player)
    asteroid_objects = pygame.sprite.Group()
    shot_objects = pygame.sprite.Group()

    # Set up containers for Asteroid class
    Asteroid.asteroids = asteroid_objects
    Asteroid.updatables = updatable_objects
    Asteroid.drawables = drawable_objects

    # Set up containers for AsteroidField class
    asteroidfield.AsteroidField.containers = updatable_objects
    asteroidfield.asteroidfield_updatables = updatable_objects
    asteroidfield.Asteroid.containers = [asteroid_objects, updatable_objects, drawable_objects]

    # Set up containers for Shot class
    Shot.containers = [shot_objects, updatable_objects, drawable_objects]

    # Create asteroid field after containers are set
    asteroid_field = asteroidfield.AsteroidField()

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

        # Check collisions
            
        for asteroid in asteroid_objects:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return

        # Black screen
        screen.fill((0, 0, 0))

        # Draw all objects
        for drawable in drawable_objects:
            drawable.draw(screen)

        pygame.display.flip()

    

    pygame.quit()


if __name__ == "__main__":
    main()

