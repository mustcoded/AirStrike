from Enemy import Enemy
from GameSprite import GameSprite
from pygame.locals import *
from EnemyMissileManager import EnemyMissileManager
import random
from Objectpool import Objectpool
from Enemy1 import Enemy1

class EnemyManager(object):

    def __init__(self, scene, player, game_level):

        self.enemy_missile_manager = EnemyMissileManager()
        self.scene = scene
        self.player = player
        self.enemy_count = 10
        self.horizontal_enemy_count = 1
        self.missile_count = 60
        self.enemy_list = []
        self.horizontal_enemy_list = []
        self.image = 'Asset/enemy0.png'
        self.image1 =  'Asset/enemy1.png'
        self.image2 = 'Asset/enemy2.png'
        self.width = 30
        self.height = 30
        self.width1 = 130
        self.height1 = 130
        self.rect = Rect(0, 0, self.width, self.height)
        self.rect1 = Rect(0, 0, self.width1, self.height1)
        self.more_enemy = 0
        self.y = -50
        self.boundary_width = 660
        self.boundary_height = 660
        self.object_pool = Objectpool(self.enemy_count)
        self.horizontal_object_pool = Objectpool(self.horizontal_enemy_count)
        self.next_enemy = 0
        self.level = game_level

        # initialize game sprite object
        self.sprite = GameSprite(self.image, self.rect)
        self.sprite1 = GameSprite(self.image1, self.rect)
        self.sprite2 = GameSprite(self.image2, self.rect1)

    def create_enemy(self, x, y):

        if(self.enemy_count > 0):

            if(self.object_pool.getSize() > 0): # get the ship from object pool if the pool is not empty
                self.enemy_list.append(self.object_pool.obtain())
            else: # objects setup based on the level of the game
                if(self.level == 1):
                    self.enemy_surface = self.sprite.getImage()
                elif(self.level == 2 or self.level == 3):
                    if(self.next_enemy == 0):
                        self.enemy_surface = self.sprite.getImage()
                        self.next_enemy += 1
                    elif(self.next_enemy == 1):
                        self.enemy_surface = self.sprite1.getImage()
                        self.next_enemy = 0
                self.enemy_list.append(Enemy(self.enemy_surface, x, y))
            self.enemy_count -= 1

    def create_horizontal_enemy(self, x, y):

        if (self.horizontal_enemy_count > 0):

            if (self.horizontal_object_pool.getSize() > 0):  # get the ship from object pool if the pool is not empty
                self.horizontal_enemy_list.append(self.horizontal_object_pool.obtain())
            else:  # objects setup based on the level of the game
                if (self.level == 3):
                    self.enemy_surface1 = self.sprite2.getImage()
                self.horizontal_enemy_list.append(Enemy1(self.enemy_surface1, x, y))
            self.horizontal_enemy_count -= 1


    def update(self):

        if (self.level == 1 or self.level == 2):

            if (self.more_enemy > 600):
                self.more_enemy = 0
                x = random.randint(30, self.boundary_width - 50)
                self.create_enemy(x , self.y)  # create more enemy
            else:
                self.more_enemy += 1 # increase time

        elif(self.level == 3):

            if (self.more_enemy > 600):
                self.more_enemy = 0
                x = random.randint(30, self.boundary_width - 50)
                self.create_enemy(x , self.y)  # create more enemy
            else:
                self.more_enemy += 1 # increase time

            if(self.horizontal_enemy_count > 0):
                self.create_horizontal_enemy(-130, 200)  # create new enemy

        self.create_enemy_missile()
        self.enemy_update()
        self.check_boundary()

    def create_enemy_missile(self):

        for item in list(self.enemy_list):

            if(self.player.pos.y - item.y  < 200 and abs(self.player.pos.x - item.x) < 160):

                item.create_enemy_missile(self.enemy_missile_manager)

        if(self.level == 3):

            for item in list(self.horizontal_enemy_list):
                item.create_enemy_missile(self.enemy_missile_manager)

    def enemy_update(self):

        for item in list(self.enemy_list):

            if(item.on == False):
                self.enemy_list.remove(item)
                self.enemy_count += 1
                item.y = self.y
                item.on = True
                self.object_pool.recycle(item)
            else:
                if ((self.player.pos.y - item.y < 200 and self.player.pos.y - item.y > -2) and abs(self.player.pos.x - item.x) < 200):
                    item.update((self.player.pos.x - item.x) * 0.004, 0.2)
                else:
                    item.update(0, 0.2)

        if (self.level == 3):

            for item in list(self.horizontal_enemy_list):

                if (item.on == False):

                    self.horizontal_enemy_count += 1
                    item.y = 220

                    if(item.direction == True):
                        item.x = 800
                        item.direction = False
                    else:
                        item.x = -130
                        item.direction = True
                    self.horizontal_enemy_list.remove(item)
                    item.on = True
                    self.horizontal_object_pool.recycle(item)

                else:
                    item.update()

    # check the boundary of the enemy ship with the game scene area
    def check_boundary(self):

        for i in range(len(self.enemy_list)):
            if (self.enemy_list[i].y > self.boundary_height):
                self.enemy_list[i].on = False

        if (self.level == 3):
            for i in range(len(self.horizontal_enemy_list)):
                if (self.horizontal_enemy_list[i].x > self.boundary_width):
                    self.horizontal_enemy_list[i].direction = False
                elif(self.horizontal_enemy_list[i].x <= -130):
                    self.horizontal_enemy_list[i].direction = True

    def draw(self):

        # blit the enemy and enemy missiles on  the scene
        for i in range(len(self.enemy_list)):
            self.scene.blit(self.enemy_list[i].enemy_surface, self.enemy_list[i].enemy_pos)
            self.enemy_list[i].missile_draw(self.scene)

        if(self.level == 3):
            for i in range(len(self.horizontal_enemy_list)):
                self.scene.blit(self.horizontal_enemy_list[i].enemy_surface, self.horizontal_enemy_list[i].enemy_pos)
                self.horizontal_enemy_list[i].missile_draw(self.scene)
