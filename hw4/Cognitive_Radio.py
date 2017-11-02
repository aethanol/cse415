'''Ethan Anderson aethan & Bartholomew Olson N/A
CSE 415, Autumn 2017, University of Washington
Instructor:  S. Tanimoto.
Assignment 4
'''
'''Cognitive_Radio.py
A QUIET Solving Tool problem formulation.
QUIET = Quetzal User Intelligence Enhancing Technology.
The XML-like tags used here serve to identify key sections of this
problem formulation.
CAPITALIZED constructs are generally present in any problem
formulation and therefore need to be spelled exactly the way they are.
Other globals begin with a capital letter but otherwise are lower
case or camel case.
'''

# <METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Cognitive_Radio"
PROBLEM_VERSION = "1"
PROBLEM_AUTHORS = ['E. Anderson', 'B. Olson']
PROBLEM_CREATION_DATE = "30-OCT-2017"
PROBLEM_DESC = \
    '''This formulation of the Cognitive Radio problem uses generic
    Python 3 constructs and has been tested with Python 3.4.
    It is designed to work according to the QUIET tools interface, Version 1.
    '''
# </METADATA>


# <COMMON_DATA>
INITIAL_STATE_SIZE = 300
# </COMMON_DATA>

# <COMMON_CODE>

class State:
    def __init__(self, d, p, total_radios, known_radios, beam_position):
        self.d = d
        self.p = p
        self.r = total_radios
        self.kr = known_radios
        self.b = beam_position

    def __eq__(self, s2):
        for i, v in enumerate(s2.d):
            for j, v2 in enumerate(v):
                if s2.d[i][j] != self.d[i][j]:
                    return False
        return True

    def __copy__(self):
        # Performs a  deep copy of a state,
        # for use by operators in creating new states.
        news = [p for p in self.d]
        return State(news, self.p, self.r, self.kr, self.b)

    def __hash__(self):
        return (self.__str__()).__hash__()

    def __str__(self):
        str = '\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in self.d])
        str += "\ncurrent position: %s \n beam position: %s \n total radios: %s \n known radios %s \n" % (self.p, self.b, self.r, self.kr)
        return str
        #str += "current position: " + str(self.p) + "\n" + "beam position: " + self.b + "\n" +"total radios: " + self.r + "\n" + "known radios: " + self.kr + "\n"

    def search(self, x, y):
        news = self.__copy__()  # start with a deep copy
        news.b = (x,y)

        # check if we've found a radio at that position
        if news.d[y][x] == 1:
            news.kr += 1

        if news.p < INITIAL_STATE_SIZE - 1:
            news.p += 1  # make the satellite move by one
        else:
            news.p = 0 # or loop back around

        return news

    def can_search(self, x, y):
        if y > self.p + 3 or y < self.p - 3:
            return False
        if x > self.b[1] + 1 or x < self.b[1] - 1:
            return False
        if y > self.b[0] + 1 or x < self.b[0] - 1:
            return False
        return True



class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)


def goal_test(s):
    if s.r == s.kr:
        return True
    return False

def goal_message(s):
    return "Solved the satellite puzzle"


def h_custom(s):
    pass
# </COMMON_CODE>

# <INITIAL_STATE>
# [0,0,0,0,0,0,0]
import random

TOTAL_RADIOS = 0


def generate_initial_state(state_size=INITIAL_STATE_SIZE):
    global TOTAL_RADIOS
    state = []
    for x in range(state_size):
        cur = [0, 0, 0, 0, 0, 0, 0]
        # randomly generate radios every 5 squares
        if not x % 5:
            r = random.getrandbits(1)
            if r == 1:
                TOTAL_RADIOS += 1
            cur[random.randint(0, 6)] = r
        state.append(cur)

    return state


# create an initial state with the satellite starting at position 0
INITIAL_STATE = State(generate_initial_state(), 0, TOTAL_RADIOS, 0, (0,3))

CREATE_INITIAL_STATE = lambda: INITIAL_STATE
# </INITIAL_STATE>


# <OPERATORS>
OPERATORS = []
for y in range(INITIAL_STATE_SIZE):
    for x in range(6):
        OPERATORS.append(Operator("Beam search at %s, %s" % (x, y),
                                  lambda s, x1=x, y1=y: s.can_search(x1, y1),
                                  lambda s, x1=x, y1=y: s.search(x1, y1) ) )
# </OPERATORS>

# <GOAL_TEST>
GOAL_TEST = lambda s: goal_test(s)
# </GOAL_TEST>

# <GOAL_MESSAGE_FUNCTION>
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
# </GOAL_MESSAGE_FUNCTION>

# <HEURISTICS>
HEURISTICS = {'h_custom': h_custom}
# </HEURISTICS>
