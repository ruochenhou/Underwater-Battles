#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from math import pi, cos, sin

from colors import WHITE, GREY


class Aim:
    def __init__(self):
        self.alpha = 0
        self.beta = 0.08 * pi
        self.r1 = 9
        self.r2 = 16

    def update(self, dt):
        self.alpha += dt/2000 * 2*pi
        while self.alpha >= 2*pi:
            self.alpha -= 2*pi

    def draw(self, screen, rect):
        x0, y0 = rect.centerx, rect.centery

        x1 = self.r1 * cos(self.alpha)
        y1 = self.r1 * sin(self.alpha)
        x2 = self.r2 * cos(self.alpha + self.beta)
        y2 = self.r2 * sin(self.alpha + self.beta)
        x3 = self.r2 * cos(self.alpha - self.beta)
        y3 = self.r2 * sin(self.alpha - self.beta)

        x4 = self.r1 * cos(self.alpha + pi/2)
        y4 = self.r1 * sin(self.alpha + pi/2)
        x5 = self.r2 * cos(self.alpha + pi/2 + self.beta)
        y5 = self.r2 * sin(self.alpha + pi/2 + self.beta)
        x6 = self.r2 * cos(self.alpha + pi/2 - self.beta)
        y6 = self.r2 * sin(self.alpha + pi/2 - self.beta)

        pygame.draw.polygon(screen, GREY, ((x0+x1, y0+y1), (x0+x2, y0+y2), (x0+x3, y0+y3)))
        pygame.draw.polygon(screen, GREY, ((x0-x1, y0-y1), (x0-x2, y0-y2), (x0-x3, y0-y3)))
        pygame.draw.polygon(screen, GREY, ((x0+x4, y0+y4), (x0+x5, y0+y5), (x0+x6, y0+y6)))
        pygame.draw.polygon(screen, GREY, ((x0-x4, y0-y4), (x0-x5, y0-y5), (x0-x6, y0-y6)))


class Point:
    def __init__(self, coords, is_first_point=False):
        self.coords = coords
        self.is_first_point = is_first_point
        self.scale = 23

    def draw(self, screen, dx, dy, rect):
        x = rect.centerx + (self.coords[0] - dx) * self.scale
        y = rect.centery + (self.coords[1] - dy) * self.scale

        if rect.collidepoint(x, y):
            pygame.draw.circle(screen, WHITE, (x, y), 4)
            pygame.draw.circle(screen, GREY, (x, y), 8, 1)

            if self.is_first_point:
                pygame.draw.circle(screen, GREY, (x, y), 12, 1)


class GameMap:
    def __init__(self):
        self.points = [Point((0, 0), True)]
        self.current_point = (0, 0)
        self.rect = pygame.Rect(125, 165, 620, 385)

        self.lines = []

        self.aim = Aim()

        self.dx = 0
        self.dy = 0

    def reset(self):
        self.points = [Point((0, 0), True)]
        self.current_point = (0, 0)
        self.lines = []
        self.dx = 0
        self.dy = 0

    def new_line(self, coords):
        for line in self.lines:
            if line in [(self.current_point, coords),
                        (coords, self.current_point)]:
                return False
        return True

    def new_point(self, coords):
        for point in self.points:
            if point.coords == coords:
                return False
        return True

    def update_data(self, coords):
        if self.new_line(coords):
            self.lines.append((self.current_point, coords))

        if self.new_point(coords):
            self.points.append(Point(coords))

        self.current_point = coords
        self.dx = coords[0]
        self.dy = coords[1]

    def update(self, dt):
        self.aim.update(dt)

    def line_on_screen(self, pos1, pos2):
        if self.rect.collidepoint(pos1) and self.rect.collidepoint(pos2):
            return True
        return False

    def draw_lines(self, screen):
        for line in self.lines:
            x1 = self.rect.centerx + (line[0][0] - self.dx) * 23
            y1 = self.rect.centery + (line[0][1] - self.dy) * 23
            x2 = self.rect.centerx + (line[1][0] - self.dx) * 23
            y2 = self.rect.centery + (line[1][1] - self.dy) * 23

            if self.line_on_screen((x1, y1), (x2, y2)):
                pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2))

    def draw_points(self, screen):
        for point in self.points:
            point.draw(screen, self.dx, self.dy, self.rect)

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect, 1)

        self.draw_lines(screen)

        self.draw_points(screen)

        self.aim.draw(screen, self.rect)
