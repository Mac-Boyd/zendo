class Node:
    def __init__(self, size, color, position):
        self.size = size
        self.color = color
        self.position = position
    def setPostition(self, x, y):
        self.position = [x, y]