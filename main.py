import rule
import table
#python hates recursion. most complex rule with current system is ((a^b) ^ (c^d))
a = rule.Rule("a ^ b")
a.partialParseRule()
a.printRule()
truth = table.Table(2, a)
truth.evalTable()
print(truth.truthTable)