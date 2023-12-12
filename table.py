class Table:
    def __init__(self, vars, filename):
        self.vars = vars
        self.filename = filename
    def singleLineEval(self, lineNum):
        line = self.readLine(lineNum)
        total = 0
        currExpression = 0 #0 for or, 1 for and
        for char in line:
            if(ord(char) < 65):
                return -1
            elif(ord(char) < 90):
                if(currExpression == 0):
                    total = total + vars[ord(char) - 65]
                else:
                    total = total * vars[ord(char) - 65]
            elif(ord(char) == 94):
                currExpression = 1
            elif(ord(char) == 118):
                currExpression = 0
    def readLine(self, lineNum):
        with open(self.filename, 'r') as rule:
            count = 0
            for line in rule:
                if(count == lineNum):
                    return line.strip().replace(" ", "")
                count += 1
            