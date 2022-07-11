import pygame.font as txt
from pygame.locals import *
from BgSprite import BgSprite
from pygame import math as mt

class Score(object):

    def __init__(self, scene, l_m):

        self.score = 0
        self.scene = scene
        self.rect = Rect(20,20, 100, 30)
        self.font = txt.Font('Asset/ft.ttf', 30)
        self.score_text = "Score : " + str(self.score)
        self.level_manager = l_m

        #power bar setup

        self.power = 'Asset/power.png'
        self.power_rect = Rect(0, 0, 40, 100)
        self.power_sprite = BgSprite(self.power, self.power_rect)
        self.power_surface = self.power_sprite.getImage()
        self.draw_power_pos = mt.Vector2(600, 540)
        self.power_y = 0
        self.o_p = 100

    def set_score(self, score):

        self.score += score

        if(score < 0):
            self.power_y += 1
            self.draw_power_pos = mt.Vector2(600, 550 - self.power_y)
            self.power_rect = Rect(0, self.power_y, 40, self.o_p - self.power_y)
            self.power_sprite = BgSprite(self.power, self.power_rect)
            self.power_surface = self.power_sprite.getImage()

        self.score_text = " Score : " + str(self.score)

    def draw(self):
        self.level_text = "         Level " + str(self.level_manager.get_level())
        self.text = self.font.render(self.score_text+self.level_text, 1, (255, 255, 255))
        self.scene.blit(self.text, self.rect)

        self.scene.blit(self.power_surface, self.draw_power_pos)