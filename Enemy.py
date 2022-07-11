from pygame import math as mt
from Objectpool import Objectpool

class Enemy(object):

    def __init__(self, enemy_surface, x, y):

        self.on = True
        self.enemy_surface = enemy_surface
        self.x = x
        self.y = y
        self.hit = False
        self.enemy_pos = mt.Vector2(self.x, self.y)
        self.missile_count = 10
        self.missile_timer = 0
        self.missile_object_pool = Objectpool(self.missile_count)
        self.missile_list = []

    def update(self, x, y):
        self.y += y
        self.x += x
        self.enemy_pos = mt.Vector2(self.x, self.y)
        self.missile_update(self.missile_object_pool)

    def missile_update(self, pool):

        for item in list(self.missile_list):
            if (item.on == False):
                self.missile_list.remove(item)
                pool.recycle(item)
            else:
                item.update()

    def missile_draw(self, scene): # draw enemy missiles on game scene
        for item in list(self.missile_list):
            scene.blit(item.missile_surface, item.missile_pos)


    def create_enemy_missile(self, enemy_missile_manager):

        if(self.missile_timer > 300):

            self.missile_timer = 0

            if (self.missile_object_pool.getSize() > 0):
                enemy_missile_manager.create_missile(self.x + 5, self.y + 4, self.missile_object_pool, self.missile_list)
            else:
                enemy_missile_manager.create_missile(self.x + 5, self.y + 4, None, self.missile_list)

        else:

            self.missile_timer += 1

