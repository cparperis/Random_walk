#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:45:36 2020

@author: Christopher
"""

import random

def random_walk(n):
    """Return coordinates after random walk of 'n' steps"""
    x, y, z = 0, 0, 0
    for i in range(n):
        (dx, dy, dz) = random.choice([(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)])
        x += dx
        y += dy
        z += dz
    return (x, y, z)

(x, y, z) = random_walk(100)

print(x, y, z)