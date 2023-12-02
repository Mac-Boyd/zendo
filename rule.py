class Rule:
    ruleStack = [] #technically doesn't enforce use as a stack but if it's not used as a stack it could be a problem
    def __init__(self, rule): 
        self.rule = rule
    def parseRule (self):
        #for lack of a better system, for now i will use v for logical or and ^ for logical and
        for i in self.rule:
            if i == ' ':
                continue
            if i == 'v':
                #dostuff
                break
            elif i == '^':
                #doOtherStuff
                break
    def checkRule():
        pass

    