#!/usr/bin/python3
# encoding: utf-8
# @file: game.py
# @created: 2020/1/1 4:52 PM
# @desc:

import pygame
from pygame.locals import *
from config import *
from ball import Ball


class game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(game_resolution)
        self.clock = pygame.time.Clock()
        self.gameObjects = []
        self.gameObjects.append(Ball(game_resolution, rad=5))
        self.gameObjects.append(Ball(game_resolution, xPos=100, rad=5))

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

    def run(self):

        while True:
            self.handleEvents()

            for gameObj in self.gameObjects:
                gameObj.update()

            self.screen.fill(white)

            for gameObj in self.gameObjects:
                gameObj.draw(self.screen)

            self.clock.tick(60)
            pygame.display.flip()

game().run()
