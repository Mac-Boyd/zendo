class Table:
    def __init__(self, vars, filename):
        self.vars = vars
        self.filename = filename
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
                print(line)
                if(count == lineNum):
                    return line.replace(" ", "")
                count += 1
            return "-1"