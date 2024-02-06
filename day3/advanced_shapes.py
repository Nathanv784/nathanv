# advanced_shapes.py

import math

class ThreeDShape:
    def volume(self):
        pass

class Sphere(ThreeDShape):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

class Cuboid(ThreeDShape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height
