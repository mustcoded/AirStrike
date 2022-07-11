from pygame import math as mt
from pygame.locals import *

class Explosion(object):

    def __init__(self, ex_surface, x, y):
        self.on = True
        self.ex_surface = ex_surface
        self.x = x
        self.y = y
        self.ex_pos = mt.Vector2(self.x, self.y)
        self.count = 0
        self.width = 64
        self.height = 64
        self.rect = Rect(self.count * self.width, 0, self.width, self.height)
        self.timer = 0

    def update(self):

        if(self.count <= 9):

            if(self.timer > 16):
                self.count += 1
                self.rect = Rect(self.count * self.width, 0, self.width, self.height)
                self.ex_pos = mt.Vector2(self.x, self.y)
                self.timer = 0
            else:
                self.timer += 1
        else:
            self.count = 0
            self.on = False
            self.timer = 0
            self.rect = Rect(self.count * self.width, 0, self.width, self.height)
