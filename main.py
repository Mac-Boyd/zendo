import table

vars = []
for i in range(0, 26):
    vars.append(-1)
vars[0] = 0
vars[1] = 1
vars[2] = 0
truth = table.Table(vars, "rule.txt")
print(truth.singleLineEval(0))