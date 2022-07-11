from GameSprite import GameSprite
from pygame.locals import *
from Enemymissile import Enemymissile

class EnemyMissileManager(object):

    def __init__(self):

        self.image = 'Asset/e_missile.png'
        self.width = 20
        self.height = 20
        self.rect = Rect(0, 0, self.width, self.height)

        # initialize game sprite object
        self.sprite = GameSprite(self.image, self.rect)
        self.missile_surface = self.sprite.getImage()

    def create_missile(self, x, y, pool, missile_list):
        if(pool == None):
            missile_list.append(Enemymissile(self.missile_surface, x, y))
        else:
            missile_list.append(pool.obtain_missile(x, y))