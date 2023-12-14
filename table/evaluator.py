from graph import rule
from table import table
class Evaluator:
    def __init__(self, logicalRuleName, evaluatedRules):
        self.rules = evaluatedRules
        self.table = table.Table(logicalRuleName, len(evaluatedRules))
        self.truthTable = self.table.fullEval()
        #priority is defined a little weird
        #priority[speed category][internal priority] = variable index
        self.priority = []
        #HEY! LISTEN! If I screwed up the number of O() time value thingies this number here will need to change or this whole thing breaks
        #It's currently 5, but that should go up or down depending on the number of speed categories rules can have
        for i in range(6):
            self.priority.append([])
        
