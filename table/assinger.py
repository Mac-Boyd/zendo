from graph import rule
class Assigner:
    def __init__ (self, filename, numVars, graph):
        self.filename = filename
        self.numVars = numVars
        self.vars = []
        self.graph = graph
    def assignRules(self):
        with open (self.filename, 'r') as rulevars:
            currRule = 0
            for line in rulevars:
                line = line.replace(" ", "").replace('\n', "")
                if(line[0] == '#'):
                    return self.vars
                else:
                    ruleNum = line[0:3]
                    RULE_DICTIONARY = {'000': rule.NumRule}
                    self.vars.append(RULE_DICTIONARY.get(ruleNum)(self.graph))
                    self.vars[currRule].parameters = line[3:]
                currRule = currRule + 1
