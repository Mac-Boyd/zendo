import numpy as np
import numpy.linalg as lin
from graph import graph
from table import evaluator
from table import assinger
from table import table

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

#from table import table

Graph = graph.Graph()
Assigner = assinger.Assigner("variableAssignment.txt", 2, Graph)
Assigner.assignRules()
Evaluator = evaluator.PriorityEvaluator("rule.txt", Assigner.vars)
for i in range(0, 5):
    Evaluator.evalInternalPriority(i)
print(Evaluator.evalRule())