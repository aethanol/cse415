'''Ethan Anderson aethan
cse415 assignment 3'''

# Astar.py, April 2017
# Based on ItrDFS.py, Ver 0.4a, October 14, 2017.

# A* Search of a problem space.
# The Problem should be given in a separate Python
# file using the "QUIET" file format.
# See the TowerOfHanoi.py example file for details.
# Examples of Usage:

# A small change was made on Oct. 14, so that backtrace
# uses None as the BACKLINK value for the initial state,
# just as in ItrDFS.py, rather than using -1 as it did
# in an earlier version.

# python3 AStar.py EightPuzzleWithHeuristics h_manhattan

import sys
from priorityq import PriorityQ

# DO NOT CHANGE THIS SECTION
if sys.argv == [''] or len(sys.argv) < 2:
    import Cognitive_Radio as Problem

    heuristics = lambda s: Problem.HEURISTICS['h_manhattan'](s)
    initial_state = Problem.CREATE_INITIAL_STATE()

else:
    import importlib

    Problem = importlib.import_module(sys.argv[1])
    heuristics = lambda s: Problem.HEURISTICS[sys.argv[2]](s)
    initial_state = Problem.State(importlib.import_module(sys.argv[3]).CREATE_INITIAL_STATE())

print("\nWelcome to AStar")
COUNT = None
BACKLINKS = {}


# DO NOT CHANGE THIS SECTION
def runAStar():
    # initial_state = Problem.CREATE_INITIAL_STATE(keyVal)
    # initial_state = Problem.CREATE_INITIAL_STATE()
    print("Initial State:")
    print(initial_state)
    global COUNT, BACKLINKS
    COUNT = 0
    BACKLINKS = {}
    path, name = AStar(initial_state)
    print(str(COUNT) + " states examined.")
    return path, name


# A star search algorithm
# TODO: finish A star implementation
def AStar(initial_state):
    global COUNT, BACKLINKS
    # TODO: initialze and put first state into
    # priority queue with respective priority
    # add any auxiliary data structures as needed

    GVALUE = {}
    # FVALUE = {}
    OPEN = PriorityQ()
    CLOSED = []
    OPEN.insert(initial_state, 0)
    BACKLINKS[initial_state] = None
    GVALUE[initial_state] = 0

    while len(OPEN) != 0:
        S = OPEN.deletemin()
        while S[0] in CLOSED:
            S = OPEN.deletemin()
        cost = S[1]
        S = S[0]
        CLOSED.append(S)

        COUNT += 1
        # DO NOT CHANGE THIS SECTION: begining
        if Problem.GOAL_TEST(S):
            print(Problem.GOAL_MESSAGE_FUNCTION(S))
            path = backtrace(S)
            return path, Problem.PROBLEM_NAME
        # DO NOT CHANGE THIS SECTION: end

        # TODO: finish A* implementation
        for op in Problem.OPERATORS:
            if op.precond(S):
                new_state = op.state_transf(S)
                GVALUE[new_state] = cost + 1
                if not (new_state in CLOSED):
                    h = heuristics(new_state)
                    f = h + GVALUE[new_state]
                    # if OPEN has the new state already, check if the new state is lower cost
                    if OPEN.__contains__(new_state) and OPEN.getpriority(new_state) < h:
                        OPEN.remove(new_state)
                        OPEN.insert(new_state, f)
                    elif not OPEN.__contains__(new_state):
                        OPEN.insert(new_state, f)

                    BACKLINKS[new_state] = S


# DO NOT CHANGE
def backtrace(S):
    global BACKLINKS
    path = []
    while S:
        path.append(S)
        S = BACKLINKS[S]
    path.reverse()
    print("Solution path: ")
    for s in path:
        print(s)
    print("\nPath length = " + str(len(path) - 1))
    return path


if __name__ == '__main__':
    path, name = runAStar()
