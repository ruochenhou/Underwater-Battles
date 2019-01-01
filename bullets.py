#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, cos, pi
from random import uniform
import pygame as pg

import config as c
from body import Body
from data_bullets import SNIPER_BULLET_BODY, SHURIKEN_BODY, BIG_BUL_BODY_1
from colors import RED, LIGHT_RED, DARK_RED, COLOR_KEY, WHITE
from math_functions import circle_collidepoint, calculate_angle


# ----------------------------------------------------------------------------- #
class Bullet:
    """ a parent class for all bullets classes """
    def __init__(self, x, y, damage, vel, angle, body):
        self.x = x
        self.y = y
        self.vel = vel
        self.vel_x = vel * cos(angle)
        self.vel_y = -vel * sin(angle)
        self.damage = damage
        self.hit_effect = self.set_hit_effect(damage)
        self.body = body
        self.hit_the_target = False
        self.exploding = False
        self.frangible = False

    @staticmethod
    def set_hit_effect(damage):
        if damage <= -5: return 'BigHitLines'
        if damage: return 'SmallHitLines'
        return 'VioletHitCircle'

    def update_pos(self, dt):
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.body.move(dx, dy)

    def is_outside(self):
        """
        :return: Bullet is outside the room circle
        """
        return not circle_collidepoint(c.SCR_W2, c.SCR_H2, c.ROOM_RADIUS, self.x, self.y)

    def draw(self, surface, dx, dy):
        self.body.draw(surface, dx, dy)


# ----------------------------------------------------------------------------- #
class RegularBullet(Bullet):
    """ A bullet with uniform rectilinear motion """
    def __init__(self, x, y, damage, vel, angle, body):
        Bullet.__init__(self, x, y, damage, vel, angle, body)
        self.body.update(self.x, self.y, 0)

    def update(self, dt):
        self.update_pos(dt)
        self.body.update(self.x, self.y, dt)


# ----------------------------------------------------------------------------- #
class BombBullet(Bullet):
    """A bullet which is not moving and has a specific body update"""
    def __init__(self, x, y, body):
        Bullet.__init__(self, x, y, -10, 0, 0, body)

        self.rotate_body()
        self.body.update(self.x, self.y, 0)

        # bullet switches colors periodically
        self.colors = {1: self.body.circles[0].color, -1: LIGHT_RED}
        self.color_switch = 1
        self.T = 240
        self.color_time = uniform(0, self.T)

    def rotate_body(self):
        angle = uniform(0, 2*pi)
        for circle in self.body.circles:
            circle.alpha += angle

    def change_color(self):
        self.color_switch *= -1
        self.body.circles[3].color = self.colors[self.color_switch]

    def update_color(self, dt):
        self.color_time += dt
        if self.color_time >= 0.75 * self.T and self.color_switch == 1:
            self.change_color()
        elif self.color_time >= self.T and self.color_switch == -1:
            self.change_color()
            self.color_time -= self.T

    def update(self, dt):
        self.update_color(dt)


# ----------------------------------------------------------------------------- #
class EllipticBullet(Bullet):
    """ A bullet with uniform rectilinear motion.
        Its body is a surface with transparent background and
        an ellipse drawn on it, so the 'draw' function is different
        from RegularBullet.

    """
    def __init__(self, x, y, damage, vel, angle, body):
        Bullet.__init__(self, x, y, damage, vel, angle, body)

        self.body = pg.transform.rotate(body, angle * 180/pi)
        self.x = x - self.body.get_width() / 2
        self.y = y - self.body.get_height() / 2

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def update(self, dt):
        self.update_pos(dt)

    def draw(self, surface, dx, dy):
        surface.blit(self.body, (int(self.x-dx), int(self.y-dy)))


# ----------------------------------------------------------------------------- #
class HomingMissile(Bullet):
    """ A bullet which moves with constant velocity and follows a moving target.
        Therefore, the x- and y-components of velocity are changing. """
    def __init__(self, x, y, radius, damage, vel, body):
        Bullet.__init__(self, x, y, damage, vel, 0, body)

        self.body.update(self.x, self.y, 0)
        self.health = 1
        self.rect = pg.Rect(self.x - radius, self.y - radius, 2*radius, 2*radius)
        self.hit_effect = 'RedHirCircle'

    def collide_bullet(self, x, y):
        return self.rect.collidepoint(x, y)

    def handle_injure(self, damage):
        self.health += damage

    def update_pos(self, dt):
        super().update_pos(dt)
        self.rect.center = (self.x, self.y)

    def update_vel(self, angle):
        self.vel_x = self.vel * cos(angle)
        self.vel_y = -self.vel * sin(angle)

    def update(self, dt, target_x=0, target_y=0):
        angle = calculate_angle(self.x, self.y, target_x, target_y)
        self.update_vel(angle)
        self.update_pos(dt)
        self.body.update(self.x, self.y, dt, [target_x, target_y])


# ----------------------------------------------------------------------------- #
class FrangibleBullet(Bullet):
    """
     Bullet moves evenly and rectilinearly until its timer achieves fragmentation time.
     After this bullet explodes to form fragments scattering in all directions.
     If bullet collides with an object before fragmentation_time, it deals
     damage as a regular bullet and then disappears.

    """
    def __init__(self, x, y, angle, body):
        Bullet.__init__(self, x, y, -10, 0.5, angle, body)
        self.body.update(self.x, self.y, 0)
        self.frangible = True
        self.timer = 0
        self.fragmentation_time = 1000

    def create_fragments(self, fragments):
        for i in range(0, 360, 10):
            fragments.append(EllipticBullet(self.x, self.y, -15, 1.35, i * pi/180, SNIPER_BULLET_BODY))

    def update(self, dt, fragments):
        self.update_pos(dt)
        self.body.update(self.x, self.y, dt)

        self.timer = min(self.timer + dt, self.fragmentation_time)
        if self.timer == self.fragmentation_time:
            self.hit_the_target = True
            self.create_fragments(fragments)


# ----------------------------------------------------------------------------- #
class Shuriken(Bullet):
    """
    Bullet has two states: 'orbiting', when it rotates around the player;
                           'not orbiting', when it moves as a regular bullet.
    Initially bullet is orbiting. If some target intersects with bullet's searching area,
    bullet starts moving evenly and rectilinearly to a target's position.

    """
    def __init__(self, x, y, angle):
        Bullet.__init__(self, x, y, -7, 1.6, 0, Body(SHURIKEN_BODY))

        self.is_orbiting = True
        self.angle = angle
        self.omega = -0.002 * pi
        self.health = 1
        self.search_area_rect = pg.Rect(self.x - 110, self.y - 110, 220, 220)
        self.update_polar_coords(x, y)
        self.hit_effect = 'RedHirCircle'

    def is_near_mob(self, mob):
        return self.search_area_rect.colliderect(mob.body_rect)

    def update_polar_coords(self, x, y, dt=0):
        self.angle += self.omega * dt
        while self.angle < 0:
            self.angle += 2 * pi

        self.x = x + 90 * cos(self.angle)
        self.y = y - 90 * sin(self.angle)
        self.search_area_rect.center = (self.x, self.y)
        self.body.update(self.x, self.y, 0)

    def set_vel(self, target_x, target_y):
        """
        Method is called when a target intersected with bullet's searching area.
        Sets x- and y- velocity components according to target position.

        """
        angle = calculate_angle(self.x, self.y, target_x, target_y)
        self.vel_x = self.vel * cos(angle)
        self.vel_y = -self.vel * sin(angle)

    def update_pos(self, dt):
        super().update_pos(dt)
        self.search_area_rect.center = (self.x, self.y)
        self.body.update(self.x, self.y, 0)

    def check_targets(self, mobs):
        for mob in mobs:
            if self.is_near_mob(mob):
                self.is_orbiting = False
                self.set_vel(mob.x, mob.y)
                break

    def update(self, dt, x, y, mobs):
        if self.is_orbiting:
            self.update_polar_coords(x, y, dt)
            self.check_targets(mobs)
        else:
            self.update_pos(dt)


# ----------------------------------------------------------------------------- #
class ExplodingBullet(RegularBullet):
    """
     Bullet moves evenly and rectilinearly and explodes
     from contact with the enemy, damaging others.

    """
    def __init__(self, x, y, angle):
        super().__init__(x, y, -20, 0.7, angle, Body(BIG_BUL_BODY_1))

        # bullet switches colors periodically
        self.exploding = True
        self.colors = {1: DARK_RED, -1: LIGHT_RED}
        self.color_switch = 1
        self.T = 80
        self.color_time = 0

    def change_color(self):
        self.color_switch *= -1
        self.body.circles[0].color = self.colors[self.color_switch]

    def update_color(self, dt):
        self.color_time += dt
        if self.color_time >= 0.75 * self.T and self.color_switch == 1:
            self.change_color()
        elif self.color_time >= self.T and self.color_switch == -1:
            self.change_color()
            self.color_time -= self.T

    def update(self, dt):
        super().update(dt)
        self.update_color(dt)
