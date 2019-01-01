#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi, cos
from colors import WHITE, BLUE, ORANGE, LIGHT_ORANGE, VIOLET, RED


###############################################################################
TURTLE_BODY =  [[22, 3, BLUE,   50, pi,          True, 0.016, 15, 0.1, False, False],
                [22, 3, BLUE,   50, 0.00,        True, 0.016, 15, 0.1, False, False],
                [22, 3, BLUE,   50, 0.667 * pi,  True, 0.016, 15, 0.4, False, False],
                [22, 3, BLUE,   50, -0.667 * pi, True, 0.016, 15, 0.7, False, False],
                [22, 3, BLUE,   50, 0.25 * pi,   True, 0.016, 15, 0.2, True,  False],
                [22, 3, BLUE,   50, 0.75 * pi,   True, 0.016, 15, 0.4, True,  False],
                [22, 3, BLUE,   50, -0.75 * pi,  True, 0.016, 15, 0.6, True,  False],
                [22, 3, BLUE,   50, -0.25 * pi,  True, 0.016, 15, 0.8, True,  False],
                [15, 2, BLUE,   69, 0.00,        True, 0.008, 8,  0.2, True,  False],
                [12, 2, BLUE,   50, 0.00,        True, 0.008, 8,  0.5, True,  False],
                [12, 2, BLUE,   68, 0.05 * pi,   True, 0.008, 8,  0.6, False, False],
                [12, 2, BLUE,   68, -0.05 * pi,  True, 0.008, 8,  0.1, False, False],
                [12, 2, BLUE,   74, 0.1 * pi,    True, 0.008, 8,  0.7, True,  False],
                [12, 2, BLUE,   74, -0.1 * pi,   True, 0.008, 8,  0.3, True,  False],
                [48, 6, BLUE,   0,  0.00,        True, 0.04,  30, 0,   True,  False],
                [12, 2, BLUE,   52, 0.85 * pi,   True, 0.008, 8,  0.1, True,  False],
                [12, 2, BLUE,   52, -0.85 * pi,  True, 0.008, 8,  0.7, True,  False],
                [12, 2, BLUE,   52, pi,          True, 0.008, 8,  0.3, True,  False],

                [10, 1, ORANGE, 0,  0.00,        True, 0.008, 7,  0.8, True,  True,  29, pi/4],
                [10, 1, ORANGE, 0,  0.00,        True, 0.008, 7,  0.6, True,  True,  29, -pi/4],
                [10, 1, ORANGE, 0,  0.00,        True, 0.008, 7,  0.4, True,  True,  42, pi/6],
                [10, 1, ORANGE, 0,  0.00,        True, 0.008, 7,  0.2, True,  True,  42, -pi/6],
                [9,  1, ORANGE, 0,  0.00,        True, 0.008, 7,  0,   True,  True,  55, pi/8],
                [9,  1, ORANGE, 0,  0.00,        True, 0.008, 7,  0,   True,  True,  55, -pi/8],
                [6,  1, ORANGE, 0,  0.00,        True, 0.007, 6,  0.3, True,  True,  56, -0.19*pi],
                [6,  1, ORANGE, 0,  0.00,        True, 0.007, 6,  0.9, True,  True,  56, 0.19*pi],
                [28, 4, ORANGE, 0,  0.00,        True, 0.027, 18, 0,   True,  True,  0,  0],
                [12, 2, ORANGE, 0,  0.00,        True, 0.01,  8,  0.2, True,  True,  30, -pi],
                [12, 2, ORANGE, 0,  0.00,        True, 0.01,  8,  0.5, True,  True,  30, -2 * pi/3],
                [12, 2, ORANGE, 0,  0.00,        True, 0.01,  8,  0.8, True,  True,  30, 2 * pi/3],

                [14, 1, VIOLET, 14, -0.15 * pi, False, 0,     0,  0,   False, False, 0, 0],
                [11, 1, VIOLET, 22, -0.35 * pi, False, 0,     0,  0,   False, False, 0, 0],
                [11, 1, VIOLET, 32, 0.22 * pi,  False, 0,     0,  0,   False, False, 0, 0],
                [11, 1, VIOLET, 32, -0.22 * pi, False, 0,     0,  0,   False, False, 0, 0],
                [11, 1, VIOLET, 30, -0.75 * pi, False, 0,     0,  0,   False, False, 0, 0],
                [13, 1, VIOLET, 40, -0.8 * pi,  False, 0,     0,  0,   False, False, 0, 0],
                [17, 1, VIOLET, 29, 0.82 * pi,  False, 0,     0,  0,   False, False, 0, 0],
                [11, 1, VIOLET, 8,  0.5 * pi,   False, 0,     0,  0,   False, False, 0, 0],
                [11, 1, VIOLET, 38, 0.6 * pi,   False, 0,     0,  0,   False, False, 0, 0],
                [12, 1, VIOLET, 22, 0.65 * pi,  False, 0,     0,  0,   False, False, 0, 0]]

TURTLE_HEALTH_STATES = ((21, (0, 4), (10, 12)),
                        (20, (0, 4), (8, 9), (12, 14)),
                        (19, (0, 4), (10, 14)),
                        (18, (0, 4), (8, 9), (10, 14)),
                        (17, (0, 4), (8, 9), (10, 14), (17, 18)),
                        (14, (0, 4), (8, 9), (10, 14), (15, 17)),
                        (11, (0, 4), (8, 9), (10, 14), (15, 18)),
                        (7, (0, 1), (4, 14), (15, 18)),
                        (4, (0, 2), (4, 14), (15, 18)),
                        (3, (1, 14), (15, 18)),
                        (2, (0, 14), (15, 18)))
###############################################################################
TERRORIST_BODY = [[40, 2, BLUE,         60,  0.5 * pi,   True,  0.022, 15, 0.1, True, False],
                  [40, 2, BLUE,         60,  -0.5 * pi,  True,  0.02,  15, 0.5, True, False],
                  [12, 2, BLUE,         102, -0.59 * pi, False, 0,     0,  0,   True, False],
                  [12, 2, BLUE,         102, 0.59 * pi,  False, 0,     0,  0,   True, False],
                  [12, 2, BLUE,         102, -0.41 * pi, False, 0,     0,  0,   True, False],
                  [12, 2, BLUE,         102, 0.41 * pi,  False, 0,     0,  0,   True, False],
                  [12, 2, BLUE,         44,  0.75 * pi,  False, 0,     0,  0,   True, False],
                  [12, 2, BLUE,         44,  -0.75 * pi, False, 0,     0,  0,   True, False],

                  [7,  1, ORANGE,       30,  0.2 * pi,   True,  0.005, 4,  0.1, True, False],
                  [7,  1, ORANGE,       30,  -0.2 * pi,  True,  0.005, 4,  0.3, True, False],
                  [7,  1, ORANGE,       23,  0.28 * pi,  True,  0.005, 4,  0.6, True, False],
                  [7,  1, ORANGE,       23,  -0.28 * pi, True,  0.005, 4,  0.9, True, False],
                  [7,  1, ORANGE,       18,  -0.43 * pi, True,  0.005, 4,  0.2, True, False],
                  [7,  1, ORANGE,       18,  0.43 * pi,  True,  0.005, 4,  0.5, True, False],
                  [7,  1, ORANGE,       19,  -0.62 * pi, True,  0.005, 4,  0.7, True, False],
                  [7,  1, ORANGE,       19,  0.62 * pi,  True,  0.005, 4,  0.1, True, False],
                  [7,  1, ORANGE,       24,  -0.73 * pi, True,  0.005, 4,  0.7, True, False],
                  [7,  1, ORANGE,       24,  0.73 * pi,  True,  0.005, 4,  0.1, True, False],
                  [7,  1, ORANGE,       31,  -0.8 * pi,  True,  0.005, 4,  0.7, True, False],
                  [7,  1, ORANGE,       31,  0.8 * pi,   True,  0.005, 4,  0.1, True, False],
                  [13, 2, LIGHT_ORANGE, 40,  0.15 * pi,  False, 0,     0,  0,   True, False, 0, 0, True, pi],
                  [13, 2, LIGHT_ORANGE, 40,  -0.15 * pi, False, 0,     0,  0,   True, False, 0, 0, True, pi],
                  [18, 2, ORANGE,       25,  0.00,       True,  0.013, 8,  0.1, True, False],
                  [12, 2, BLUE,         44,  0.25 * pi,  False, 0,     0,  0,   True, False],
                  [12, 2, BLUE,         44,  -0.25 * pi, False, 0,     0,  0,   True, False],
                  [12, 2, BLUE,         42,  0.12 * pi,  False, 0,     0,  0,   True, False],
                  [12, 2, BLUE,         42,  -0.12 * pi, False, 0,     0,  0,   True, False],
                  [12, 2, BLUE,         41,  0.00,       False, 0,     0,  0,   True, False],

                  [14, 1, VIOLET,       14, -0.15 * pi,  False, 0,     0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET,       22, -0.35 * pi,  False, 0,     0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET,       32, 0.22 * pi,   False, 0,     0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET,       32, -0.22 * pi,  False, 0,     0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET,       30, -0.75 * pi,  False, 0,     0,  0,   False, False, 0, 0],
                  [13, 1, VIOLET,       40, -0.8 * pi,   False, 0,     0,  0,   False, False, 0, 0],
                  [17, 1, VIOLET,       29, 0.82 * pi,   False, 0,     0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET,       8,  0.5 * pi,    False, 0,     0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET,       38, 0.6 * pi,    False, 0,     0,  0,   False, False, 0, 0],
                  [12, 1, VIOLET,       22, 0.65 * pi,   False, 0,     0,  0,   False, False, 0, 0]]

TERRORIST_HEALTH_STATES = ((18,),
                           (14, (2, 6)),
                           (8, (2, 8)),
                           (4, (2, 23)))
###############################################################################
BENLADEN_BODY = [[8,  1, ORANGE,       86,  0.572 * pi,  True,  0.007, 5,  0.1, True, False],
                 [8,  1, ORANGE,       86,  0.428 * pi,  True,  0.007, 5,  0.3, True, False],
                 [8,  1, ORANGE,       98,  0.564 * pi,  True,  0.007, 5,  0.6, True, False],
                 [8,  1, ORANGE,       98,  0.436 * pi,  True,  0.007, 5,  0.9, True, False],
                 [8,  1, ORANGE,       110, 0.558 * pi,  True,  0.007, 5,  0.2, True, False],
                 [8,  1, ORANGE,       110, 0.442 * pi,  True,  0.007, 5,  0.5, True, False],
                 [8,  1, ORANGE,       122, 0.551 * pi,  True,  0.007, 5,  0.7, True, False],
                 [8,  1, ORANGE,       122, 0.449 * pi,  True,  0.007, 5,  0.1, True, False],
                 [8,  1, ORANGE,       134, 0.546 * pi,  True,  0.007, 5,  0.4, True, False],
                 [8,  1, ORANGE,       134, 0.454 * pi,  True,  0.007, 5,  0.8, True, False],
                 [8,  1, ORANGE,       146, 0.542 * pi,  True,  0.007, 5,  0.2, True, False],
                 [8,  1, ORANGE,       146, 0.458 * pi,  True,  0.007, 5,  0.1, True, False],
                 [13, 2, LIGHT_ORANGE, 86,  0.572 * pi,  False, 0,     0,  0,   True, False, 0, 0, True, 0.5 * pi],
                 [13, 2, LIGHT_ORANGE, 86,  0.428 * pi,  False, 0,     0,  0,   True, False, 0, 0, True, 0.5 * pi],
                 [18, 2, ORANGE,       84,  0.5 * pi,    True,  0.02,  12, 0.1, True, False],

                 [8,  1, ORANGE,       86,  -0.572 * pi, True,  0.007, 5,  0.1, True, False],
                 [8,  1, ORANGE,       86,  -0.428 * pi, True,  0.007, 5,  0.3, True, False],
                 [8,  1, ORANGE,       98,  -0.564 * pi, True,  0.007, 5,  0.6, True, False],
                 [8,  1, ORANGE,       98,  -0.436 * pi, True,  0.007, 5,  0.9, True, False],
                 [8,  1, ORANGE,       110, -0.558 * pi, True,  0.007, 5,  0.2, True, False],
                 [8,  1, ORANGE,       110, -0.442 * pi, True,  0.007, 5,  0.5, True, False],
                 [8,  1, ORANGE,       122, -0.551 * pi, True,  0.007, 5,  0.7, True, False],
                 [8,  1, ORANGE,       122, -0.449 * pi, True,  0.007, 5,  0.1, True, False],
                 [8,  1, ORANGE,       134, -0.546 * pi, True,  0.007, 5,  0.4, True, False],
                 [8,  1, ORANGE,       134, -0.454 * pi, True,  0.007, 5,  0.8, True, False],
                 [8,  1, ORANGE,       146, -0.542 * pi, True,  0.007, 5,  0.2, True, False],
                 [8,  1, ORANGE,       146, -0.458 * pi, True,  0.007, 5,  0.1, True, False],
                 [13, 2, LIGHT_ORANGE, 86,  -0.572 * pi, False, 0,     0,  0,   True, False, 0, 0, True, -0.5 * pi],
                 [13, 2, LIGHT_ORANGE, 86,  -0.428 * pi, False, 0,     0,  0,   True, False, 0, 0, True, -0.5 * pi],
                 [18, 2, ORANGE,       84,  -0.5 * pi,   True,  0.02,  12, 0.1, True, False],

                 [8,  1, ORANGE,       86,  0.322 * pi,  True,  0.007, 5,  0.1, True, False],
                 [8,  1, ORANGE,       86,  0.178 * pi,  True,  0.007, 5,  0.3, True, False],
                 [8,  1, ORANGE,       98,  0.314 * pi,  True,  0.007, 5,  0.6, True, False],
                 [8,  1, ORANGE,       98,  0.186 * pi,  True,  0.007, 5,  0.9, True, False],
                 [8,  1, ORANGE,       110, 0.308 * pi,  True,  0.007, 5,  0.2, True, False],
                 [8,  1, ORANGE,       110, 0.192 * pi,  True,  0.007, 5,  0.5, True, False],
                 [8,  1, ORANGE,       122, 0.301 * pi,  True,  0.007, 5,  0.7, True, False],
                 [8,  1, ORANGE,       122, 0.199 * pi,  True,  0.007, 5,  0.1, True, False],
                 [8,  1, ORANGE,       134, 0.296 * pi,  True,  0.007, 5,  0.4, True, False],
                 [8,  1, ORANGE,       134, 0.204 * pi,  True,  0.007, 5,  0.8, True, False],
                 [8,  1, ORANGE,       146, 0.292 * pi,  True,  0.007, 5,  0.2, True, False],
                 [8,  1, ORANGE,       146, 0.208 * pi,  True,  0.007, 5,  0.1, True, False],
                 [13, 2, LIGHT_ORANGE, 86,  0.322 * pi,  False, 0,     0,  0,   True, False, 0, 0, True, 0.25 * pi],
                 [13, 2, LIGHT_ORANGE, 86,  0.178 * pi,  False, 0,     0,  0,   True, False, 0, 0, True, 0.25 * pi],
                 [18, 2, ORANGE,       84,  0.25 * pi,   True,  0.02,  12, 0.1, True, False],

                 [8,  1, ORANGE,       86,  -0.322 * pi, True,  0.007, 5,  0.1, True, False],
                 [8,  1, ORANGE,       86,  -0.178 * pi, True,  0.007, 5,  0.3, True, False],
                 [8,  1, ORANGE,       98,  -0.314 * pi, True,  0.007, 5,  0.6, True, False],
                 [8,  1, ORANGE,       98,  -0.186 * pi, True,  0.007, 5,  0.9, True, False],
                 [8,  1, ORANGE,       110, -0.308 * pi, True,  0.007, 5,  0.2, True, False],
                 [8,  1, ORANGE,       110, -0.192 * pi, True,  0.007, 5,  0.5, True, False],
                 [8,  1, ORANGE,       122, -0.301 * pi, True,  0.007, 5,  0.7, True, False],
                 [8,  1, ORANGE,       122, -0.199 * pi, True,  0.007, 5,  0.1, True, False],
                 [8,  1, ORANGE,       134, -0.296 * pi, True,  0.007, 5,  0.4, True, False],
                 [8,  1, ORANGE,       134, -0.204 * pi, True,  0.007, 5,  0.8, True, False],
                 [8,  1, ORANGE,       146, -0.292 * pi, True,  0.007, 5,  0.2, True, False],
                 [8,  1, ORANGE,       146, -0.208 * pi, True,  0.007, 5,  0.1, True, False],
                 [13, 2, LIGHT_ORANGE, 86,  -0.322 * pi, False, 0,     0,  0,   True, False, 0, 0, True, -0.25 * pi],
                 [13, 2, LIGHT_ORANGE, 86,  -0.178 * pi, False, 0,     0,  0,   True, False, 0, 0, True, -0.25 * pi],
                 [18, 2, ORANGE,       84,  -0.25 * pi,  True,  0.02,  12, 0.1, True, False],

                 [8,  1, ORANGE,       86,  0.822 * pi,  True,  0.007, 5,  0.1, True, False],
                 [8,  1, ORANGE,       86,  0.678 * pi,  True,  0.007, 5,  0.3, True, False],
                 [8,  1, ORANGE,       98,  0.814 * pi,  True,  0.007, 5,  0.6, True, False],
                 [8,  1, ORANGE,       98,  0.686 * pi,  True,  0.007, 5,  0.9, True, False],
                 [8,  1, ORANGE,       110, 0.808 * pi,  True,  0.007, 5,  0.2, True, False],
                 [8,  1, ORANGE,       110, 0.692 * pi,  True,  0.007, 5,  0.5, True, False],
                 [8,  1, ORANGE,       122, 0.801 * pi,  True,  0.007, 5,  0.7, True, False],
                 [8,  1, ORANGE,       122, 0.699 * pi,  True,  0.007, 5,  0.1, True, False],
                 [8,  1, ORANGE,       134, 0.796 * pi,  True,  0.007, 5,  0.4, True, False],
                 [8,  1, ORANGE,       134, 0.704 * pi,  True,  0.007, 5,  0.8, True, False],
                 [8,  1, ORANGE,       146, 0.792 * pi,  True,  0.007, 5,  0.2, True, False],
                 [8,  1, ORANGE,       146, 0.708 * pi,  True,  0.007, 5,  0.1, True, False],
                 [13, 2, LIGHT_ORANGE, 86,  0.822 * pi,  False, 0,     0,  0,   True, False, 0, 0, True, 0.75 * pi],
                 [13, 2, LIGHT_ORANGE, 86,  0.678 * pi,  False, 0,     0,  0,   True, False, 0, 0, True, 0.75 * pi],
                 [18, 2, ORANGE,       84,  0.75 * pi,   True,  0.02,  12, 0.1, True, False],

                 [8,  1, ORANGE,       86,  -0.822 * pi, True,  0.007, 5,  0.1, True, False],
                 [8,  1, ORANGE,       86,  -0.678 * pi, True,  0.007, 5,  0.3, True, False],
                 [8,  1, ORANGE,       98,  -0.814 * pi, True,  0.007, 5,  0.6, True, False],
                 [8,  1, ORANGE,       98,  -0.686 * pi, True,  0.007, 5,  0.9, True, False],
                 [8,  1, ORANGE,       110, -0.808 * pi, True,  0.007, 5,  0.2, True, False],
                 [8,  1, ORANGE,       110, -0.692 * pi, True,  0.007, 5,  0.5, True, False],
                 [8,  1, ORANGE,       122, -0.801 * pi, True,  0.007, 5,  0.7, True, False],
                 [8,  1, ORANGE,       122, -0.699 * pi, True,  0.007, 5,  0.1, True, False],
                 [8,  1, ORANGE,       134, -0.796 * pi, True,  0.007, 5,  0.4, True, False],
                 [8,  1, ORANGE,       134, -0.704 * pi, True,  0.007, 5,  0.8, True, False],
                 [8,  1, ORANGE,       146, -0.792 * pi, True,  0.007, 5,  0.2, True, False],
                 [8,  1, ORANGE,       146, -0.708 * pi, True,  0.007, 5,  0.1, True, False],
                 [13, 2, LIGHT_ORANGE, 86,  -0.822 * pi, False, 0,     0,  0,   True, False, 0, 0, True, -0.75 * pi],
                 [13, 2, LIGHT_ORANGE, 86,  -0.678 * pi, False, 0,     0,  0,   True, False, 0, 0, True, -0.75 * pi],
                 [18, 2, ORANGE,       84,  -0.75 * pi,  True,  0.02,  12, 0.1, True, False],

                 [21, 3, BLUE,         104, 0.9 * pi,    True,  0.032, 18, 0.1, True, False],
                 [21, 3, BLUE,         104, -0.9 * pi,   True,  0.032, 18, 0.4, True, False],
                 [90, 5, BLUE,         0,   0.00,        True,  0.05,  36, 0.1, True, False],
                 [16, 2, BLUE,         100, pi,          True,  0.022, 13, 0.3, True, False],
                 [12, 1, BLUE,         80,  pi,          True,  0.018, 10, 0.5, True, False],
                 [12, 1, BLUE,         12,  pi,          True,  0.018, 10, 0.7, True, False],
                 [24, 3, BLUE,         22,  0.00,        True,  0.031, 18, 0.8, True, False],
                 [12, 1, BLUE,         22,  0.5 * pi,    True,  0.018, 10, 0.0, True, False],
                 [12, 1, BLUE,         22,  -0.5 * pi,   True,  0.018, 10, 0.8, True, False],
                 [14, 1, BLUE,         64,  0.00,        True,  0.019, 11, 0.4, True, False],
                 [16, 2, BLUE,         46,  0.00,        True,  0.022, 13, 0.7, True, False],
                 [24, 3, BLUE,         92,  0.00,        True,  0.031, 18, 0.2, True, False],
                 [12, 1, BLUE,         116, 0.04 * pi,   True,  0.018, 10, 0.1, True, False],
                 [12, 1, BLUE,         116, -0.04 * pi,  True,  0.018, 10, 0.4, True, False],

                 [14, 1, VIOLET,       14, -0.15 * pi,   False, 0,     0,  0,   False, False, 0, 0],
                 [11, 1, VIOLET,       22, -0.35 * pi,   False, 0,     0,  0,   False, False, 0, 0],
                 [11, 1, VIOLET,       32, 0.22 * pi,    False, 0,     0,  0,   False, False, 0, 0],
                 [11, 1, VIOLET,       32, -0.22 * pi,   False, 0,     0,  0,   False, False, 0, 0],
                 [11, 1, VIOLET,       30, -0.75 * pi,   False, 0,     0,  0,   False, False, 0, 0],
                 [13, 1, VIOLET,       40, -0.8 * pi,    False, 0,     0,  0,   False, False, 0, 0],
                 [17, 1, VIOLET,       29, 0.82 * pi,    False, 0,     0,  0,   False, False, 0, 0],
                 [11, 1, VIOLET,       8,  0.5 * pi,     False, 0,     0,  0,   False, False, 0, 0],
                 [11, 1, VIOLET,       38, 0.6 * pi,     False, 0,     0,  0,   False, False, 0, 0],
                 [12, 1, VIOLET,       22, 0.65 * pi,    False, 0,     0,  0,   False, False, 0, 0]]

BENLADEN_HEALTH_STATES = ((0, ),)
###############################################################################
ANT_BODY = [[17, 2, BLUE,   0,  0.00,       True, 0.02,  13, 0,   True, True],
            [13, 2, BLUE,   27, 0.74 * pi,  True, 0.01,  6,  0.3, True, False],
            [13, 2, BLUE,   27, -0.74 * pi, True, 0.01,  6,  0,   True, False],
            [12, 2, BLUE,   24, 0.00,       True, 0.018, 11, 0.6, True, False],
            [10, 1, BLUE,   39, 0.1 * pi,   True, 0.012, 8,  0.3, True, False],
            [10, 1, BLUE,   39, -0.1 * pi,  True, 0.012, 8,  0,   True, False],
            [14, 2, ORANGE, 0,  0.00,       True, 0.025, 15, 0,   True, True],
            [5,  1, ORANGE, 0,  0.00,       True, 0.01,  5,  0,   True, True,  18],

            [14, 1, VIOLET, 14, -0.15 * pi, False, 0,     0,  0,   False, False, 0, 0],
            [11, 1, VIOLET, 22, -0.35 * pi, False, 0,     0,  0,   False, False, 0, 0],
            [11, 1, VIOLET, 32, 0.22 * pi,  False, 0,     0,  0,   False, False, 0, 0],
            [11, 1, VIOLET, 32, -0.22 * pi, False, 0,     0,  0,   False, False, 0, 0],
            [11, 1, VIOLET, 30, -0.75 * pi, False, 0,     0,  0,   False, False, 0, 0],
            [13, 1, VIOLET, 40, -0.8 * pi,  False, 0,     0,  0,   False, False, 0, 0],
            [17, 1, VIOLET, 29, 0.82 * pi,  False, 0,     0,  0,   False, False, 0, 0],
            [11, 1, VIOLET, 8,  0.5 * pi,   False, 0,     0,  0,   False, False, 0, 0],
            [11, 1, VIOLET, 38, 0.6 * pi,   False, 0,     0,  0,   False, False, 0, 0],
            [12, 1, VIOLET, 22, 0.65 * pi,  False, 0,     0,  0,   False, False, 0, 0]]

ANT_HEALTH_STATES = ((0, ),)
###############################################################################
SCARAB_BODY = [[28, 4, BLUE,   0,  0.00,       True, 0.03,  22, 0,   True, False],
               [20, 2, ORANGE, 0,  0.00,       True, 0.028, 18, 0,   True, True],
               [8,  1, ORANGE, 0,  0.00,       True, 0.014, 8,  0,   True, True,  22],
               [16, 2, BLUE,   38, 0.25 * pi,  True, 0.02,  12, 0,   True, False],
               [16, 2, BLUE,   38, -0.25 * pi, True, 0.02,  12, 0.3, True, False],
               [16, 2, BLUE,   38, 0.75 * pi,  True, 0.02,  12, 0.5, True, False],
               [16, 2, BLUE,   38, -0.75 * pi, True, 0.02,  12, 0.7, True, False],
               [12, 2, BLUE,   36, pi,         True, 0.015, 9,  0.9, True, False],

               [14, 1, VIOLET, 14, -0.15 * pi, False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 22, -0.35 * pi, False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 32, 0.22 * pi,  False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 32, -0.22 * pi, False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 30, -0.75 * pi, False, 0,     0,  0,   False, False, 0, 0],
               [13, 1, VIOLET, 40, -0.8 * pi,  False, 0,     0,  0,   False, False, 0, 0],
               [17, 1, VIOLET, 29, 0.82 * pi,  False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 8,  0.5 * pi,   False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 38, 0.6 * pi,   False, 0,     0,  0,   False, False, 0, 0],
               [12, 1, VIOLET, 22, 0.65 * pi,  False, 0,     0,  0,   False, False, 0, 0]]

SCARAB_HEALTH_STATES = ((6, ),
                        (3, (7, 8)),)
###############################################################################
GULL_BODY = [[32, 4, BLUE,   6,  0.00,       True, 0.03,  20, 0,   True,  False],
             [16, 2, BLUE,   40, 0.72 * pi,  True, 0.023, 14, 0.1, True,  False],
             [16, 2, BLUE,   40, -0.72 * pi, True, 0.023, 14, 0.5, True,  False],
             [16, 2, BLUE,   40, pi,         True, 0.023, 14, 0.1, False, False],
             [13, 1, BLUE,   66, 0.72 * pi,  True, 0.019, 11, 0.3, True,  False],
             [13, 1, BLUE,   66, -0.72 * pi, True, 0.019, 11, 0.7, True,  False],
             [20, 2, ORANGE, 0,  0.00,       True, 0.028, 18, 0,   True,  True],
             [8,  1, ORANGE, 0,  0.00,       True, 0.014, 8,  0,   True,  True,  23],

             [14, 1, VIOLET, 14, -0.15 * pi, False, 0,     0,  0,   False, False, 0, 0],
             [11, 1, VIOLET, 22, -0.35 * pi, False, 0,     0,  0,   False, False, 0, 0],
             [11, 1, VIOLET, 32, 0.22 * pi,  False, 0,     0,  0,   False, False, 0, 0],
             [11, 1, VIOLET, 32, -0.22 * pi, False, 0,     0,  0,   False, False, 0, 0],
             [11, 1, VIOLET, 30, -0.75 * pi, False, 0,     0,  0,   False, False, 0, 0],
             [13, 1, VIOLET, 40, -0.8 * pi,  False, 0,     0,  0,   False, False, 0, 0],
             [17, 1, VIOLET, 29, 0.82 * pi,  False, 0,     0,  0,   False, False, 0, 0],
             [11, 1, VIOLET, 8,  0.5 * pi,   False, 0,     0,  0,   False, False, 0, 0],
             [11, 1, VIOLET, 38, 0.6 * pi,   False, 0,     0,  0,   False, False, 0, 0],
             [12, 1, VIOLET, 22, 0.65 * pi,  False, 0,     0,  0,   False, False, 0, 0]]

GULL_HEALTH_STATES = ((5, (3, 4)),
                      (4, (3, 6)),
                      (2, (1, 3), (4, 6)),
                      (1, (1, 6)))
###############################################################################
MOTHER_BODY = [[12, 1, BLUE,         141, 0.95 * pi,  True,  0.02,  12, 0.2, True, False],
                   [14, 2, BLUE,         121, 0.95 * pi,  True,  0.023, 13, 0.5, True, False],
                   [20, 3, BLUE,         96,  0.95 * pi,  True,  0.028, 16, 0.8, True, False],
                   [12, 1, BLUE,         137, 0.32 * pi,  True,  0.02,  12, 0.1, True, False],
                   [14, 2, BLUE,         117, 0.32 * pi,  True,  0.021, 13, 0.3, True, False],
                   [20, 3, BLUE,         92,  0.32 * pi,  True,  0.028, 16, 0.8, True, False],
                   [12, 1, BLUE,         145, 0.63 * pi,  True,  0.02,  12, 0.7, True, False],
                   [14, 2, BLUE,         125, 0.63 * pi,  True,  0.021, 13, 0.1, True, False],
                   [20, 3, BLUE,         100, 0.63 * pi,  True,  0.028, 16, 0.5, True, False],
                   [12, 1, BLUE,         130, -0.39 * pi, True,  0.02,  12, 0.4, True, False],
                   [14, 2, BLUE,         110, -0.4 * pi,  True,  0.021, 13, 0.7, True, False],
                   [20, 3, BLUE,         85,  -0.42 * pi, True,  0.028, 16, 0.1, True, False],
                   [12, 1, BLUE,         150, -0.76 * pi, True,  0.02,  12, 0,   True, False],
                   [14, 2, BLUE,         130, -0.76 * pi, True,  0.023, 13, 0.3, True, False],
                   [20, 3, BLUE,         105, -0.76 * pi, True,  0.028, 16, 0.7, True, False],
                   [28, 1, BLUE,         72,  0.23 * pi,  True,  0.02,  12, 0.4, True, False],
                   [28, 1, BLUE,         65,  0.45 * pi,  True,  0.02,  12, 0.1, True, False],
                   [28, 1, BLUE,         70,  0.66 * pi,  True,  0.02,  12, 0.8, True, False],
                   [28, 1, BLUE,         70,  0.87 * pi,  True,  0.02,  12, 0.5, True, False],
                   [28, 1, BLUE,         70,  -0.94 * pi, True,  0.02,  12, 0.2, True, False],
                   [28, 1, BLUE,         70,  -0.75 * pi, True,  0.02,  12, 0.9, True, False],
                   [28, 1, BLUE,         62,  -0.57 * pi, True,  0.02,  12, 0.6, True, False],
                   [28, 1, BLUE,         63,  -0.37 * pi, True,  0.02,  12, 0.3, True, False],
                   [28, 1, BLUE,         66,  -0.16 * pi, True,  0.02,  12, 0,   True, False],

                   [13, 1, ORANGE,       56,  0.26 * pi,  True,  0.017, 10, 0.3, True, False],
                   [13, 1, ORANGE,       56,  -0.26 * pi, True,  0.017, 10, 0.5, True, False],
                   [13, 1, ORANGE,       56,  0.74 * pi,  True,  0.017, 10, 0.7, True, False],
                   [13, 1, ORANGE,       56,  -0.74 * pi, True,  0.017, 10, 0.0, True, False],
                   [5,  1, LIGHT_ORANGE, 0,   0.00,       False, 0,     0,  0,   True, False, 0, 0, False, 0, True, 40, 0],
                   [5,  1, LIGHT_ORANGE, 0,   0.00,       False, 0,     0,  0,   True, False, 0, 0, False, 0, True, 40, 0.65 * pi],

                   [14, 1, VIOLET,       14, -0.15 * pi,  False, 0,     0,  0,   False, False, 0, 0],
                   [11, 1, VIOLET,       22, -0.35 * pi,  False, 0,     0,  0,   False, False, 0, 0],
                   [11, 1, VIOLET,       32, 0.22 * pi,   False, 0,     0,  0,   False, False, 0, 0],
                   [11, 1, VIOLET,       32, -0.22 * pi,  False, 0,     0,  0,   False, False, 0, 0],
                   [11, 1, VIOLET,       30, -0.75 * pi,  False, 0,     0,  0,   False, False, 0, 0],
                   [13, 1, VIOLET,       40, -0.8 * pi,   False, 0,     0,  0,   False, False, 0, 0],
                   [17, 1, VIOLET,       29, 0.82 * pi,   False, 0,     0,  0,   False, False, 0, 0],
                   [11, 1, VIOLET,       8,  0.5 * pi,    False, 0,     0,  0,   False, False, 0, 0],
                   [11, 1, VIOLET,       38, 0.6 * pi,    False, 0,     0,  0,   False, False, 0, 0],
                   [12, 1, VIOLET,       22, 0.65 * pi,   False, 0,     0,  0,   False, False, 0, 0]]

MOTHER_HEALTH_STATES = ((90, ),
                            (60, (0, 1), (3, 4), (6, 7), (9, 10), (12, 13)),
                            (30, (0, 2), (3, 5), (6, 8), (9, 11), (12, 14)),)
###############################################################################
COCKROACH_BODY = [[12, 1, BLUE,   22, 0.66 * pi,  True, 0.017, 10, 0.3, True, False],
                  [12, 1, BLUE,   22, -0.66 * pi, True, 0.017, 10, 0.7, True, False],
                  [10, 1, BLUE,   39, 0.59 * pi,  True, 0.012, 7,  0.4, True, False],
                  [10, 1, BLUE,   39, -0.59 * pi, True, 0.012, 7,  0.8, True, False],

                  [13, 1, BLUE,   55, 0.48 * pi,  True, 0.019, 11, 0.1, True, False],
                  [13, 1, BLUE,   55, -0.48 * pi, True, 0.019, 11, 0.5, True, False],
                  [10, 1, BLUE,   38, 0.47 * pi,  True, 0.012, 7,  0.1, True, False],
                  [10, 1, BLUE,   38, -0.47 * pi, True, 0.012, 7,  0.5, True, False],
                  [10, 1, BLUE,   47, 0.39 * pi,  True, 0.012, 7,  0.2, True, False],
                  [10, 1, BLUE,   47, -0.39 * pi, True, 0.012, 7,  0.9, True, False],

                  [10, 1, BLUE,   51, 0.29 * pi,  True, 0.012, 7,  0.0, True, False],
                  [10, 1, BLUE,   51, -0.29 * pi, True, 0.012, 7,  0.6, True, False],
                  [10, 1, BLUE,   56, 0.2 * pi,   True, 0.012, 7,  0.1, True, False],
                  [10, 1, BLUE,   56, -0.2 * pi,  True, 0.012, 7,  0.4, True, False],

                  [18, 2, BLUE,   4,  0.00,       True, 0.02,  12, 0,   True, False],
                  [15, 2, ORANGE, 0,  0.00,       True, 0.015, 10, 0,   True, True],
                  [6,  1, ORANGE, 0, 0.00,        True, 0.01,  6,  0,   True, True,  19],

                  [14, 1, VIOLET, 14, -0.15 * pi, False, 0,    0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET, 22, -0.35 * pi, False, 0,    0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET, 32, 0.22 * pi,  False, 0,    0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET, 32, -0.22 * pi, False, 0,    0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET, 30, -0.75 * pi, False, 0,    0,  0,   False, False, 0, 0],
                  [13, 1, VIOLET, 40, -0.8 * pi,  False, 0,    0,  0,   False, False, 0, 0],
                  [17, 1, VIOLET, 29, 0.82 * pi,  False, 0,    0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET, 8,  0.5 * pi,   False, 0,    0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET, 38, 0.6 * pi,   False, 0,    0,  0,   False, False, 0, 0],
                  [12, 1, VIOLET, 22, 0.65 * pi,  False, 0,    0,  0,   False, False, 0, 0]]

COCKROACH_HEALTH_STATES = ((10, ),
                           (9, (12, 14)),
                           (7, (4, 6), (12, 14)),
                           (5, (4, 6), (10, 14)),
                           (3, (2, 14), (15, 17)))
###############################################################################
BOMBERSHOOTER_BODY = [[18, 2, BLUE,         38,  0.54 * pi,   True,  0.027,  16, 0.9, True, False],
                      [18, 2, BLUE,         38,  -0.54 * pi,  True,  0.027,  16, 0.6, True, False],
                      [18, 2, BLUE,         76,  0.17 * pi,   True,  0.027,  16, 0.3, True, False],
                      [18, 2, BLUE,         76,  -0.17 * pi,  True,  0.027,  16, 0.1, True, False],
                      [18, 2, BLUE,         27,  0.73 * pi,   True,  0.027,  16, 0.5, True, False],
                      [18, 2, BLUE,         27,  -0.73 * pi,  True,  0.027,  16, 0.2, True, False],
                      [18, 2, BLUE,         60,  0.83 * pi,   True,  0.027,  16, 0.1, True, False],
                      [18, 2, BLUE,         60,  -0.83 * pi,  True,  0.027,  16, 0.7, True, False],
                      [18, 2, BLUE,         85,  0.9 * pi,    True,  0.027,  16, 0.4, True, False],
                      [18, 2, BLUE,         85,  -0.9 * pi,   True,  0.0227, 16, 0.9, True, False],
                      [11, 1, BLUE,         99,  0.15 * pi,   True,  0.016,  9,  0.4, True, False],
                      [11, 1, BLUE,         99,  -0.15 * pi,  True,  0.016,  9,  0.8, True, False],
                      [11, 1, BLUE,         81,  0.27 * pi,   True,  0.016,  9,  0.1, True, False],
                      [11, 1, BLUE,         81,  -0.27 * pi,  True,  0.016,  9,  0.6, True, False],
                      [11, 1, BLUE,         108, 0.91 * pi,   True,  0.016,  9,  0.5, True, False],
                      [11, 1, BLUE,         108, -0.91 * pi,  True,  0.016,  9,  0.7, True, False],
                      [11, 1, BLUE,         90,  0.82 * pi,   True,  0.016,  9,  0.3, True, False],
                      [11, 1, BLUE,         90,  -0.82 * pi,  True,  0.016,  9,  0.9, True, False],
                      [38, 4, BLUE,         30,  0.00,        True,  0.046,  28, 0,   True, False],
                      [19, 2, ORANGE,       30,  0.00,        True,  0.035,  21, 0,   True, True],
                      [9,  1, ORANGE,       30,  0.00,        True,  0.014,  8,  0,   True, True, 23],
                      [8,  1, ORANGE,       33,  0.85 * pi,   True,  0.007,  5,  0.9, True, False],
                      [8,  1, ORANGE,       33,  -0.85 * pi,  True,  0.007,  5,  0.6, True, False],
                      [8,  1, ORANGE,       43,  0.888 * pi,  True,  0.007,  5,  0.7, True, False],
                      [8,  1, ORANGE,       43,  -0.888 * pi, True,  0.007,  5,  0.4, True, False],
                      [8,  1, ORANGE,       54,  0.91 * pi,   True,  0.007,  5,  0.5, True, False],
                      [8,  1, ORANGE,       54,  -0.91 * pi,  True,  0.007,  5,  0.2, True, False],
                      [8,  1, ORANGE,       65,  0.925 * pi,  True,  0.007,  5,  0.3, True, False],
                      [8,  1, ORANGE,       65,  -0.925 * pi, True,  0.007,  5,  0.0, True, False],
                      [8,  1, ORANGE,       76,  0.935 * pi,  True,  0.007,  5,  0.1, True, False],
                      [8,  1, ORANGE,       76,  -0.935 * pi, True,  0.007,  5,  0.8, True, False],
                      [8,  1, ORANGE,       87,  0.944 * pi,  True,  0.007,  5,  0.9, True, False],
                      [8,  1, ORANGE,       87,  -0.944 * pi, True,  0.007,  5,  0.6, True, False],
                      [13, 2, LIGHT_ORANGE, 33,  0.85 * pi,   False, 0,      0,  0,   True, False, 0, 0, True, pi],
                      [13, 2, LIGHT_ORANGE, 33,  -0.85 * pi,  False, 0,      0,  0,   True, False, 0, 0, True, pi],
                      [14, 2, ORANGE,       30,  pi,          True,  0.019,  12, 0,   True, False],

                      [14, 1, VIOLET,       14, -0.15 * pi,   False, 0,      0,  0,   False, False, 0, 0],
                      [11, 1, VIOLET,       22, -0.35 * pi,   False, 0,      0,  0,   False, False, 0, 0],
                      [11, 1, VIOLET,       32, 0.22 * pi,    False, 0,      0,  0,   False, False, 0, 0],
                      [11, 1, VIOLET,       32, -0.22 * pi,   False, 0,      0,  0,   False, False, 0, 0],
                      [11, 1, VIOLET,       30, -0.75 * pi,   False, 0,      0,  0,   False, False, 0, 0],
                      [13, 1, VIOLET,       40, -0.8 * pi,    False, 0,      0,  0,   False, False, 0, 0],
                      [17, 1, VIOLET,       29, 0.82 * pi,    False, 0,      0,  0,   False, False, 0, 0],
                      [11, 1, VIOLET,       8,  0.5 * pi,     False, 0,      0,  0,   False, False, 0, 0],
                      [11, 1, VIOLET,       38, 0.6 * pi,     False, 0,      0,  0,   False, False, 0, 0],
                      [12, 1, VIOLET,       22, 0.65 * pi,    False, 0,      0,  0,   False, False, 0, 0]]

BOMBERSHOOTER_HEALTH_STATES = ((27, ),
                               (24, (16, 18)),
                               (21, (12, 14), (16, 18)),
                               (18, (10, 18)),
                               (12, (2, 4), (10, 18)))
###############################################################################
BUG_BODY = [[15, 2, BLUE,  29, 0.5 * pi,   True, 0.018, 11, 0.3, True, False],
            [15, 2, BLUE,  29, -0.5 * pi,  True, 0.018, 11, 0,   True, False],
            [10, 1, BLUE,  40, 0.64 * pi,  True, 0.01,  6,  0.3, True, False],
            [10, 1, BLUE,  40, -0.64 * pi, True, 0.01,  6,  0,   True, False],
            [21, 3, BLUE,  0,  0,          True, 0.024, 15, 0,   True, False],
            [15, 2, BLUE,  27, pi,         True, 0.018, 11, 0.6, True, False],
            [17, 2, ORANGE, 0, 0,          True, 0.03,  18, 0,   True, True],
            [7,  1, ORANGE, 0, 0,          True, 0.01,  6,  0,   True, True,  17],

            [14, 1, VIOLET, 4, -0.15 * pi,   False, 0,     0,  0,   False, False, 0, 0],
            [11, 1, VIOLET, 22, -0.35 * pi,  False, 0,     0,  0,   False, False, 0, 0],
            [11, 1, VIOLET, 32, 0.22 * pi,   False, 0,     0,  0,   False, False, 0, 0],
            [11, 1, VIOLET, 32, -0.22 * pi,  False, 0,     0,  0,   False, False, 0, 0],
            [11, 1, VIOLET, 30, -0.75 * pi,  False, 0,     0,  0,   False, False, 0, 0],
            [13, 1, VIOLET, 40, -0.8 * pi,   False, 0,     0,  0,   False, False, 0, 0],
            [17, 1, VIOLET, 29, 0.82 * pi,   False, 0,     0,  0,   False, False, 0, 0],
            [11, 1, VIOLET, 8,  0.5 * pi,    False, 0,     0,  0,   False, False, 0, 0],
            [11, 1, VIOLET, 38, 0.6 * pi,    False, 0,     0,  0,   False, False, 0, 0],
            [12, 1, VIOLET, 22, 0.65 * pi,   False, 0,     0,  0,   False, False, 0, 0]]

BUG_HEALTH_STATES = ((0, ),)
###############################################################################
AMEBA_BODY = []
for i in range(1, 21):
    AMEBA_BODY.append([5, 1, BLUE, 23 + 5*cos(i * 3*pi/10), i*pi/10, False, 0, 0, 0, True, False])
AMEBA_BODY.extend([[11, 2, BLUE,   11, 0,          True,  0.014, 8, 0.1, True, False],
                   [11, 2, BLUE,   11, 2*pi/3,     True,  0.014, 8, 0.4, True, False],
                   [11, 2, BLUE,   11, -2*pi/3,    True,  0.014, 8, 0.7, True, False],

                   [14, 1, VIOLET, 14, -0.15 * pi, False, 0,     0,  0,  False, False, 0, 0],
                   [11, 1, VIOLET, 22, -0.35 * pi, False, 0,     0,  0,  False, False, 0, 0],
                   [11, 1, VIOLET, 32, 0.22 * pi,  False, 0,     0,  0,  False, False, 0, 0],
                   [11, 1, VIOLET, 32, -0.22 * pi, False, 0,     0,  0,  False, False, 0, 0],
                   [11, 1, VIOLET, 30, -0.75 * pi, False, 0,     0,  0,  False, False, 0, 0],
                   [13, 1, VIOLET, 40, -0.8 * pi,  False, 0,     0,  0,  False, False, 0, 0],
                   [17, 1, VIOLET, 29, 0.82 * pi,  False, 0,     0,  0,  False, False, 0, 0],
                   [11, 1, VIOLET, 8,  0.5 * pi,   False, 0,     0,  0,  False, False, 0, 0],
                   [11, 1, VIOLET, 38, 0.6 * pi,   False, 0,     0,  0,  False, False, 0, 0],
                   [12, 1, VIOLET, 22, 0.65 * pi,  False, 0,     0,  0,  False, False, 0, 0]])

AMEBA_HEALTH_STATES = ((4,),
                       (3, (22, 23)),
                       (2, (21, 23)),
                       (1, (20, 23)))
###############################################################################
CELL_BODY = []
for i in range(1, 13):
    CELL_BODY.append([6, 1, BLUE, 20, i*pi/6, False, 0, 0, 0, True, False])
CELL_BODY.extend([[14, 2, BLUE,   0,  0,          True,  0.014, 8, 0.1, True,  False],

                  [14, 1, VIOLET, 14, -0.15 * pi, False, 0,     0, 0,   False, False, 0, 0],
                  [11, 1, VIOLET, 22, -0.35 * pi, False, 0,     0, 0,   False, False, 0, 0],
                  [11, 1, VIOLET, 32, 0.22 * pi,  False, 0,     0, 0,   False, False, 0, 0],
                  [11, 1, VIOLET, 32, -0.22 * pi, False, 0,     0, 0,   False, False, 0, 0],
                  [11, 1, VIOLET, 30, -0.75 * pi, False, 0,     0, 0,   False, False, 0, 0],
                  [13, 1, VIOLET, 40, -0.8 * pi,  False, 0,     0, 0,   False, False, 0, 0],
                  [17, 1, VIOLET, 29, 0.82 * pi,  False, 0,     0, 0,   False, False, 0, 0],
                  [11, 1, VIOLET, 8,  0.5 * pi,   False, 0,     0, 0,   False, False, 0, 0],
                  [11, 1, VIOLET, 38, 0.6 * pi,   False, 0,     0, 0,   False, False, 0, 0],
                  [12, 1, VIOLET, 22, 0.65 * pi,  False, 0,     0, 0,   False, False, 0, 0]])

CELL_HEALTH_STATES = ((4,),
                      (3, (0, 1), (4, 5), (8, 9)),
                      (2, (0, 4), (5, 6), (7, 8), (9, 10), (11, 12)),
                      (1, (0, 4), (5, 6), (7, 11)))
###############################################################################
INFUSORIA_BODY = [[10, 1, BLUE,   26, 5*pi/6,     True,  0.012, 7,  0.3, True,  False],
                  [10, 1, BLUE,   26, -5*pi/6,    True,  0.012, 7,  0.7, True,  False],
                  [18, 2, BLUE,   0,  0,          True,  0.017, 10, 0,   True,  False],
                  [8,  1, BLUE,   22, 0,          True,  0.008, 5,  0.5, True,  False],

                  [14, 1, VIOLET, 14, -0.15 * pi, False, 0,     0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET, 22, -0.35 * pi, False, 0,     0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET, 32, 0.22 * pi,  False, 0,     0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET, 32, -0.22 * pi, False, 0,     0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET, 30, -0.75 * pi, False, 0,     0,  0,   False, False, 0, 0],
                  [13, 1, VIOLET, 40, -0.8 * pi,  False, 0,     0,  0,   False, False, 0, 0],
                  [17, 1, VIOLET, 29, 0.82 * pi,  False, 0,     0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET, 8,  0.5 * pi,   False, 0,     0,  0,   False, False, 0, 0],
                  [11, 1, VIOLET, 38, 0.6 * pi,   False, 0,     0,  0,   False, False, 0, 0],
                  [12, 1, VIOLET, 22, 0.65 * pi,  False, 0,     0,  0,   False, False, 0, 0]]

INFUSORIA_HEALTH_STATES = ((2,),
                           (1, (3, 4)))
###############################################################################
BABY_BODY = [[8,  1, BLUE,   14, 0.8 * pi,   True,  0.01,  6, 0.7, True,  False],
             [11, 1, BLUE,   0,  0,          True,  0.013, 8, 0.3, True,  False],
             [8,  1, BLUE,   14, -0.8 * pi,  True,  0.01,  6, 0.5, True,  False],

             [14, 1, VIOLET, 14, -0.15 * pi, False, 0,     0,  0,  False, False, 0, 0],
             [11, 1, VIOLET, 22, -0.35 * pi, False, 0,     0,  0,  False, False, 0, 0],
             [11, 1, VIOLET, 32, 0.22 * pi,  False, 0,     0,  0,  False, False, 0, 0],
             [11, 1, VIOLET, 32, -0.22 * pi, False, 0,     0,  0,  False, False, 0, 0],
             [11, 1, VIOLET, 30, -0.75 * pi, False, 0,     0,  0,  False, False, 0, 0],
             [13, 1, VIOLET, 40, -0.8 * pi,  False, 0,     0,  0,  False, False, 0, 0],
             [17, 1, VIOLET, 29, 0.82 * pi,  False, 0,     0,  0,  False, False, 0, 0],
             [11, 1, VIOLET, 8,  0.5 * pi,   False, 0,     0,  0,  False, False, 0, 0],
             [11, 1, VIOLET, 38, 0.6 * pi,   False, 0,     0,  0,  False, False, 0, 0],
             [12, 1, VIOLET, 22, 0.65 * pi,  False, 0,     0,  0,  False, False, 0, 0]]

BABY_HEALTH_STATES = ((0, ),)
###############################################################################
BEETLE_BODY = [[12, 1, BLUE,   113, 0.075 * pi,  True, 0.02,  12, 0.1, True, False],
               [12, 1, BLUE,   113, -0.075 * pi, True, 0.02,  12, 0.6, True, False],
               [12, 1, BLUE,   94,  0.06 * pi,   True, 0.02,  12, 0.4, True, False],
               [12, 1, BLUE,   94,  -0.06 * pi,  True, 0.02,  12, 0.9, True, False],
               [12, 1, BLUE,   119, 0.13 * pi,   True, 0.02,  12, 0.7, True, False],
               [12, 1, BLUE,   119, -0.13 * pi,  True, 0.02,  12, 0.2, True, False],
               [12, 1, BLUE,   122, 0.18 * pi,   True, 0.02,  12, 0.0, True, False],
               [12, 1, BLUE,   122, -0.18 * pi,  True, 0.02,  12, 0.5, True, False],
               [12, 1, BLUE,   122, 0.23 * pi,   True, 0.02,  12, 0.3, True, False],
               [12, 1, BLUE,   122, -0.23 * pi,  True, 0.02,  12, 0.8, True, False],
               # 10
               [12, 1, BLUE,   116, 0.28 * pi,   True, 0.02,  12, 0.6, True, False],
               [12, 1, BLUE,   116, -0.28 * pi,  True, 0.02,  12, 0.1, True, False],
               [19, 2, BLUE,   83,  0.2 * pi,    True, 0.026, 15, 0.1, True, False],
               [19, 2, BLUE,   83,  -0.2 * pi,   True, 0.026, 15, 0.3, True, False],
               [19, 2, BLUE,   74,  0.74 * pi,   True, 0.026, 15, 0.4, True, False],
               [19, 2, BLUE,   74,  -0.74 * pi,  True, 0.026, 15, 0.9, True, False],
               [19, 2, BLUE,   81,  0.5 * pi,    True, 0.026, 15, 0.8, True, False],
               [19, 2, BLUE,   81,  -0.5 * pi,   True, 0.026, 15, 0.0, True, False],
               [19, 2, BLUE,   54,  0.5 * pi,    True, 0.026, 15, 0.2, True, False],
               [19, 2, BLUE,   54,  -0.5 * pi,   True, 0.026, 15, 0.5, True, False],
               # 20
               [46, 2, BLUE,   50,  0.00,        True, 0.027, 16, 0,   True, False],
               [60, 2, BLUE,   25,  pi,          True, 0.034, 20, 0.4, True, False],
               [19, 2, BLUE,   92,  0.82 * pi,   True, 0.026, 15, 0.6, True, False],
               [19, 2, BLUE,   92,  -0.82 * pi,  True, 0.026, 15, 0.9, True, False],
               [19, 2, BLUE,   94,  pi,          True, 0.026, 15, 0.2, True, False],
               [20, 2, ORANGE, 58,  0.00,        True, 0.033, 19, 0.0, True, True],
               [9,  1, ORANGE, 58,  0.00,        True, 0.016, 9,  0,   True, True, 25],
               [27, 3, ORANGE, 35,  pi,          True, 0.044, 25, 0.0, True, True],
               [11, 1, ORANGE, 35,  pi,          True, 0.017, 10, 0,   True, True, 35],

               [14, 1, VIOLET, 4, -0.15 * pi,   False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 22, -0.35 * pi,  False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 32, 0.22 * pi,   False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 32, -0.22 * pi,  False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 30, -0.75 * pi,  False, 0,     0,  0,   False, False, 0, 0],
               [13, 1, VIOLET, 40, -0.8 * pi,   False, 0,     0,  0,   False, False, 0, 0],
               [17, 1, VIOLET, 29, 0.82 * pi,   False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 8,  0.5 * pi,    False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 38, 0.6 * pi,    False, 0,     0,  0,   False, False, 0, 0],
               [12, 1, VIOLET, 22, 0.65 * pi,   False, 0,     0,  0,   False, False, 0, 0]]

BEETLE_HEALTH_STATES = ((30, ),
                        (27, (10, 12)),
                        (24, (8, 12)),
                        (21, (6, 12)),
                        (18, (4, 12)),
                        (15, (0, 12)),
                        (12, (0, 14)),
                        (6, (0, 21), (25, 27)),
                        (3, (0, 21), (24, 27)))
###############################################################################
SPREADER_BODY = [[14, 2, BLUE,   45, 0.1 * pi,  False, 0,     0,  0,   True, False],
                 [14, 2, BLUE,   45, 0.3 * pi,  False, 0,     0,  0,   True, False],
                 [14, 2, BLUE,   45, 0.5 * pi,  False, 0,     0,  0,   True, False],
                 [14, 2, BLUE,   45, 0.7 * pi,  False, 0,     0,  0,   True, False],
                 [14, 2, BLUE,   45, 0.9 * pi,  False, 0,     0,  0,   True, False],

                 [14, 2, BLUE,   45, -0.9 * pi, False, 0,     0,  0,   True, False],
                 [14, 2, BLUE,   45, -0.7 * pi, False, 0,     0,  0,   True, False],
                 [14, 2, BLUE,   45, -0.5 * pi, False, 0,     0,  0,   True, False],
                 [14, 2, BLUE,   45, -0.3 * pi, False, 0,     0,  0,   True, False],
                 [14, 2, BLUE,   45, -0.1 * pi, False, 0,     0,  0,   True, False],

                 [43, 2, BLUE,   0,  0.00,      True,  0.028, 17, 0,   True, False],
                 [20, 3, ORANGE, 0,  0.00,      True,  0.026, 15, 0,   True, True],
                 [7,  1, ORANGE, 27, 0.00,      True,  0.011, 7,  0.3, True, False],
                 [7,  1, ORANGE, 38, 0.00,      True,  0.011, 7,  0.6, True, False],
                 [7,  1, ORANGE, 27, 0.2 * pi,  True,  0.011, 7,  0.7, True, False],
                 [7,  1, ORANGE, 38, 0.2 * pi,  True,  0.011, 7,  0.0, True, False],
                 [7,  1, ORANGE, 27, 0.4 * pi,  True,  0.011, 7,  0.1, True, False],
                 [7,  1, ORANGE, 38, 0.4 * pi,  True,  0.011, 7,  0.4, True, False],
                 [7,  1, ORANGE, 27, 0.6 * pi,  True,  0.011, 7,  0.5, True, False],
                 [7,  1, ORANGE, 38, 0.6 * pi,  True,  0.011, 7,  0.8, True, False],
                 [7,  1, ORANGE, 27, 0.8 * pi,  True,  0.011, 7,  0.9, True, False],
                 [7,  1, ORANGE, 38, 0.8 * pi,  True,  0.011, 7,  0.2, True, False],
                 [7,  1, ORANGE, 27, pi,        True,  0.011, 7,  0.3, True, False],
                 [7,  1, ORANGE, 38, pi,        True,  0.011, 7,  0.6, True, False],
                 [7,  1, ORANGE, 27, -0.8 * pi, True,  0.011, 7,  0.7, True, False],
                 [7,  1, ORANGE, 38, -0.8 * pi, True,  0.011, 7,  0.0, True, False],
                 [7,  1, ORANGE, 27, -0.6 * pi, True,  0.011, 7,  0.1, True, False],
                 [7,  1, ORANGE, 38, -0.6 * pi, True,  0.011, 7,  0.4, True, False],
                 [7,  1, ORANGE, 27, -0.4 * pi, True,  0.011, 7,  0.5, True, False],
                 [7,  1, ORANGE, 38, -0.4 * pi, True,  0.011, 7,  0.8, True, False],
                 [7,  1, ORANGE, 27, -0.2 * pi, True,  0.011, 7,  0.9, True, False],
                 [7,  1, ORANGE, 38, -0.2 * pi, True,  0.011, 7,  0.2, True, False],

                 [14, 1, VIOLET, 4, -0.15 * pi,  False, 0,    0,  0,   False, False, 0, 0],
                 [11, 1, VIOLET, 22, -0.35 * pi, False, 0,    0,  0,   False, False, 0, 0],
                 [11, 1, VIOLET, 32, 0.22 * pi,  False, 0,    0,  0,   False, False, 0, 0],
                 [11, 1, VIOLET, 32, -0.22 * pi, False, 0,    0,  0,   False, False, 0, 0],
                 [11, 1, VIOLET, 30, -0.75 * pi, False, 0,    0,  0,   False, False, 0, 0],
                 [13, 1, VIOLET, 40, -0.8 * pi,  False, 0,    0,  0,   False, False, 0, 0],
                 [17, 1, VIOLET, 29, 0.82 * pi,  False, 0,    0,  0,   False, False, 0, 0],
                 [11, 1, VIOLET, 8,  0.5 * pi,   False, 0,    0,  0,   False, False, 0, 0],
                 [11, 1, VIOLET, 38, 0.6 * pi,   False, 0,    0,  0,   False, False, 0, 0],
                 [12, 1, VIOLET, 22, 0.65 * pi,  False, 0,    0,  0,   False, False, 0, 0]]

SPREADER_HEALTH_STATES = ((18, ),
                          (15, (0, 1), (5, 6)),
                          (12, (0, 2), (5, 7)),
                          (9, (0, 2), (4, 7), (9, 10)),
                          (6, (0, 3), (4, 8), (9, 10)),
                          (3, (0, 10)))
###############################################################################
BIGEGG_BODY = [[80, 5, RED,    0,  0,           True,  0.01,  6,  0,   True,  False],
               [43, 2, BLUE,   0,  0,           True,  0.028, 17, 0,   True,  True],
               [20, 3, ORANGE, 0,  0,           True,  0.026, 15, 0.0, True,  True],
               [8, 1,  ORANGE, 0,  0,           True,  0.011, 7,  0.9, True,  True,  27],

               [14, 1, VIOLET, 4, -0.15 * pi,   False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 22, -0.35 * pi,  False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 32, 0.22 * pi,   False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 32, -0.22 * pi,  False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 30, -0.75 * pi,  False, 0,     0,  0,   False, False, 0, 0],
               [13, 1, VIOLET, 40, -0.8 * pi,   False, 0,     0,  0,   False, False, 0, 0],
               [17, 1, VIOLET, 29, 0.82 * pi,   False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 8,  0.5 * pi,    False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 38, 0.6 * pi,    False, 0,     0,  0,   False, False, 0, 0],
               [12, 1, VIOLET, 22, 0.65 * pi,   False, 0,     0,  0,   False, False, 0, 0]]

BIGEGG_HEALTH_STATES = ((0, ),)
###############################################################################
SPIDER_BODY = [[23, 3, BLUE,   101, 0.5 * pi,   True, 0.032, 19, 0.0, True, False],
               [23, 3, BLUE,   101, -0.5 * pi,  True, 0.032, 19, 0.3, True, False],
               [23, 3, BLUE,   122, 0.79 * pi,  True, 0.032, 19, 0.6, True, False],
               [23, 3, BLUE,   122, -0.79 * pi, True, 0.032, 19, 0.9, True, False],
               [23, 3, BLUE,   104, 0.23 * pi,  True, 0.032, 19, 0.5, True, False],
               [23, 3, BLUE,   104, -0.23 * pi, True, 0.032, 19, 0.2, True, False],
               [23, 3, BLUE,   75,  0.00,       True, 0.032, 19, 0.7, True, False],
               # 7
               [18, 2, BLUE,   70,  0.5 * pi,   True, 0.026, 15, 0.0, True, False],
               [18, 2, BLUE,   70,  -0.5 * pi,  True, 0.026, 15, 0.3, True, False],
               [18, 2, BLUE,   74,  0.2 * pi,   True, 0.026, 15, 0.6, True, False],
               [18, 2, BLUE,   74,  -0.2 * pi,  True, 0.026, 15, 0.8, True, False],
               # 11
               [36, 1, BLUE,   35,  0.28 * pi,  True, 0.024, 14, 0.8, True, False],
               [36, 1, BLUE,   35,  -0.28 * pi, True, 0.024, 14, 0.5, True, False],
               [26, 1, BLUE,   12,  0.00,       True, 0.02,  12, 0,   True, False],
               [70, 3, BLUE,   70,  pi,         True, 0.055, 33, 0.2, True, False],
               # 15
               [11, 1, BLUE,   64,  0.45 * pi,  True, 0.017, 10, 0.7, True, False],
               [11, 1, BLUE,   64,  -0.45 * pi, True, 0.017, 10, 0.4, True, False],
               [11, 1, BLUE,   74,  0.3 * pi,   True, 0.017, 10, 0.1, True, False],
               [11, 1, BLUE,   74,  -0.3 * pi,  True, 0.017, 10, 0.9, True, False],
               # 19
               [23, 3, BLUE,   82,  -0.63 * pi, True, 0.032, 19, 0.2, False, False],
               [23, 3, BLUE,   82,  0.63 * pi,  True, 0.032, 19, 0.7, False, False],
               [70, 3, BLUE,   2,   pi,         True, 0.055, 33, 0.2, False, False],
               # 22
               [11, 1, ORANGE, 70,  pi,         True, 0.014, 8,  0.1, True, True,  34, -0.2 * pi],
               [11, 1, ORANGE, 70,  pi,         True, 0.014, 8,  0.4, True, True,  34, 0.2 * pi],
               [11, 1, ORANGE, 70,  pi,         True, 0.014, 8,  0.7, True, True,  50, -0.13 * pi],
               [11, 1, ORANGE, 70,  pi,         True, 0.014, 8,  0.9, True, True,  50, 0.13 * pi],
               [30, 4, ORANGE, 70,  pi,         True, 0.038, 23, 0.0, True, True],
               [12, 1, ORANGE, 70,  pi,         True, 0.017, 10, 0.6, True, True,  38, -0.78 * pi],
               [12, 1, ORANGE, 70,  pi,         True, 0.017, 10, 0.9, True, True,  38, 0.78 * pi],
               [19, 3, ORANGE, 26,  0.00,       True, 0.026, 15, 0.0, True, True],
               [8,  1, ORANGE, 26,  0.00,       True, 0.011, 7,  0.5, True, True,  24],

               [14, 1, VIOLET, 4, -0.15 * pi,   False, 0,    0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 22, -0.35 * pi,  False, 0,    0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 32, 0.22 * pi,   False, 0,    0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 32, -0.22 * pi,  False, 0,    0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 30, -0.75 * pi,  False, 0,    0,  0,   False, False, 0, 0],
               [13, 1, VIOLET, 40, -0.8 * pi,   False, 0,    0,  0,   False, False, 0, 0],
               [17, 1, VIOLET, 29, 0.82 * pi,   False, 0,    0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 8,  0.5 * pi,    False, 0,    0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 38, 0.6 * pi,    False, 0,    0,  0,   False, False, 0, 0],
               [12, 1, VIOLET, 22, 0.65 * pi,   False, 0,    0,  0,   False, False, 0, 0]]

SPIDER_HEALTH_STATES = ((130, (19, 22)),
                        (70, (0, 4), (7, 9), (11, 19), (29, 31)),
                        (50, (0, 6), (7, 9), (11, 19), (29, 31)),
                        (35, (0, 6), (7, 19), (29, 31)),
                        (20, (0, 19), (29, 31)),)
###############################################################################
MACHINEGUNNER_BODY = [[10, 1, BLUE,   63, 0.07 * pi,  True, 0.013, 8,  0.2, True, False],
                      [10, 1, BLUE,   63, -0.07 * pi, True, 0.013, 8,  0.9, True, False],
                      [16, 2, BLUE,   44, 0.00,       True, 0.022, 13, 0.4, True, False],
                      [18, 2, BLUE,   37, 0.72 * pi,  True, 0.026, 15, 0.4, True, False],
                      [18, 2, BLUE,   37, -0.72 * pi, True, 0.026, 15, 0.8, True, False],

                      [38, 2, BLUE,   0,  0.00,       True, 0.035, 20, 0,   True, False],
                      [12, 1, BLUE,   64, 0.72 * pi,  True, 0.016, 10, 0,   True, False],
                      [12, 1, BLUE,   64, -0.72 * pi, True, 0.016, 10, 0.3, True, False],
                      [12, 1, BLUE,   41, pi,         True, 0.016, 10, 0.7, True, False],

                      [18, 3, ORANGE, 0,  0.00,       True, 0.026, 14, 0.0, True, True],
                      [8,  1, ORANGE, 0,  0.00,       True, 0.011, 7,  0.9, True, True, 23],
                      [10, 1, ORANGE, 0,  0.00,       True, 0.013, 8,  0,   True, True, 25, 0.77 * pi],
                      [10, 1, ORANGE, 0,  0.00,       True, 0.013, 8,  0.4, True, True, 25, -0.77 * pi],

                      [14, 1, VIOLET, 4, -0.15 * pi,  False, 0,    0,  0,   False, False, 0, 0],
                      [11, 1, VIOLET, 22, -0.35 * pi, False, 0,    0,  0,   False, False, 0, 0],
                      [11, 1, VIOLET, 32, 0.22 * pi,  False, 0,    0,  0,   False, False, 0, 0],
                      [11, 1, VIOLET, 32, -0.22 * pi, False, 0,    0,  0,   False, False, 0, 0],
                      [11, 1, VIOLET, 30, -0.75 * pi, False, 0,    0,  0,   False, False, 0, 0],
                      [13, 1, VIOLET, 40, -0.8 * pi,  False, 0,    0,  0,   False, False, 0, 0],
                      [17, 1, VIOLET, 29, 0.82 * pi,  False, 0,    0,  0,   False, False, 0, 0],
                      [11, 1, VIOLET, 8,  0.5 * pi,   False, 0,    0,  0,   False, False, 0, 0],
                      [11, 1, VIOLET, 38, 0.6 * pi,   False, 0,    0,  0,   False, False, 0, 0],
                      [12, 1, VIOLET, 22, 0.65 * pi,  False, 0,    0,  0,   False, False, 0, 0]]

MACHINEGUNNER_HEALTH_STATES = ((50, ),
                               (35, (8, 9)),
                               (25, (6, 8)),
                               (15, (6, 9)),
                               (5, (0, 2), (6, 9)))
###############################################################################
TURRET_BODY = [[12, 2, BLUE, 112,  0.41 * pi, False, 0, 0, 0, True, False],
               [12, 2, BLUE, 112,  -0.41 * pi, False, 0, 0, 0, True, False],
               [12, 2, BLUE, 112,  0.59 * pi, False, 0, 0, 0, True, False],
               [12, 2, BLUE, 112,  -0.59 * pi, False, 0, 0, 0, True, False],

               [12, 2, BLUE, 112,  0.09 * pi, False, 0, 0, 0, True, False],
               [12, 2, BLUE, 112,  -0.09 * pi, False, 0, 0, 0, True, False],
               [12, 2, BLUE, 112,  0.91 * pi, False, 0, 0, 0, True, False],
               [12, 2, BLUE, 112,  -0.91 * pi, False, 0, 0, 0, True, False],

               [12, 2, BLUE, 99,  0.07 * pi, False, 0, 0, 0, True, False],
               [12, 2, BLUE, 99,  -0.07 * pi, False, 0, 0, 0, True, False],
               [12, 2, BLUE, 99,  0.93 * pi, False, 0, 0, 0, True, False],
               [12, 2, BLUE, 99,  -0.93 * pi, False, 0, 0, 0, True, False],

               [12, 2, BLUE, 99,  0.43 * pi, False, 0, 0, 0, True, False],
               [12, 2, BLUE, 99,  -0.43 * pi, False, 0, 0, 0, True, False],
               [12, 2, BLUE, 99,  0.57 * pi, False, 0, 0, 0, True, False],
               [12, 2, BLUE, 99,  -0.57 * pi, False, 0, 0, 0, True, False],

               [26, 3, BLUE, 72, 0, True, 0.037, 22, 0, True, False],
               [26, 3, BLUE, 72, 0.5 * pi, True, 0.037, 22, 0.2, True, False],
               [26, 3, BLUE, 72, -0.5 * pi, True, 0.037, 22, 0.5, True, False],
               [26, 3, BLUE, 72, pi, True, 0.037, 22, 0.8, True, False],

               [70, 3, BLUE,   0,  0, True, 0.04, 27, 0.2, True, False],
               [32, 1, BLUE, 0, 0, True, 0.031, 18, 0, True, False],

               [6, 1, ORANGE, 0, 0, True, 0.01, 6, 0.9, True, True, 22, 0.23 * pi],
               [6, 1, ORANGE, 0, 0, True, 0.01, 6, 0.5, True, True, 22, -0.23 * pi],
               [6,  1, ORANGE,  0, 0, True,  0.01, 6,  0.7, True,  True, 28,  0.13 * pi],
               [6, 1, ORANGE, 0, 0, True, 0.01, 6, 0.2, True, True, 28, -0.13 * pi],
               [6,  1, ORANGE,  0, 0, True,  0.01, 6,  0.4, True,  True, 34,  0.06 * pi],
               [6, 1, ORANGE, 0, 0, True, 0.01, 6, 0.1, True, True, 34, -0.06 * pi],

               [20, 3, ORANGE, 0, 0, True, 0.026, 15, 0, True, True],
               [9,  1, ORANGE, 0,  0, True, 0.013, 8,  0.5, True, True,  42],

               [14, 1, VIOLET, 4, -0.15 * pi,   False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 22, -0.35 * pi,  False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 32, 0.22 * pi,   False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 32, -0.22 * pi,  False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 30, -0.75 * pi,  False, 0,     0,  0,   False, False, 0, 0],
               [13, 1, VIOLET, 40, -0.8 * pi,   False, 0,     0,  0,   False, False, 0, 0],
               [17, 1, VIOLET, 29, 0.82 * pi,   False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 8,  0.5 * pi,    False, 0,     0,  0,   False, False, 0, 0],
               [11, 1, VIOLET, 38, 0.6 * pi,    False, 0,     0,  0,   False, False, 0, 0],
               [12, 1, VIOLET, 22, 0.65 * pi,   False, 0,     0,  0,   False, False, 0, 0]]

TURRET_HEALTH_STATES = ((0, ),)
###############################################################################


def align_body(body):
    max_sizes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(body[0])):
        for j in range(len(body)):
            if i == 2:
                if body[j][2] == ORANGE: body[j][2] = 'ORANGE'
                elif body[j][2] == BLUE: body[j][2] = 'BLUE'
                elif body[j][2] == VIOLET: body[j][2] = 'VIOLET'
                elif body[j][2] == LIGHT_ORANGE: body[j][2] = 'LIGHT_ORANGE'
            elif i == 4:
                sign = '' if body[j][4] > 0 else '-'
                if body[j][4] == 0:
                    body[j][4] = '0.00'
                elif body[j][4] == pi:
                    body[j][4] = 'pi'
                else:
                    body[j][4] = sign + str(round(abs(body[j][4]/pi), 3)) + ' * pi'
            else:
                body[j][i] = str(body[j][i])
            if len(body[j][i]) > max_sizes[i]:
                max_sizes[i] = len(str(body[j][i]))

    for i in range(len(body)):
        print('                      [' + body[i][0] + ', ' + ' '*(max_sizes[0]-len(body[i][0])) +
              body[i][1] + ', ' + ' ' * (max_sizes[1] - len(body[i][1])) +
              body[i][2] + ', ' + ' ' * (max_sizes[2] - len(body[i][2])) +
              body[i][3] + ', ' + ' ' * (max_sizes[3] - len(body[i][3])) +
              body[i][4] + ', ' + ' ' * (max_sizes[4] - len(body[i][4])) +
              body[i][5] + ', ' + ' ' * (max_sizes[5] - len(body[i][5])) +
              body[i][6] + ', ' + ' ' * (max_sizes[6] - len(body[i][6])) +
              body[i][7] + ', ' + ' ' * (max_sizes[7] - len(body[i][7])) +
              body[i][8] + ', ' + ' ' * (max_sizes[8] - len(body[i][8])) +
              body[i][9] + ', ' + ' ' * (max_sizes[9] - len(body[i][9])) +
              body[i][10] + '],')


#align_body(MACHINEGUNNER_BODY)
