import rule
import math
class Table:
    def __init__(self, numVars, rule):
        self.truthTable = []
        self.numVars = numVars
        self.rule = rule
    def binarizeNum(self, num, expSize):
        returnString = ""
        while(num > 0):
            returnString += str(num % 2)
            num = int(num / 2)
        while(len(returnString) < expSize):
            returnString = "0" + returnString
        print(returnString)
        return returnString
    def evalStatement(self, vars):
        if len(self.rule.ruleStack) == 1:
            if self.rule.ruleStack[0].ruleStack[1] == 'v':
                if "1" in vars:
                    return True
                else:
                    return False
            else:
                if "0" in vars:
                    return False
                else:
                    return True
        return False
    def evalTable(self):
        for i in range(int(math.pow(2, self.numVars))):
            binaryVal = self.binarizeNum(i, self.numVars)
            if self.evalStatement(binaryVal):
                self.truthTable.append(True)
            else:
                self.truthTable.append(False)
