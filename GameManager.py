from Player import Player
from Background import Background
from EnemyManager import EnemyManager
from Overlap import Overlap
from ExplosionManager import ExplosionManager
from Score import Score
from StartScene import StartScene
from pygame.locals import *
from LevelManager import LevelManager
import pygame
import webbrowser
from Scene import Scene

class GameManager(object):

    def __init__(self, scene):

        self.scene = scene

        self.load_music()
        self.play_music()
        self.overlap_manager = Overlap()
        self.level_manager = LevelManager(self)
        self.level_manager.set_level()
        self.setup(self.level_manager.get_level())
        self.start_scene = StartScene(scene, self.level_manager)
        #self.setup(3)

        self.pause = False # flag to pause the game

        self.game_scene = Scene(self.scene)

        #game state
        self.LOAD = 0
        self.GAME = 1
        self.OVER = 2
        self.NEXT = 3
        self.WIN = 4
        self.ABOUT = 5
        self.MANUAL = 6
        self.PAUSE = 7
        self.SCORE = 8
        self.SCENE = 9

        self.state = self.LOAD

    def setup(self, game_level):

        self.game_level = game_level
        self.score_manager = Score(self.scene, self.level_manager)
        self.background = Background(self.scene)
        self.player = Player(self.scene)
        self.enemy_manager = EnemyManager(self.scene, self.player, game_level)
        self.explosion_manager = ExplosionManager(self.scene)

    def loop(self):

        if(self.state == self.LOAD):
            self.start_scene.draw(self.state)
        elif(self.state == self.OVER or self.state == self.NEXT or self.state == self.WIN or self.state == self.ABOUT or self.state == self.MANUAL or self.state == self.SCORE):
            self.start_scene.draw(self.state)
        elif(self.state == self.SCENE):
            self.game_scene.draw()
        elif(self.state == self.GAME):

            self.update()
            self.draw()

        elif(self.state == self.PAUSE):

            self.start_scene.draw(self.state)

    def isAreaClick(self, x, y):
        if (self.state == self.LOAD or self.state == self.OVER or self.state == self.NEXT or self.state == self.WIN or self.state == self.ABOUT or self.state == self.SCORE or self.state == self.SCENE or self.state == self.MANUAL or self.state == self.PAUSE):
            self.rect = Rect(177, 274, 306, 112) # the position of the play button on the scene
            self.rect_play = Rect(229, 200, 200, 53)  # the position of the play button on the home scene
            self.rect_about = Rect(229, 263, 200, 53)  # the position of the about button on the home scene
            #self.rect_exit = Rect(229, 456, 200, 53)  # the position of the exit button on the home scene
            self.rect_pause_home = Rect(229, 263, 200, 53)  # the position of the home button on pause scene
            self.rect_score = Rect(229, 328, 200, 53)  # the position of the score button on the home scene
            self.rect_manual = Rect(229, 393, 200, 53)  # the position of the manual button on the home scene
            self.rect_scene = Rect(229, 519, 200, 53)  # the position of the manual button on the home scene
            self.rect_back = Rect(10, 620, 40, 30)  # the position of the back button on the home scene
            self.rect_sound = Rect(10, 620, 30, 30) # the position of the sound button on the home scene
            self.rect_scene_next = Rect(610, 330, 30, 30)  # the position of the next scene button on scene
            self.rect_scene_previous = Rect(50, 330, 30, 30)  # the position of the previous scene button on scene

            if(self.rect.collidepoint(x, y) and (self.state == self.OVER or self.state == self.NEXT or self.state == self.WIN)):
                self.state = self.GAME
            elif(self.rect_play.collidepoint(x,y) and self.state == self.LOAD):
                self.state = self.GAME
            elif (self.rect_play.collidepoint(x, y) and self.state == self.PAUSE):
                self.state = self.GAME
            elif (self.rect_about.collidepoint(x, y) and self.state == self.LOAD):
                self.state = self.ABOUT
            elif (self.rect_score.collidepoint(x, y) and self.state == self.LOAD):
                self.state = self.SCORE
            elif (self.rect_scene.collidepoint(x, y) and self.state == self.LOAD):
                self.state = self.SCENE
            elif (self.rect_back.collidepoint(x, y) and self.state == self.SCENE):
                self.state = self.LOAD
            elif (self.rect_scene_next.collidepoint(x, y) and self.state == self.SCENE):
                self.game_scene.set_next_image()
            elif (self.rect_scene_previous.collidepoint(x, y) and self.state == self.SCENE):
                self.game_scene.set_previous_image()
            elif (self.rect_pause_home.collidepoint(x, y) and self.state == self.PAUSE):

                self.state = self.LOAD
                self.setup(self.level_manager.get_level())
                self.save_level()

            elif (self.rect_manual.collidepoint(x, y) and self.state == self.LOAD):
                webbrowser.open_new('http://gamingdirectional.com/blog/2018/12/25/air-strike//')
            elif (self.rect_back.collidepoint(x, y) and (self.state == self.ABOUT or self.state == self.MANUAL or self.state == self.SCORE)):
                self.state = self.LOAD
            elif (self.rect_sound.collidepoint(x, y) and self.state == self.LOAD):

                if(self.start_scene.soundon == True):
                    self.start_scene.soundon = False
                    pygame.mixer_music.pause()
                else:
                    self.start_scene.soundon = True
                    pygame.mixer_music.unpause()

    def save_level(self):
       self.level_manager.save_level()

    def set_pause(self, pause):

        self.pause = pause

        if(self.pause == True):

            self.state = self.PAUSE

    def load_music(self):
        pygame.mixer_music.load('Music/winternight.ogg')

    def play_music(self):
        pygame.mixer_music.play(-1) #play the music infinite time

    def set_player_x(self, _x):
        if (self.state == self.GAME):
            self.player.setX(_x)

    def save_scene(self):
        self.game_scene.take_screen()

    def set_player_y(self, _y):
        if (self.state == self.GAME):
            self.player.setY(_y)

    def set_missile_strike(self, strike):
        if (self.state == self.GAME):
            self.player.setStrike(strike)

    def update(self):
        self.player.update()
        self.enemy_manager.update()
        self.isOverlap()
        self.explosion_manager.explosion_update()

    # check for player, enemy, missiles overlap
    def isOverlap(self):
        self.overlap_manager.isOverlap(self.player, self.enemy_manager, self.explosion_manager, self.score_manager, self)

    def draw(self):
        if(self.state == self.GAME):
            self.background.draw()
            self.player.draw()
            self.enemy_manager.draw()
            self.explosion_manager.draw()
            self.score_manager.draw()
            pygame.display.flip()