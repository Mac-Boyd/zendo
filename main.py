import table
import numpy as np
import numpy.linalg as lin
import graph

truth = table.Table("rule.txt", 3)
truth.makeTable()
print(truth.table)


adjMat = [[0,1,0,0,0,0,0,0],
          [1,0,1,0,0,1,0,0],
          [0,1,0,1,1,0,0,0],
          [0,0,1,0,0,0,0,0],
          [0,0,1,0,0,0,0,0],
          [0,1,0,0,0,0,1,0],
          [0,0,0,0,0,1,0,1],
          [0,0,0,0,0,0,1,0]]

graphy = graph.Graph(adjMat, [])
print("Completeness: " + str(graphy.isComplete()))
