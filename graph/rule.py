from graph import graph
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