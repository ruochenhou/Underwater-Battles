#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg
from random import uniform
from math import pi, sin, cos
from abc import ABC, abstractmethod

import config as c
from circle import Circle
import colors as col
from effects_surfaces import (PARALYZING_EXPLOSION_SURFACE,
                              POWERFUL_EXPLOSION_SURFACE,
                              TELEPORTATION_SURFACE)


def add_effect(name, effects, x=0, y=0, radius=0):
    if name == 'SmallHitLines':
        effects.append(BulletHitLines(x, y, size_marker=1))
    elif name == 'BigHitLines':
        effects.append(BulletHitLines(x, y, size_marker=2))
    elif name == 'RedHitCircle':
        effects.append(BulletHitCircle(x, y, col.RED))
    elif name == 'VioletHitCircle':
        effects.append(BulletHitCircle(x, y, col.VIOLET))
    elif name == 'Armor':
        effects.append(Armor(x, y, radius))
    elif name == 'ParalyzingExplosion':
        effects.append(ParalyzingExplosion(x, y))
    elif name == 'PowerfulExplosion':
        effects.append(PowerfulExplosion(x, y))
    elif name == 'Flash':
        effects.append(Flash())
    elif name == 'StarsAroundMob':
        effects.append(StarsAroundMob(x, y, radius))
    elif name == 'TeleportationFlash':
        effects.append(TeleportationFlash(x, y))


# ----------------------------------------------------------------------------- #
class Line:
    def __init__(self, x, y, size_marker, alpha, duration):
        radius = 20
        length = 37 + 120 * uniform(0, 1) if size_marker == 1 else 135 + 250 * uniform(0, 1)
        cosa, sina = cos(alpha), sin(alpha)
        self.X0 = x + radius * cosa
        self.Y0 = y - radius * sina
        self.X1, self.Y1 = self.X0, self.Y0
        self.vel_x = length * cosa / duration
        self.vel_y = -length * sina / duration
        self.widths = [2, 3, 4] if size_marker == 1 else [5, 7, 9]

    def update(self, dt):
        self.X1 += self.vel_x * dt
        self.Y1 += self.vel_y * dt

    def draw(self, surface, dx, dy):
        pg.draw.line(surface, col.HIT_COLOR,
                     (self.X0 - dx, self.Y0 - dy),
                     (self.X1 - dx, self.Y1 - dy), self.widths[0])
        pg.draw.line(surface, col.HIT_COLOR,
                     (self.X0 + (self.X1-self.X0)*0.125 - dx,
                      self.Y0 + (self.Y1-self.Y0)*0.125 - dy),
                     (self.X1 - (self.X1-self.X0)*0.125 - dx,
                      self.Y1 - (self.Y1-self.Y0)*0.125 - dy), self.widths[1])
        pg.draw.line(surface, col.HIT_COLOR,
                     (self.X0 + (self.X1-self.X0)*0.25 - dx,
                      self.Y0 + (self.Y1-self.Y0)*0.25 - dy),
                     (self.X1 - (self.X1-self.X0)*0.25 - dx,
                      self.Y1 - (self.Y1-self.Y0)*0.25 - dy), self.widths[2])


# ----------------------------------------------------------------------------- #
class SpecialEffect(ABC):
    def __init__(self, x, y, duration):
        self.x = x
        self.y = y
        self.t = 0
        self.duration = duration
        self.running = True

    def update(self, dt):
        self.t = min(self.t + dt, self.duration)
        if self.t >= self.duration:
            self.running = False

    @abstractmethod
    def draw(self, screen, dx, dy):
        pass


# ----------------------------------------------------------------------------- #
class BulletHitLines(SpecialEffect):
    def __init__(self, x, y, size_marker):
        super().__init__(x, y, duration=90)
        self.lines = self.create_lines(size_marker)

    def create_lines(self, size_marker):
        lines = []
        beta = 0
        for i in range(4):
            angle = uniform(pi/16, 7*pi/16) + beta
            beta += pi/2
            lines.append(Line(self.x, self.y, size_marker, angle, self.duration))
        return lines

    def update(self, dt):
        super().update(dt)

        for line in self.lines:
            line.update(dt)

    def draw(self, surface, dx, dy):
        for line in self.lines:
            line.draw(surface, dx, dy)


# ----------------------------------------------------------------------------- #
class BulletHitCircle(SpecialEffect):
    def __init__(self, x, y, color):
        super().__init__(x, y, duration=125)
        self.r = 30
        self.circle = Circle(40, 2, color, 0, 0, True,
                             0.32, 80, 0.75, True, False)

        self.surface = pg.Surface((120, 120))
        self.alpha = 255
        self.surface.set_alpha(self.alpha)
        self.surface.set_colorkey(col.BLACK)

    def update(self, dt):
        super().update(dt)

        self.circle.update(60, 60, dt)

        self.alpha -= 255 / (self.duration / dt)
        self.alpha = max(self.alpha, 0)
        self.surface.set_alpha(int(self.alpha))

    def draw(self, surface, dx, dy):
        self.surface.fill(col.BLACK)
        self.circle.draw(self.surface, 0, 0)
        surface.blit(self.surface, (self.x - 60 - dx,
                                    self.y - 60 - dy))


# ----------------------------------------------------------------------------- #
class Armor(SpecialEffect):
    def __init__(self, x, y, radius):
        super().__init__(x+3, y, duration=500)
        self.surface = pg.Surface((2*radius, 2*radius))
        self.surface.fill(col.COLOR_KEY)
        pg.draw.circle(self.surface, col.WHITE, (radius, radius), radius)
        self.surface.set_colorkey(col.COLOR_KEY)
        self.surface.set_alpha(255)
        self.is_shifted = False

    def shift(self):
        self.x -= 3
        self.is_shifted = True

    def update(self, dt):
        super().update(dt)
        alpha = int(255 - self.t / self.duration * 255)
        self.surface.set_alpha(alpha)
        if self.t >= 50 and not self.is_shifted:
            self.shift()

    def draw(self, screen, dx, dy):
        screen.blit(self.surface, (self.x, self.y))


# ----------------------------------------------------------------------------- #
class ParalyzingExplosion(SpecialEffect):
    def __init__(self, x, y):
        super().__init__(x, y, duration=300)
        self.surface_0 = PARALYZING_EXPLOSION_SURFACE
        self.surface = None
        self.max_diam = 400
        self.diam = None

    def update(self, dt):
        super().update(dt)
        if self.t <= self.duration:
            self.diam = int(self.max_diam * self.t/(self.duration))
            self.surface = pg.transform.scale(self.surface_0, (self.diam, self.diam))

    def draw(self, screen, dx, dy):
        screen.blit(self.surface, (self.x - self.diam/2 - dx,
                                   self.y - self.diam/2 - dy))


# ----------------------------------------------------------------------------- #
class PowerfulExplosion(SpecialEffect):
    def __init__(self, x, y):
        super().__init__(x, y, duration=300)
        self.surface_0 = POWERFUL_EXPLOSION_SURFACE
        self.surface = None
        self.max_diam = 500
        self.diam = None

    def update(self, dt):
        super().update(dt)
        if self.t <= self.duration:
            self.diam = int(self.max_diam * self.t/(self.duration))
            self.surface = pg.transform.scale(self.surface_0, (self.diam, self.diam))

    def draw(self, screen, dx, dy):
        screen.blit(self.surface, (self.x - self.diam/2 - dx,
                                   self.y - self.diam/2 - dy))


# ----------------------------------------------------------------------------- #
class Flash(SpecialEffect):
    def __init__(self):
        super().__init__(0, 0, duration=200)
        self.surface = pg.Surface((c.SCR_W, c.SCR_H))
        self.surface.fill(col.WHITE)

    def update(self, dt):
        super().update(dt)
        alpha = int(255 * (1-self.t/self.duration))
        self.surface.set_alpha(alpha)

    def draw(self, screen, dx, dy):
        screen.blit(self.surface, (0, 0))


# ----------------------------------------------------------------------------- #
class StarsAroundMob(SpecialEffect):
    def __init__(self, mob_x, mob_y, mob_radius):
        super().__init__(mob_x, mob_y, duration=2000)

        self.angle = uniform(0, 2*pi)
        self.timer = 0
        self.radius = mob_radius + 40
        self.big_stars_marker = True

    def get_stars_coords(self, dx, dy):
        pos_1 = (int(self.x + self.radius * cos(self.angle) - dx),
                 int(self.y - self.radius * sin(self.angle) - dy))

        pos_2 = (int(self.x + self.radius * cos(self.angle+2/3*pi) - dx),
                 int(self.y - self.radius * sin(self.angle+2/3*pi) - dy))

        pos_3 = (int(self.x + self.radius * cos(self.angle+4/3*pi) - dx),
                 int(self.y - self.radius * sin(self.angle+4/3*pi) - dy))

        return [pos_1, pos_2, pos_3]

    def update_stars_marker(self, dt):
        self.timer += dt
        if self.timer >= 80:
            self.timer -= 80
            self.angle += 0.4 * pi
            self.big_stars_marker = not self.big_stars_marker

    def update(self, dt):
        super().update(dt)
        self.update_stars_marker(dt)

    @staticmethod
    def draw_big_star(screen, x, y):
        pg.draw.circle(screen, col.WHITE, (x, y), 5, 2)
        pg.draw.line(screen, col.WHITE, (x, y - 17), (x, y + 7), 2)
        pg.draw.line(screen, col.WHITE, (x - 6, y), (x + 8, y), 2)

    @staticmethod
    def draw_small_star(screen, x, y):
        pg.draw.circle(screen, col.WHITE, (x, y), 3)

    def draw(self, screen, dx, dy):
        if self.big_stars_marker:
            for pos in self.get_stars_coords(dx, dy):
                self.draw_big_star(screen, *pos)
        else:
            for pos in self.get_stars_coords(dx, dy):
                self.draw_small_star(screen, *pos)


# ----------------------------------------------------------------------------- #
class TeleportationFlash(SpecialEffect):
    def __init__(self, x, y):
        super().__init__(x, y, duration=250)
        self.surface_0 = TELEPORTATION_SURFACE
        self.surface = None
        self.diam = 0

    def update(self, dt):
        super().update(dt)
        if self.t <= self.duration:
            self.diam = int(200 - 200*self.t/self.duration)
            self.surface = pg.transform.scale(self.surface_0, (self.diam, self.diam))

    def draw(self, screen, dx, dy):
        screen.blit(self.surface, (self.x - self.diam/2 - dx,
                                   self.y - self.diam/2 - dy))
