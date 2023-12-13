import table

vars = []
for i in range(0, 26):
    vars.append(-1)
vars[0] = 0
vars[1] = 0
vars[2] = 0
vars[3] = 0
truth = table.Table(vars, "rule.txt")
full = {}
i = 0
while(i < 16):
    full[i] = truth.fullEval()
    i = i + 1
    for j in range(0, 4):
        vars[j] = (i >> j) & 1
print(full)