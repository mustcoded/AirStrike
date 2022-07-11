from Missile import Missile
from GameSprite import GameSprite
from pygame.locals import *
from Objectpool import Objectpool

class MissileManager(object):

    def __init__(self, scene):
        self.scene = scene
        self.missile_count = 10
        self.missile_list = []
        self.image = 'Asset/missile.png'
        self.width = 20
        self.height = 20
        self.rect = Rect(0, 0, self.width, self.height)
        self.strike = False
        self.strike_again = 0
        self.missile_object_pool = Objectpool(self.missile_count)
        # initialize game sprite object
        self.sprite = GameSprite(self.image, self.rect)

    def setStrike(self, strike):

        # set the missile strike flag
        self.strike = strike
        self.strike_again += 1

    def create_missile(self, x, y):
        if(self.missile_count >= 0):

            if (self.missile_object_pool.getSize() > 0):
                self.missile_list.append(self.missile_object_pool.obtain_missile(x, y))
            else:
                self.missile_surface = self.sprite.getImage()
                self.missile_list.append(Missile(self.missile_surface, x, y))
            self.missile_count -= 1

    def update(self,x,y):
        if (self.strike == True and self.strike_again > 1):
            self.strike_again = 0
            self.create_missile(x + 5, y - 8)  # create more missile
        self.missile_update()
        self.check_boundary()

    def missile_update(self):

        for item in list(self.missile_list):
            if(item.on == False):
                self.missile_list.remove(item)
                self.missile_count += 1
                self.missile_object_pool.recycle(item)
            else:
                item.update()

    def check_boundary(self):

        for i in range(len(self.missile_list)):
            if (self.missile_list[i].y < 0):
                self.missile_list[i].on = False

    def draw(self):

        # blit the missile on  the scene
        for i in range(len(self.missile_list)):
            self.scene.blit(self.missile_list[i].missile_surface, self.missile_list[i].missile_pos)