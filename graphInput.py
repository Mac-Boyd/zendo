import pygame
class GraphInput:
    def __init__(self, filename):
        self.filename = filename
    def getInput(self):
        #get input from file
        result = [[], []]
        with open(self.filename, 'r') as nodes:
            lineNum = 0
            for line in nodes:
                line = line.replace(" ", "").replace('\n', "").replace(",", "").replace("(", "").replace(")", "").replace("L", "3").replace("M", "2").replace("S", "1")
                if(line[0] == '#'):
                    break
                currNode = [line[0], line[1]]
                match currNode[0]:
                    case 'Y':
                        currNode[0] = pygame.Color('#f0ed00')
                    case 'G':
                        currNode[0] = pygame.Color('#31973b')
                    case 'B':
                        currNode[0] = pygame.Color('#2137d6')
                    case other:
                        currNode[0] = pygame.Color('#d82716')
                result[1].append(currNode)
                result[0].append([])
                for i in range(2, len(line)):
                    result[0][lineNum].append(int(line[i]) - 1)
                lineNum += 1
        matrix = []
        for i in range(0, len(result[1])):
            matrix.append([])
            for j in range(0, len(result[1])):
                if(j in result[0][i]):
                    matrix[i].append(1)
                else:
                    matrix[i].append(0)
        result[0] = matrix
        return result
        
        