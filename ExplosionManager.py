from pygame.locals import *
from GameSprite import GameSprite
from Objectpool import Objectpool
from Explosion import Explosion

class ExplosionManager(object):

    def __init__(self, scene):

        self.image = 'Asset/explosion.png'
        self.scene = scene
        self.width = 640
        self.height = 64
        self.explosion_count = 10
        self.count = 0
        self.rect = Rect(0, 0, self.width, self.height)
        self.sprite = GameSprite(self.image, self.rect)
        self.sprite_surface = self.sprite.getImage()  # get the player sprite surface
        self.explosion_object_pool = Objectpool(self.explosion_count)
        self.explosion_list = []

    def create_explosion(self, x, y):

        if (self.explosion_object_pool.getSize() > 0):
            self.explosion_list.append(self.explosion_object_pool.obtain_missile(x, y))
        else:
            self.explosion_list.append(Explosion(self.sprite_surface, x, y))

    def explosion_update(self):

        for item in list(self.explosion_list):
            if(item.on == False):
                self.explosion_list.remove(item)
                self.explosion_object_pool.recycle(item)
            else:
                item.update()

    def draw(self):

        # blit the explosion on  the scene
        for i in range(len(self.explosion_list)):
            self.scene.blit(self.explosion_list[i].ex_surface, self.explosion_list[i].ex_pos, self.explosion_list[i].rect)