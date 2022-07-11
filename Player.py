from pygame.locals import *
from GameSprite import GameSprite
from pygame import math as mt
from MissileManager import MissileManager
import pygame

class Player(object):

    def __init__(self, scene):

        self.image = 'Asset/player.png'
        self.scene = scene
        self.width = 40
        self.height = 40
        self.missile_count = 10
        self.direction_x = 0
        self.direction_y = 0
        self.rect = Rect(0, 0, self.width, self.height)
        self.sprite = GameSprite(self.image, self.rect)
        self.sprite_surface = self.sprite.getImage()  # get the player sprite surface
        self.bwidth, self.bheight = 660, 660
        self.pos = mt.Vector2(self.bwidth / 2, self.bheight / 2)  # initialize the position of the player sprite
        self.draw_pos = mt.Vector2(self.pos.x, self.pos.y)
        self.missile_manager = MissileManager(scene)

        pygame.display.set_icon(self.sprite_surface) # use the same player surface object as the icon for the game window

    def setX(self, _x):

        # set new x position and detect the boundary on the game scene
        self.direction_x = _x

    def setY(self, _y):

        # set new y position and detect the boundary on the game scene
        self.direction_y = _y

    def setStrike(self, strike):

        self.missile_manager.setStrike(strike)

    def update(self):

        if(self.direction_x == -0.1):
            if(self.pos.x > 0):
                self.pos.x += self.direction_x
        elif(self.direction_x == 0.1):
            if(self.pos.x + self.width <= self.bwidth):
                self.pos.x += self.direction_x
        if(self.direction_y == -0.1):
            if (self.pos.y > 0):
                self.pos.y += self.direction_y
        elif (self.direction_y == 0.1):
            if (self.pos.y + self.height <= self.bheight):
                self.pos.y += self.direction_y

        self.draw_pos = mt.Vector2(self.pos.x, self.pos.y)
        self.missile_manager.update(self.pos.x, self.pos.y)

    def get(self):
        return (self.pos.x, self.pos.y)


    def draw(self):
        self.scene.blit(self.sprite_surface,  self.draw_pos)
        self.missile_manager.draw()

    def getMissileManager(self):

        return self.missile_manager