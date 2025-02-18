import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        old_radius = self.radius
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        smaller1 = Asteroid(self.position.x, self.position.y, (old_radius - ASTEROID_MIN_RADIUS))
        smaller2 = Asteroid(self.position.x, self.position.y, (old_radius - ASTEROID_MIN_RADIUS))
        smaller1.velocity = self.velocity.rotate(random_angle) * 1.2
        smaller2.velocity = self.velocity.rotate(-random_angle) * 1.2