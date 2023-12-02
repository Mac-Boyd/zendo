import rule
a = rule.Rule("(a v b) ^ (c v d) v e")
a.partialParseRule()
a.ruleStack[0].parseRule()
a.ruleStack[1].parseRule()
a.printRule()