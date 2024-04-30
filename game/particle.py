from game.entity import Entity
from images import *
from math import pi, sin, cos

class Particle(Entity):
    def __init__(self, x, y, speed, dir_x, dir_y, life_time=-1):
        super().__init__(IMAGES[IMAGE.PARTICLE], x, y, speed, dir_x, dir_y, life_time)
    @classmethod
    def create_explosion(cls, x, y):
        particles = []
        for i in range(12):
            speed = 4
            dir = i*2*pi
            dir_x = cos(dir)
            dir_y = sin(dir)
            life_time = -1
            particle = cls(x, y, speed, dir_x, dir_y, life_time)
            particles.append(particle)
        return particles
    def update(self, now, dt, screen, entities):
        super().update(now, dt, screen, entities)
        self.speed -= dt
        if self.speed <= 0:
            self.die()
