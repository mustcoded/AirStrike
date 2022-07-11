from pygame import math as mt
from Objectpool import Objectpool

class Enemy1(object):

    def __init__(self, enemy_surface, x, y):

        self.on = True
        self.enemy_surface = enemy_surface
        self.x = x
        self.y = y
        self.hit = False
        self.direction = True
        self.y_direction = True
        self.enemy_pos = mt.Vector2(self.x, self.y)
        self.missile_count = 10
        self.missile_timer = 0
        self.missile_object_pool = Objectpool(self.missile_count)
        self.missile_list = []

    def update(self):

        if(self.direction == True):
            self.x += 0.1
        else:
            self.x -= 0.1

        if(self.y >= 160 and self.y_direction == True):
            self.y -= 0.1
        elif (self.y <= 250 and self.y_direction == False):
            self.y += 0.1

        if (self.y < 160):
            self.y_direction = False
        elif(self.y > 250):
            self.y_direction = True

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
                enemy_missile_manager.create_missile(self.x + 3, self.y + 100, self.missile_object_pool, self.missile_list)
                enemy_missile_manager.create_missile(self.x + 50, self.y + 100, self.missile_object_pool, self.missile_list)
                enemy_missile_manager.create_missile(self.x + 100, self.y + 100, self.missile_object_pool, self.missile_list)
            else:
                enemy_missile_manager.create_missile(self.x + 3, self.y + 100, None, self.missile_list)
                enemy_missile_manager.create_missile(self.x + 50, self.y + 100, None, self.missile_list)
                enemy_missile_manager.create_missile(self.x + 100, self.y + 100, None, self.missile_list)

        else:

            self.missile_timer += 1

