import pygame
from pygame.locals import *
from GameManager import GameManager

# run this file to play the game

pygame.init()

size = width, height = 660, 660
pygame.display.set_caption("Air Strike")  # set the title of the window
screen = pygame.display.set_mode(size)
game_manager = GameManager(screen)
rect_exit = Rect(229, 456, 200, 53)  # the position of the exit button on the home scene
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_manager.save_level()
            running = False
        # detect key press event
        if event.type == KEYDOWN:

            if (game_manager.state == 1):
                if event.key == K_LEFT:
                    game_manager.set_player_x(-0.1)
                elif event.key == K_RIGHT:
                    game_manager.set_player_x(0.1)

                if event.key == K_UP:
                    game_manager.set_player_y(-0.1)
                elif event.key == K_DOWN:
                    game_manager.set_player_y(0.1)

                if event.key == K_SPACE:
                    game_manager.set_missile_strike(True)

                if event.key == K_p:
                    game_manager.set_pause(True)  # set the pause state to true

                if event.key == K_s:
                    game_manager.save_scene()

        elif event.type == KEYUP:

            if (game_manager.state == 1):
                if event.key == K_LEFT:
                    game_manager.set_player_x(0)
                elif event.key == K_RIGHT:
                    game_manager.set_player_x(0)

                if event.key == K_UP:
                    game_manager.set_player_y(0)
                elif event.key == K_DOWN:
                    game_manager.set_player_y(0)

                if event.key == K_SPACE:
                    game_manager.set_missile_strike(False)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if (rect_exit.collidepoint(x, y) and game_manager.state == game_manager.LOAD):
                game_manager.save_level()
                running = False
            # 1 is the left mouse button
            elif event.button == 1:
                game_manager.isAreaClick(x, y)

    game_manager.loop()