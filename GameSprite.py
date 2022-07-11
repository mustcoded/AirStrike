import pygame

class GameSprite(object):

    def __init__(self, image, rect):
        self.image = image
        self.rect = rect
        self.sprite = pygame.image.load(image).convert_alpha() #return a pygame surface object

    def getImage(self):  # this method will return a subsurface which is the child of the self.sprite surface
        return self.sprite.subsurface(self.rect)