from BgSprite import BgSprite
from GameSprite import GameSprite
from pygame.locals import *
from pygame import math as mt
import pygame

class Scene(object):

    def __init__(self, scene):

        self.scene = scene
        self.screen_folder = 'Screen/'
        self.next_button = 'Screen/right_arrow.png'
        self.previous_button = 'Screen/left_arrow.png'
        self.home_button = 'Asset/back.png'

        self.bg_rect = Rect(0, 0, 660, 660)
        self.next_button_rect = Rect(0, 0,  30, 30)
        self.previous_button_rect = Rect(0, 0, 30, 30)
        self.home_button_rect = Rect(0, 0, 40, 30)
        self.count = 0
        self.next = 1
        self.open_file()
        self.setup()

        self.previous_button_sprite = GameSprite(self.previous_button, self.previous_button_rect)
        self.next_button_sprite = GameSprite(self.next_button, self.next_button_rect)
        self.sprite_home_button = GameSprite(self.home_button, self.home_button_rect)


        self.previous_button_surface = self.previous_button_sprite.getImage() # get the button sprite surface
        self.next_button_surface = self.next_button_sprite.getImage()  # get the button sprite surface
        self.home_button_surface = self.sprite_home_button.getImage()  # get the button sprite surface

        self.draw_pos = mt.Vector2(0, 0)
        self.draw_next_button_pos = mt.Vector2(610, 330)
        self.draw_previous_button_pos = mt.Vector2(50, 330)
        self.draw_home_button_pos = mt.Vector2(10, 620)

    def open_file(self):

        try:
            f = open("Screen/count.txt", "r")

            try:
                if f.mode == 'r':
                    self.f1 = f.readlines()
                    for x in self.f1:
                        self.count = int(x)
            finally:
                f.close()


        except IOError:
            print('Error')

    def setup(self):

        if(self.count > 0):
            self.general_image = 'Screen/' + str(self.next) + 'game.png'
        else:
            self.general_image = 'Asset/general.png'

        self.screen_sprite = BgSprite(self.general_image, self.bg_rect)
        self.screen_surface = self.screen_sprite.getImage()  # get the screen sprite surface


    def take_screen(self): # take screenshot
        self.count += 1
        self.file_path = 'Screen/' + str(self.count) + 'game.png'
        pygame.image.save(self.scene, self.file_path)
        self.save_file()

    def save_file(self):
        try:

            f = open("Screen/count.txt", "w+")
            try:
                f.write(str(self.count))
            finally:
                f.close()
        except IOError:
            print('cannot save a file')

    def set_next_image(self):

        self.next += 1
        if(self.next > self.count):
            self.next = self.count

        self.setup()

    def set_previous_image(self):

        self.next -= 1

        if(self.next <= 0):
            self.next = 1

        self.setup()

    def draw(self):

        self.scene.blit(self.screen_surface, self.draw_pos)  # draw a game scene sprite
        self.scene.blit(self.previous_button_surface, self.draw_previous_button_pos)  # draw a button sprite
        self.scene.blit(self.next_button_surface, self.draw_next_button_pos)  # draw a button sprite
        self.scene.blit(self.home_button_surface, self.draw_home_button_pos)  # draw a button sprite

        pygame.display.flip()