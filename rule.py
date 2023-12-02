class RuleSegment:
    def __init__(self, rule): 
        self.rule = rule
        self.ruleStack = [] #technically doesn't enforce use as a stack but if it's not used as a stack it could be a problem
    def parseRule (self):
        #for lack of a better system, for now i will use v for logical or and ^ for logical and
        for i in self.rule:
            if i != ' ':
                self.ruleStack.append(i)
        self.rule = ""
    def checkRule():
        pass
class Rule:
    ruleStack = []
    def __init__(self, rule):
        self.rule = rule
    def partialParseRule(self):
        if "(" not in self.rule:
            self.ruleStack.append(RuleSegment(self.rule))
            for i in self.ruleStack:
               i.parseRule()
            return
        locOpen = self.rule.find('(')
        locClose = self.rule.find(')')
        smallRule = self.rule[locOpen : locClose + 1]
        self.rule = self.rule.replace(smallRule, '', 1)
        smallRule = smallRule[1:len(smallRule) - 1]
        smallRule = Rule(smallRule)
        smallRule.partialParseRule()
        self.partialParseRule()
    #PRINTRULE SHOULD BE ONLY FOR DEBUGGING
    def printRule(self):
        for i in self.ruleStack:
            print("rule stack")
            print(i.ruleStack)