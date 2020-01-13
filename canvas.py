#!/usr/bin/python3
# encoding: utf-8
# @file: canvas.py
# @created: 2020/1/10 11:14 PM
# @desc:

import pygame
import pygame_gui
from pygame_gui.core.ui_window import UIWindow
from pygame_gui.elements.ui_image import UIImage
from ball import Ball
from config import *

class GameWindow(UIWindow):
    def __init__(self, game_resolution, ui_manager):
        super().__init__(pygame.Rect((0, 0), game_resolution), ui_manager, ['game_window'])
        x_res, y_res = game_resolution

        self.game = Ball(game_resolution, x_res/2, y_res/2, rad=5)
        self.game_surface_element = UIImage(pygame.Rect((0, 0), game_resolution),
                                            pygame.Surface(game_resolution).convert(),
                                            manager=ui_manager,
                                            container=self.get_container(),
                                            parent_element=self)

    def process_event(self, event):
        pass

    def update(self, time_delta):
        self.game.update()

        super().update(time_delta)

        self.game.draw(self.game_surface_element.image)


class Canvas:
    def __init__(self, gui_resolution, game_resolution):
        pygame.init()

        self.window_surface = pygame.display.set_mode(gui_resolution)

        self.background = pygame.Surface(gui_resolution)
        self.background.fill(pygame.Color('#808080'))
        self.ui_manager = pygame_gui.UIManager(gui_resolution)
        self.clock = pygame.time.Clock()
        self.is_running = True

        self.game_window = GameWindow(game_resolution, self.ui_manager)

    def run(self):
        while self.is_running:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

                self.ui_manager.process_events(event)

            self.ui_manager.update(time_delta)

            self.window_surface.blit(self.background, (0, 0))
            self.ui_manager.draw_ui(self.window_surface)

            pygame.display.update()

Canvas(gui_resolution, game_resolution).run()