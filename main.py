#from table import table
from graph import graph
from table import evaluator
from table import assinger
Graph = graph.Graph()
Assigner = assinger.Assigner("variableAssignment.txt", 2, Graph)
Assigner.assignRules()
Evaluator = evaluator.PriorityEvaluator("rule.txt", Assigner.vars)
for i in range(0, 5):
    Evaluator.evalInternalPriority(i)
print(Evaluator.evalRule())