class Table:
    def __init__(self, filename, usedVars):
        self.vars = []
        self.filename = filename
        self.table = {}
        self.usedVars = usedVars
    def singleLineEval(self, lineNum):
        line = self.readLine(lineNum)
        total = 0
        currExpression = 0 #0 for or, 1 for and
        for char in line:
            charNum = ord(char)
            index = charNum - 65
            if(charNum < 65):
                return -1
            elif(charNum < 90):
                if(currExpression == 0):
                    total = total + self.vars[index]
                else:
                    total = total * self.vars[index]
            elif(charNum == 94):
                currExpression = 1
            elif(charNum == 118):
                currExpression = 0
        if(total >= 1):
            return 1
        else:
            return 0
    def readLine(self, lineNum):
        with open(self.filename, 'r') as rule:
            count = 0
            for line in rule:
                if(count == lineNum):
                    return line.replace(" ", "").replace('\n', "")
                count += 1
            return "-1"
    def fullEval(self):
        currentLine = 0
        currentOp = 0 #again, 0 for or, 1 for and
        total = 0
        with open(self.filename, 'r') as rule:
            for line in rule:
                if(line[0] == "^"):
                    currentOp = 1
                elif(line[0] == "v"):
                    currentOp = 0
                else:
                    if(currentOp == 0):
                        total = total + self.singleLineEval(currentLine)
                    else:
                        total = total * self.singleLineEval(currentLine)
                currentLine += 1         
        if(total == 0):
            return 0
        else:
            return 1
    def makeTable(self):
        for i in range(0, 26):
            self.vars.append(-1)
        for i in range(0, self.usedVars):
            self.vars[i] = 0
        i = 0
        while(i < 16):
            self.table[i] = self.fullEval()
            i = i + 1
            for j in range(0, self.usedVars):
                self.vars[j] = (i >> j) & 1