#!/usr/bin/python3
# encoding: utf-8
# @file: ball.py
# @created: 2020/1/1 4:52 PM
# @desc:


from config import *
import pygame


class Ball:
    def __init__(self, resolution, xPos=0, yPos=0, xVel=1, yVel=1, rad=15):
        self.x_up_limit, self.y_up_limit = resolution
        self.x = xPos
        self.y = yPos
        self.dx = xVel
        self.dy = yVel
        self.radius = rad
        self.type = "ball"

        self.background = pygame.Surface(resolution)  # make a background surface
        self.background = self.background.convert()
        self.background.fill(white)

    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        pygame.draw.circle(surface, black, (int(self.x), int(self.y)), int(self.radius))

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if (self.x <= 0 or self.x >= self.x_up_limit):
            self.dx *= -1
        if (self.y <= 0 or self.y >= self.y_up_limit):
            self.dy *= -1
