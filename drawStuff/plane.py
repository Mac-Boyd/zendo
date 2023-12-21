from drawStuff import node
from numpy import sin
from numpy import cos
class Plane:
    def __init__(self, nodes):
        self.nodes = nodes
        self.radSize = 1.25
        
    def positionNodes(self):
        radius = self.radSize * len(self.nodes)
        pi = 3.14159265
        for i in range(0, len(self.nodes)):
            angle = i * ((pi * 2) / len(self.nodes))
            self.nodes[i].setPostition(radius * cos(angle), radius * sin(angle))