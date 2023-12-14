from graph import rule
from table import table
class PriorityEvaluator:
    def __init__(self, logicalRuleName, evaluatedRules):
        #note that evaluated rules needs to be in variable order (i.e. the rule that corresponds to the variable A needs to be at evaluatedRules[0])
        self.rules = evaluatedRules
        self.table = table.Table(logicalRuleName, len(evaluatedRules)).makeTable()
        #priority is defined a little weird
        #priority[speed category][internal priority] = variable index
        self.priority = []
        #HEY! LISTEN! If I screwed up the number of O() time value thingies this number here will need to change or this whole thing breaks
        #It's currently 5, but that should go up or down depending on the number of speed categories rules can have        
        for i in range(0, len(self.evaluatedRules)):
            self.priority[self.evaluatedRules[i].speed].append(i)            

    def evalInternalPriority(self, speedClass):
        internalOrder = []
        fragility = []
        for i in range(0, len(self.priority[speedClass])):
            fragility.append([self.priority[speedClass][i], 0])
            for j in self.table:
                if (j >> (self.priority[speedClass][i]) & 1):
                    k = j - pow(self.priority[speedClass][i], 2)
                    if(self.table[i] != self.table[k]):
                        fragility[i][1] += 1
        fragility.sort(key = lambda x: x[1])
        for i in fragility:
            internalOrder.append(i[0])
        self.priority[speedClass] = internalOrder

    def evalRule(self):
        possibilities = self.table
        #i is the speed cadegory, j is the variable index (i hope)
        for i in self.priority:
            for j in i:
                var = self.rules[j].evalRule()
                for k in range(0, len(possibilities)):
                    if((k >> j & 1) != var):
                        possibilities[k] = -1
                evalDone = set([i for i in possibilities if i != -1])
                if(len(evalDone == 1)):
                    return evalDone[0]
        return -1

                    
