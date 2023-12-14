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
    def evalRule(self):
        raise NotImplementedError
    
