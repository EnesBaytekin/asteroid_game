from game.player import Player
from game.asteroid import Asteroid
from random import seed as set_seed
from random import randrange
from util import do_it_later
from math import atan2, sin, cos

class Game:
    def __init__(self):
        self.player = Player(5, 21)
        self.entities = [
            self.player,
            # Asteroid(4, 0, 2, 1, 1, 3),
        ]

        self.started = False
        self.started_at = 0
        self.wave_started_at = 0
        self.added_asteroid_count = 10
    def start_level(self, now, seed=None):
        if seed == None:
            seed = now
        set_seed(seed)
        self.started = True
        self.started_at = now
    def start_wave(self, now, screen):
        self.wave_started_at = now
        self.added_asteroid_count = 0
        def add_asteroid(asteroid):
            self.entities.append(asteroid)
            self.added_asteroid_count += 1
        for i in range(10):
            x = randrange(screen.width*2)-screen.width//2
            y = randrange(5)-6
            speed = randrange(4)+2
            direction = atan2((y-screen.height//2),(x-screen.width//2))
            dir_x = -cos(direction)
            dir_y = -sin(direction)
            radius = randrange(3)+2
            asteroid = Asteroid(x, y, speed, dir_x, dir_y, radius)
            spawn_time = i*(randrange(4)+2)
            do_it_later(add_asteroid, (asteroid, ), spawn_time)
    def draw(self, screen):
        # draw entities
        for entity in self.entities:
            entity.draw(screen)
        # draw border
        for x in range(screen.width):
            for y in range(screen.height):
                if x in (0, screen.width-1) or y in (0, screen.height-1):
                    screen.set_pixel(x, y, "#")
    def update(self, now, dt, key, screen):
        if self.started:
            if self.added_asteroid_count >= 10 and now-self.wave_started_at > 20:
                self.start_wave(now, screen)
            for entity in self.entities:
                if isinstance(entity, Player):
                    entity.update(now, dt, key, screen, self.entities)
                else:
                    entity.update(now, dt, screen, self.entities)
            for entity in self.entities:
                self.entities.extend(entity.get_new_objects())
                if not entity.is_alive():
                    self.entities.remove(entity)
