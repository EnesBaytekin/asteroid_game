from game.entity import *
from game.throwable import *
from game.particle import *
from images import *
from util import collide_rect

class Asteroid(Entity):
    def __init__(self, x, y, speed, dir_x, dir_y, radius):
        image = self.create_image(radius)
        super().__init__(image, x, y, speed, dir_x, dir_y, -1)
        self.radius = radius
        self.health = radius*20
        self.value = radius*351
    def create_image(self, radius):
        grid = []
        for x in range(-radius, radius+1):
            grid.append([])
            for y in range(-radius, radius+1):
                if (radius-0.5)**2 <= x**2+y**2 <= (radius+0.5)**2:
                    grid[-1].append("@")
                else:
                    grid[-1].append(" ")
        return Image.from_grid(grid, radius, radius)
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()
            #self.spawn_object(Particle.create_explosion(self.x, self.y))
        else:
            self.radius = (int(self.health)//20)+1
            self.image = self.create_image(self.radius)
    def update(self, now, dt, screen, entities):
        super().update(now, dt, screen, entities)
        player = entities[0]
        self_rect = self.image.get_rect_at(self.x, self.y)
        for entity in entities:
            if entity == self: continue
            entity_rect = entity.image.get_rect_at(entity.x, entity.y)
            if collide_rect(self_rect, entity_rect):
                if isinstance(entity, Throwable):
                    self.take_damage(entity.damage)
                    entity.die()
                    player.add_score(entity.damage*13)
                    if not self.alive:
                        player.add_score(self.value)
