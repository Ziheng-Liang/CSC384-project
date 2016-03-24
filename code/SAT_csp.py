def convert_CSP(sat):
    csp = CSP('sat')
    variables = {}
    sat_tuples = [(True, True, True),
                  (True, True, False),
                  (True, False, True),
                  (True, False, False),
                  (False, True, True),
                  (False, True, False),
                  (False, False, True),
                  (False, False, False)]
    idx = 0
    for set_3 in sat:
        three_variables = []
        neg = []
        for v in set_3:
            if '~' in v:
                variable = v[1:]
                neg.append(True)
            else:
                variable = v
                neg.append(False)
            if not v in variables:
                variables[v] = Variable(v, domain=[True, False])
                csp.add_var(variables[v])
            three_variables.append(variables[v])
        sat_tuples_temp = sat_tuples[:]
        sat_tuples_temp.remove(tuple(neg))
        c = Constraint(str(idx), three_variables)
        c.add_satisfying_tuples(sat_tuples_temp)
        csp.add_constraint(c)
        
        idx += 1
    return csp

if __name__ == '__main__':
    from cspbase import *
    from futoshiki_csp import *
    test = [['x1', 'x2', 'x3'], ['x4', '~x5', '~x1']]
    csp = convert_CSP(test)