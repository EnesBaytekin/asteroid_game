class Entity:
    def __init__(self, image, x, y, speed, dir_x, dir_y, life_time=-1):
        self.x = x
        self.y = y
        self.x_old = x
        self.y_old = y
        self.direction_x = dir_x
        self.direction_y = dir_y
        self.speed = speed
        self.image = image
        self.born_at = -1
        self.life_time = life_time
        self.new_objects = []
        self.alive = True
    def is_alive(self):
        return self.alive
    def die(self):
        self.alive = False
    def spawn_object(self, *objects):
        self.new_objects.extend(objects)
    def get_new_objects(self):
        new_objects = self.new_objects.copy()
        self.new_objects.clear()
        return new_objects
    def move(self, dx, dy):
        self.x_old = self.x
        self.y_old = self.y
        self.x += dx
        self.y += dy
    def unmove(self):
        self.x = self.x_old
        self.y = self.y_old
    def draw(self, screen):
        screen.paste(self.image, int(self.x), int(self.y))
    def update(self, now, dt, screen, entities):
        if self.born_at == -1:
            self.born_at = now
        if self.life_time != -1 and now-self.born_at >= self.life_time:
            self.die()
        dx = self.direction_x*self.speed*dt
        dy = self.direction_y*self.speed*dt
        self.move(dx, dy)
