from game.throwable import *
from images import *

class Laser(Throwable):
    def __init__(self, x, y, speed, dir_x, dir_y, damage, life_time=-1):
        super().__init__(IMAGES[IMAGE.LASER], x, y, speed, dir_x, dir_y, damage, life_time)
