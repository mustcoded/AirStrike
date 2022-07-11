from BgSprite import BgSprite
from pygame.locals import *
from pygame import math as mt

class Background(object):

    def __init__(self, scene):
        self.scene = scene
        self.image = 'Asset/bg1.png'
        self.rect = Rect(0, 0, 660, 660)
        self.sprite = BgSprite(self.image, self.rect)
        self.surface = self.sprite.getImage()  # get the background sprite surface
        self.draw_pos = mt.Vector2(0, 0)

    def draw(self):
        self.scene.blit( self.surface, self.draw_pos) # draw a background sprite
