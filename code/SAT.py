AND = '^'
OR = 'v'
NG = '~'
from cspbase import *

class SAT:
    def __init__(self, operator, children=None):
        self.operator = operator
        self.children = children

    def add_children(children):
        self.children.extend(children)

    def set_operator(operator):
        self.operator = operator

    def to_string():
        if self.is_variable():
            return self.operator
        elif operator == NG:
            return '~{}'.format(children[0].to_string())
        output = children[0].to_string()
        for i in range(1,len(children)):
            output += operator + children[i].to_string()
        return '({})'.format(output)

    def is_variable():
        return len(self.children) == 0
    '''
    def result():
        '''
        #Negation should only have one child.
        #Other operator can have multiple children.
        '''
        if operator == AND:
            return sum([i.result() for i in self.children]) == len(self.children)
        elif operator == OR:
            return sum([i.result() for i in self.children]) > 0
        elif operator = NG:
            return not self.children[0].result()
        return self.operator
    '''
    