import numpy
class Node:
    def __init__(self, size, color, position):
        self.size = size
        self.color = color
        self.position = position
    def setPostition(self, radius, angle):
        self.position = [radius * numpy.cos(angle), radius * numpy.sin(angle)]