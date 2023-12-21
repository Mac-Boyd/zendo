from drawStuff import node
from graph import graph
import pygame
class Plane:
    def __init__(self, graph, graphFile):
        self.nodes = graph.nodeProps
        self.adjMat = graph.adjMat
        self.radSize = 30
        self.screenSize = 750
        self.graphFile = graphFile
    def positionNodes(self):
        radius = self.radSize * len(self.nodes)
        pi = 3.14159265
        for i in range(0, len(self.nodes)):
            angle = i * ((pi * 2) / len(self.nodes))
            self.nodes[i].setPostition(radius, angle)
            for j in range(len(self.nodes[i].position)):
                self.nodes[i].position[j] += self.screenSize/2
    
    def drawGraph(self):
        pygame.init()
        self.positionNodes()
        screen = pygame.display.set_mode((self.screenSize, self.screenSize))
        clock = pygame.time.Clock()
        fontSize = 15
        font = pygame.font.SysFont("Arial", fontSize)
        backgroundColor = pygame.Color('#b5bbcc')
        running = True
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill(backgroundColor)
            for i in range (0, len(self.nodes)):
                for j in range(len(self.adjMat[i])):
                    if(self.adjMat[i][j] == 1):
                        pygame.draw.line(screen, "black", self.nodes[i].position, self.nodes[j].position)
            for i in range (0, len(self.nodes)):
                pygame.draw.circle(screen, self.nodes[i].color, self.nodes[i].position, (self.radSize * (self.nodes[i].size/2)))
            graphNodes = []
            with open(self.graphFile, 'r') as file:
                i = 0
                for line in file:
                    if(line[0] == '#'):
                        break
                    screen.blit(font.render(line.replace('\n', ""), True, "black"), (self.screenSize/1.25, self.screenSize/1.25 + i))
                    i += fontSize
            pygame.display.flip()
            clock.tick(10)
        pygame.quit()