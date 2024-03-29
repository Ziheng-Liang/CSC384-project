#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented.

'''
Construct and return Futoshiki CSP models.
'''

from cspbase import *
import itertools

def futoshiki_csp_model_1(initial_futoshiki_board):
    '''Return a CSP object representing a Futoshiki CSP problem along with an
    array of variables for the problem. That is return

    futoshiki_csp, variable_array

    where futoshiki_csp is a csp representing futoshiki using model_1 and
    variable_array is a list of lists

    [ [  ]
      [  ]
      .
      .
      .
      [  ] ]

    such that variable_array[i][j] is the Variable (object) that you built to
    represent the value to be placed in cell i,j of the futoshiki board
    (indexed from (0,0) to (n-1,n-1))


    The input board is specified as a list of n lists. Each of the n lists
    represents a row of the board. If a 0 is in the list it represents an empty
    cell. Otherwise if a number between 1--n is in the list then this
    represents a pre-set board position.

    Each list is of length 2n-1, with each space on the board being separated
    by the potential inequality constraints. '>' denotes that the previous
    space must be bigger than the next space; '<' denotes that the previous
    space must be smaller than the next; '.' denotes that there is no
    inequality constraint.

    E.g., the board

    -------------------
    | > |2| |9| | |6| |
    | |4| | | |1| | |8|
    | |7| <4|2| | | |3|
    |5| | | | | |3| | |
    | | |1| |6| |5| | |
    | | <3| | | | | |6|
    |1| | | |5|7| |4| |
    |6> | |9| < | |2| |
    | |2| | |8| <1| | |
    -------------------
    would be represented by the list of lists

    [[0,'>',0,'.',2,'.',0,'.',9,'.',0,'.',0,'.',6,'.',0],
     [0,'.',4,'.',0,'.',0,'.',0,'.',1,'.',0,'.',0,'.',8],
     [0,'.',7,'.',0,'<',4,'.',2,'.',0,'.',0,'.',0,'.',3],
     [5,'.',0,'.',0,'.',0,'.',0,'.',0,'.',3,'.',0,'.',0],
     [0,'.',0,'.',1,'.',0,'.',6,'.',0,'.',5,'.',0,'.',0],
     [0,'.',0,'<',3,'.',0,'.',0,'.',0,'.',0,'.',0,'.',6],
     [1,'.',0,'.',0,'.',0,'.',5,'.',7,'.',0,'.',4,'.',0],
     [6,'>',0,'.',0,'.',9,'.',0,'<',0,'.',0,'.',2,'.',0],
     [0,'.',2,'.',0,'.',0,'.',8,'.',0,'<',1,'.',0,'.',0]]


    This routine returns Model_1 which consists of a variable for each cell of
    the board, with domain equal to [1,...,n] if the board has a 0 at that
    position, and domain equal [i] if the board has a fixed number i at that
    cell.

    Model_1 also contains BINARY CONSTRAINTS OF NOT-EQUAL between all relevant
    variables (e.g., all pairs of variables in the same row, etc.).

    All of the constraints of Model_1 MUST BE binary constraints (i.e.,
    constraints whose scope includes two and only two variables).
    '''

#IMPLEMENT
    futoshiki_csp = CSP('futoshiki')
    variable_array = []
    board_size = len(initial_futoshiki_board)
    init_domain = [number + 1 for number in range(board_size)]
    sat_tuples_not_equal = []
    sat_tuples_greater = []
    sat_tuples_smaller = []
    for i in range(board_size):
      variable_array.append([])
      for j in range(board_size):
        variable_array[i].append(Variable(str(i)+','+str(j)))
        num = initial_futoshiki_board[i][j*2]
        if num > 0:
          variable_array[i][j].add_domain_values([num])
        else:
          variable_array[i][j].add_domain_values(init_domain)
        futoshiki_csp.add_var(variable_array[i][j])
        if i != j:
          sat_tuples_not_equal.append((i+1,j+1))
        if i > j:
          sat_tuples_greater.append((i+1,j+1))
        if i < j:
          sat_tuples_smaller.append((i+1,j+1))

    for i in range(board_size):
      for j in range(board_size):
        for k in range(j+1, board_size):
          c = Constraint('Row ' + str(i) + ', ' + str(j) + ' and ' + str(k), [variable_array[i][j], variable_array[i][k]])
          c.add_satisfying_tuples(sat_tuples_not_equal)
          futoshiki_csp.add_constraint(c)
          c = Constraint('Col ' + str(i) + ', ' + str(j) + ' and ' + str(k), [variable_array[j][i], variable_array[k][i]])
          c.add_satisfying_tuples(sat_tuples_not_equal)
          futoshiki_csp.add_constraint(c)
      for j in range(1, board_size * 2 - 2, 2):
        if initial_futoshiki_board[i][j] == '>':
          c = Constraint('Row ' + str(i) + ', ' + str((j-1)//2) + ' > ' + str((j+1)//2), [variable_array[i][(j-1)//2], variable_array[i][(j+1)//2]])
          c.add_satisfying_tuples(sat_tuples_greater)
          futoshiki_csp.add_constraint(c)
        if initial_futoshiki_board[i][j] == '<':
          c = Constraint('Row ' + str(i) + ', ' + str((j-1)//2) + ' < ' + str((j+1)//2), [variable_array[i][(j-1)//2], variable_array[i][(j+1)//2]])
          c.add_satisfying_tuples(sat_tuples_smaller)
          futoshiki_csp.add_constraint(c)

    return futoshiki_csp, variable_array


##############################

def futoshiki_csp_model_2(initial_futoshiki_board):
    '''Return a CSP object representing a futoshiki CSP problem along with an
    array of variables for the problem. That is return

    futoshiki_csp, variable_array

    where futoshiki_csp is a csp representing futoshiki using model_2 and
    variable_array is a list of lists

    [ [  ]
      [  ]
      .
      .
      .
      [  ] ]

    such that variable_array[i][j] is the Variable (object) that you built to
    represent the value to be placed in cell i,j of the futoshiki board
    (indexed from (0,0) to (n-1,n-1))

    The input board takes the same input format (a list of n lists of size 2n-1
    specifying the board) as futoshiki_csp_model_1.

    The variables of Model_2 are the same as for Model_1: a variable for each
    cell of the board, with domain equal to [1,...,n] if the board has a 0 at
    that position, and domain equal [n] if the board has a fixed number i at
    that cell.

    However, Model_2 has different constraints. In particular, instead of
    binary non-equals constaints Model_2 has 2*n all-different constraints:
    all-different constraints for the variables in each of the n rows, and n
    columns. Each of these constraints is over n-variables (some of these
    variables will have a single value in their domain). Model_2 should create
    these all-different constraints between the relevant variables, and then
    separately generate the appropriate binary inequality constraints as
    required by the board. There should be j of these constraints, where j is
    the number of inequality symbols found on the board.  
    '''

#IMPLEMENT
    futoshiki_csp = CSP('futoshiki')
    variable_array = []
    board_size = len(initial_futoshiki_board)
    init_domain = [number + 1 for number in range(board_size)]
    sat_tuples_greater = []
    sat_tuples_smaller = []
    sat_tuples_not_equal = []

    varDoms = []
    for v in range(board_size):
      varDoms.append(init_domain)
    for t in itertools.product(*varDoms):
      if not is_duplicate(t):
        sat_tuples_not_equal.append(t)

    for i in range(board_size):
      variable_array.append([])
      for j in range(board_size):
        variable_array[i].append(Variable(str(i)+','+str(j)))
        num = initial_futoshiki_board[i][j*2]
        if num > 0:
          variable_array[i][j].add_domain_values([num])
        else:
          variable_array[i][j].add_domain_values(init_domain)
        futoshiki_csp.add_var(variable_array[i][j])
        if i > j:
          sat_tuples_greater.append((i+1,j+1))
        if i < j:
          sat_tuples_smaller.append((i+1,j+1))

    for i in range(board_size):
      for j in range(1, board_size * 2 - 2, 2):
        if initial_futoshiki_board[i][j] == '>':
          c = Constraint('Row ' + str(i) + ', ' + str((j-1)//2) + ' > ' + str((j+1)//2), [variable_array[i][(j-1)//2], variable_array[i][(j+1)//2]])
          c.add_satisfying_tuples(sat_tuples_greater)
          futoshiki_csp.add_constraint(c)
        if initial_futoshiki_board[i][j] == '<':
          c = Constraint('Row ' + str(i) + ', ' + str((j-1)//2) + ' < ' + str((j+1)//2), [variable_array[i][(j-1)//2], variable_array[i][(j+1)//2]])
          c.add_satisfying_tuples(sat_tuples_smaller)
          futoshiki_csp.add_constraint(c)

      row = variable_array[i]
      col = []
      for j in range(board_size):
        col.append(variable_array[j][i])
      c = Constraint('Row ' + str(i), row)
      c.add_satisfying_tuples(sat_tuples_not_equal)
      futoshiki_csp.add_constraint(c)
      c = Constraint('Col ' + str(i), col)
      c.add_satisfying_tuples(sat_tuples_not_equal)
      futoshiki_csp.add_constraint(c)


    return futoshiki_csp, variable_array


def is_duplicate(t):
  for i in range(len(t)):
    for j in range(i+1, len(t)):
      if t[i] == t[j]:
        return True
  return False