#!/usr/bin/env python

from pov import Vector, Texture, Pigment


x = Vector(1, 0, 0)
y = Vector(0, 1, 0)
z = Vector(0, 0, 1)

white = Texture(Pigment(color=(1, 1, 1)))
light_grey = Texture(Pigment(color=(0.75, 0.75, 0.75)))
grey = Texture(Pigment(color=(0.5, 0.5, 0.5)))
dark_grey = Texture(Pigment(color=(0.25, 0.25, 0.25)))

