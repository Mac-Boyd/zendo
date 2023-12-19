from graph import graph
#note to whoever is doing the rule classes: just put them all in this file. unless each one is > 50 lines or so it'll probably be fine. just put space in between them
class Rule:
    def __init__(self, speed, graph):
        '''speed should be a variable from 0-5 
        0: O(1), 
        1: O(log(n)), 
        2: O(n)
        3: O(nlog(n))
        4: O(n^2)
        5: O(n^n)'''
        self.speed = speed
        self.graph = graph
        #Each rule should be numbered, do them in order of creations, for now. Each abstract rule should have a negative number
        self.num = -1
        self.paramaters = []
    def evalRule(self):
        raise NotImplementedError
    
class NumRule(Rule):
    def __init__(self, graph):
        self.speed = 0
        self.graph = graph
        self.parameters = []
    def evalRule(self):
        comparative = self.parameters[0:3]
        match comparative:
            case '000':
                return (self.graph.nodes > int(self.parameters[3:]))
            case '001':
                return (self.graph.nodes < int(self.parameters[3:]))
            case '002':
                return (self.graph.nodes == int(self.parameters[3:]))
