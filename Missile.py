from pygame import math as mt

class Missile(object):

    def __init__(self, missile_surface, x, y):
        self.on = True
        self.missile_surface = missile_surface
        self.x = x
        self.y = y
        self.missile_pos = mt.Vector2(self.x, self.y)

    def update(self):
        self.y -= 1
        self.missile_pos = mt.Vector2(self.x, self.y)