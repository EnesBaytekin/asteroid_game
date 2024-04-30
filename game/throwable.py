from game.entity import *
from util import is_inside

class Throwable(Entity):
    def __init__(self, image, x, y, speed, dir_x, dir_y, damage, life_time=-1):
        super().__init__(image, x, y, speed, dir_x, dir_y, life_time)
        self.damage = damage
    def update(self, now, dt, screen, entities):
        super().update(now, dt, screen, entities)
        self_rect = self.image.get_rect_at(self.x, self.y)
        screen_rect = screen.image.get_rect_at(0, 0)
        if not is_inside(self_rect, screen_rect):
            self.die()
