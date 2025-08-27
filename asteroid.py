import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    asteroids = None
    updatables = None
    drawables = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        if Asteroid.asteroids:
            Asteroid.asteroids.add(self)
        if Asteroid.updatables:
            Asteroid.updatables.add(self)
        if Asteroid.drawables:
            Asteroid.drawables.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt