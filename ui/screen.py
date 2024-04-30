from os import system
from images.image import *
from random import random, randrange

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image(self.width, self.height)
        self.background = self.create_background()
    def create_background(self):
        width = self.width
        height = self.height*4
        grid = [ [ " " for x in range(width) ] for y in range(height) ]
        for y in range(height):
            for x in range(width):
                if x%4 == 0 and y%4 == 0:
                    if random() < 0.3:
                        dx = randrange(3)-1
                        dy = randrange(3)-1
                        if x+dx in range(width) and y+dy in range(height):
                            grid[y+dy][x+dx] = "*"
        return Image.from_grid(grid)
    def draw_background(self, now):
        y = int(now*15)%self.background.height
        self.paste(self.background, 0, y-self.background.height)
        self.paste(self.background, 0, y)
    def clear(self):
        self.image.grid = [ [ " " for y in range(self.height)] for x in range(self.width) ]
    def set_pixel(self, x, y, pixel):
        self.image.grid[x][y] = pixel
    def paste(self, image, x, y):
        image.draw_onto(self.image, x, y)
    def update(self):
        system("cls")
        for y in range(self.height):
            for x in range(self.width):
                print(self.image.grid[x][y], end="")
            print()