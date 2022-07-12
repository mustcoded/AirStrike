from BgSprite import BgSprite
from GameSprite import GameSprite
from pygame.locals import *
from pygame import math as mt
import pygame
import pygame.font as txt
from AirStrikeColor import AirStrikeColor

class StartScene(object):

    def __init__(self, scene, lm):

        self.level_manager = lm

        self.scene = scene
        self.play_button = 'Asset/play.png'
        self.about_button  = 'Asset/about.png'
        self.exit_button = 'Asset/exit.png'
        self.scene_button = 'Asset/scene.png'
        self.score_button = 'Asset/score.png'
        self.home_button = 'Asset/back.png'
        self.button_image = 'Asset/button_play.png'
        self.manual_button = 'Asset/manual.png'
        self.bg_image = 'Asset/start.png'
        self.win_image = 'Asset/winn.png'
        self.general_image = 'Asset/general.png'


        self.soundon = 'Asset/sound.png'
        self.soundoff = 'Asset/soundoff.png'
        self.home_button_image = 'Asset/home.png'
        self.game_logo = 'Asset/enemy3.png'
        self.bg_rect = Rect(0, 0, 660, 660)
        self.button_rect = Rect(0, 0,  306, 112)
        self.home_button_rect = Rect(0, 0, 200, 53)
        self.back_button_rect = Rect(0, 0, 40, 30)
        self.sound_button_rect = Rect(0, 0, 30, 30)
        self.game_logo_rect = Rect(0, 0, 160, 160)

        self.sprite = BgSprite(self.general_image, self.bg_rect)


        self.sprite_win = BgSprite(self.win_image, self.bg_rect)

        self.sprite_pause = BgSprite(self.general_image, self.bg_rect)

        self.soundon_button = GameSprite(self.soundon, self.sound_button_rect)
        self.soundoff_button = GameSprite(self.soundoff, self.sound_button_rect)

        self.soundoff_button_surface = self.soundoff_button.getImage()  # get the button sprite surface
        self.soundon_button_surface = self.soundon_button.getImage()  # get the button sprite surface
        self.game_logo_sprite = GameSprite(self.game_logo, self.game_logo_rect)
        self.sprite_button = GameSprite(self.button_image, self.button_rect)
        self.sprite_home_pause_button = GameSprite(self.home_button_image, self.home_button_rect)
        self.sprite_scene_button = GameSprite(self.scene_button, self.home_button_rect)
        self.sprite_manual_button = GameSprite(self.manual_button, self.home_button_rect)
        self.sprite_exit_button = GameSprite(self.exit_button, self.home_button_rect)
        self.sprite_play_button = GameSprite(self.play_button, self.home_button_rect)
        self.sprite_about_button = GameSprite(self.about_button, self.home_button_rect)
        self.sprite_score_button = GameSprite(self.score_button, self.home_button_rect)
        self.sprite_home_button = GameSprite(self.home_button, self.back_button_rect)


        self.win_surface = self.sprite_win.getImage()  # get the win sprite surface
        self.pause_surface = self.sprite_pause.getImage()  # get the pause sprite surface
        self.surface = self.sprite.getImage()  # get the start scene sprite surface
        self.button_surface = self.sprite_button.getImage() # get the button sprite surface
        self.home_pause_button_surface = self.sprite_home_pause_button.getImage() # get the button sprite surface
        self.play_button_surface = self.sprite_play_button.getImage()  # get the button sprite surface
        self.about_button_surface = self.sprite_about_button.getImage()  # get the button sprite surface
        self.score_button_surface = self.sprite_score_button.getImage()  # get the button sprite surface
        self.manual_button_surface = self.sprite_manual_button.getImage()  # get the button sprite surface
        self.scene_button_surface = self.sprite_scene_button.getImage()  # get the button sprite surface
        self.home_button_surface = self.sprite_home_button.getImage()  # get the button sprite surface
        self.exit_button_surface = self.sprite_exit_button.getImage()  # get the button sprite surface
        self.game_logo_surface = self.game_logo_sprite.getImage() # get game logo image
        self.draw_pos = mt.Vector2(0, 0)
        self.draw_button_pos = mt.Vector2(177, 274)
        self.draw_game_logo_pos = mt.Vector2(246, 60)
        self.draw_play_button_pos = mt.Vector2(229, 200)
        self.draw_about_button_pos = mt.Vector2(229, 263)
        self.draw_home_button_pos = mt.Vector2(229, 263)
        self.draw_score_button_pos = mt.Vector2(229, 328)
        self.draw_manual_button_pos = mt.Vector2(229, 393)
        self.draw_exit_button_pos = mt.Vector2(229, 456)
        self.draw_scene_button_pos = mt.Vector2(229, 519)
        self.draw_back_button_pos = mt.Vector2(10, 620)

        self.draw_sound_button_pos = mt.Vector2(10, 620)

        self.soundon = True
        self.count = 0

        self.font = txt.Font('Asset/ft.ttf', 90)
        self.credit_font = txt.Font('Asset/ft.ttf', 50)
        self.score_text = "Top Achievements"
        self.credit_text_i = "Create by : IslandTropicalMan"
        self.over_text_i = "Game Over"
        self.next_text_i = "Next Level"
        self.text_width, self.text_height = self.font.size(self.score_text)
        self.credit_text_width, self.credit_text_height = self.credit_font.size(self.credit_text_i)
        self.over_text_width, self.over_text_height = self.credit_font.size(self.over_text_i)
        self.next_text_width, self.next_text_height = self.credit_font.size(self.next_text_i)
        self.x_title = 330 - self.text_width/2
        self.x_credit = 330 - self.credit_text_width/2
        self.x_over = 330 - self.over_text_width / 2
        self.x_next = 330 - self.next_text_width/2
        self.y_title = 60
        self.title_rect = Rect(self.x_title, self.y_title, self.text_width, self.text_height)
        self.title_score_text = self.font.render(self.score_text, 1, (255, 255, 255))
        self.credit_rect = Rect(self.x_credit, 300, self.credit_text_width, self.credit_text_height)
        self.over_rect = Rect(self.x_over, 190, self.over_text_width, self.over_text_height)
        self.next_rect = Rect(self.x_next, 190, self.next_text_width, self.next_text_height)
        self.credit_text = self.credit_font.render(self.credit_text_i, 1, (255, 255, 255))
        self.over_text = self.credit_font.render(self.over_text_i, 1, (255, 255, 255))
        self.next_text = self.credit_font.render(self.next_text_i, 1, (255, 255, 255))
        self.score_value_text = ''
        self.f1 = None
        self.font1 = txt.Font('Asset/ft.ttf', 100)
        self.score_rect = Rect(100, self.y_title+self.text_height, 100, 100)
        self.home_background_color = AirStrikeColor(0, 0, 0, 255)

    def draw(self, state):

        if(state == 0):
            self.scene.fill(self.home_background_color)
            self.scene.blit(self.game_logo_surface, self.draw_game_logo_pos) # draw a game logo
            self.scene.blit(self.play_button_surface, self.draw_play_button_pos)  # draw a button sprite
            self.scene.blit(self.about_button_surface, self.draw_about_button_pos)  # draw a button sprite
            self.scene.blit(self.score_button_surface, self.draw_score_button_pos)  # draw a button sprite
            self.scene.blit(self.manual_button_surface, self.draw_manual_button_pos)  # draw a button sprite
            self.scene.blit(self.exit_button_surface, self.draw_exit_button_pos)  # draw a button sprite
            self.scene.blit(self.scene_button_surface, self.draw_scene_button_pos)  # draw a button sprite
            if(self.soundon == True):
                self.scene.blit(self.soundon_button_surface, self.draw_sound_button_pos)  # draw a button sprite
            else:
                self.scene.blit(self.soundoff_button_surface, self.draw_sound_button_pos)  # draw a button sprite
        elif(state == 2):

            self.scene.fill(self.home_background_color)
            self.scene.blit(self.over_text, self.over_rect)  # the over text

        elif (state == 3):

            self.scene.fill(self.home_background_color)
            self.scene.blit(self.next_text, self.next_rect)  # the next text

        elif(state == 4):
            self.scene.blit(self.win_surface, self.draw_pos)  # draw a win sprite

        elif (state == 5):
            self.scene.fill(self.home_background_color) # draw a background
            self.scene.blit(self.credit_text, self.credit_rect)  # the credit text
            #self.scene.blit(self.about_surface, self.draw_pos)  # draw a about sprite
            self.scene.blit(self.home_button_surface, self.draw_back_button_pos)  # draw a button sprite

        elif (state == 6):
            self.scene.blit(self.manual_surface, self.draw_pos)  # draw a manual sprite
            self.scene.blit(self.home_button_surface, self.draw_back_button_pos)  # draw a button sprite

        elif (state == 7):
            #self.scene.blit(self.pause_surface, self.draw_pos)  # draw a pause sprite
            self.scene.fill(self.home_background_color)  # draw a background
            self.scene.blit(self.play_button_surface, self.draw_play_button_pos)  # draw a button sprite
            self.scene.blit(self.home_pause_button_surface, self.draw_home_button_pos)  # draw a button sprite

        elif (state == 8):

            self.scene.fill(self.home_background_color)  # draw a background
            self.scene.blit(self.title_score_text, self.title_rect) # the score title first
            list_level = self.level_manager.get_list()

            for i in range(len(list_level)):
                self.score_rect = Rect(95, self.y_title + self.text_height + self.count * 100, 100, 100)
                self.score_value_text = str(self.count+1) + ".) Level " + str(list_level[i])
                self.value_score_text = self.font1.render(self.score_value_text, 1, (255, 255, 255))
                self.scene.blit(self.value_score_text, self.score_rect)  # the top 5 levels of the game
                self.count += 1

            self.count = 0

            self.scene.blit(self.home_button_surface, self.draw_back_button_pos)  # draw a button sprite

        if(state == 2 or state == 3 or state == 4):
            self.scene.blit(self.button_surface, self.draw_button_pos)  # draw a button sprite

        pygame.display.flip()