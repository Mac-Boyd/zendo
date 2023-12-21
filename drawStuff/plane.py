from drawStuff import node
import pygame
class Plane:
    def __init__(self, nodes):
        self.nodes = nodes
        self.radSize = 30
        
    def positionNodes(self):
        radius = self.radSize * len(self.nodes)
        pi = 3.14159265
        for i in range(0, len(self.nodes)):
            angle = i * ((pi * 2) / len(self.nodes))
            self.nodes[i].setPostition(radius, angle)
    
    def drawGraph(self):
        pygame.init()
        self.positionNodes()
        screen = pygame.display.set_mode((500, 500))
        clock = pygame.time.Clock()
        running = True
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("white")
            for i in range (0, len(self.nodes)):
                pygame.draw.circle(screen, "black", (self.nodes[i].position[0] + 250, self.nodes[i].position[1] + 250), self.radSize)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()