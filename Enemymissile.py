from pygame import math as mt

class Enemymissile(object):

    def __init__(self, missile_surface, x, y):
        self.on = True
        self.missile_surface = missile_surface
        self.x = x
        self.y = y
        self.height = 20
        self.width = 20
        self.missile_pos = mt.Vector2(self.x, self.y)

    def update(self):

        self.y += 1
        self.missile_pos = mt.Vector2(self.x, self.y)

        if(self.y > 660):
            self.on = False

    def draw(self, scene):
        scene.blit(self.missile_surface, self.missile_pos)