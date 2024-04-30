from game.entity import *
from game.bullet import *
from game.laser import *
from images import *
from controller import KEYS
from util import is_inside, do_it_later

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(IMAGES[IMAGE.PLAYER], x, y, 16, 0, 0)

        self.shoot_cooldown = 0.2
        self.last_shot_at = 0

        self.is_using_skill = False
        self.skill_number = 1

        self.skill1_started_at = 0
        self.skill2_started_at = 0

        self.skill1_duration = 1
        self.skill2_duration = 2

        self.skill1_cooldown = 5
        self.skill2_cooldown = 5

        self.score = 0
    def add_score(self, amount):
        self.score += amount
    def update(self, now, dt, key, screen, entities):
        # check keys
        if key == KEYS.RIGHT:
            self.direction_x = 1
        elif key == KEYS.DOWN:
            self.direction_x = 0
        elif key == KEYS.LEFT:
            self.direction_x = -1
        elif key == KEYS.SHOOT:
            if not self.is_using_skill:
                if now-self.last_shot_at >= self.shoot_cooldown:
                    self.last_shot_at = now
                    self.spawn_object(Bullet(self.x, self.y-1, 20, 0, -1, 3))
        elif key == KEYS.SKILL_1:
            if not self.is_using_skill:
                if now-self.skill1_started_at >= self.skill1_duration+self.skill1_cooldown:
                    self.skill_number = 1
                    self.skill1_started_at = now
                    self.is_using_skill = True
        elif key == KEYS.SKILL_2:
            if not self.is_using_skill:
                if now-self.skill2_started_at >= self.skill2_duration+self.skill2_cooldown:
                    self.skill_number = 2
                    self.skill2_started_at = now
                    self.is_using_skill = True
                    shot_count = 4
                    for i in range(shot_count):
                        def spawn_line():
                            for y in range(int(self.y)):
                                self.spawn_object(Laser(self.x, y, 0, 0, 0, 2, self.skill2_duration/(shot_count*2)))
                        do_it_later(spawn_line, (), self.skill2_duration*i/shot_count)
        # check skills
        if self.is_using_skill:
            if self.skill_number == 1:
                if now-self.skill1_started_at < self.skill1_duration:
                    self.spawn_object(Bullet(self.x, self.y-1, 20, 0, -1, 2))
                else:
                    self.is_using_skill = False
            elif self.skill_number == 2:
                if now-self.skill2_started_at < self.skill2_duration:
                    pass
                else:
                    self.is_using_skill = False
        # move
        super().update(now, dt, screen, entities)
        self_rect = self.image.get_rect_at(self.x, self.y)
        screen_rect = screen.image.get_rect_at(0, 0)
        if not is_inside(self_rect, screen_rect):
            self.unmove()
