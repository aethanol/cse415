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

#<METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Cognitive_Radio"
PROBLEM_VERSION = "1"
PROBLEM_AUTHORS = ['E. Anderson', 'B. Olson']
PROBLEM_CREATION_DATE = "30-OCT-2017"
PROBLEM_DESC=\
'''This formulation of the Cognitive Radio problem uses generic
Python 3 constructs and has been tested with Python 3.4.
It is designed to work according to the QUIET tools interface, Version 1.
'''
#</METADATA>


#<COMMON_DATA>

#</COMMON_DATA>

#<COMMON_CODE>

class State:
  def __init__(self, d):
    self.d = d

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

#</COMMON_CODE>

#<INITIAL_STATE>

#</INITIAL_STATE>


#<OPERATORS>

#</OPERATORS>

#<GOAL_TEST>

#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION>

#</GOAL_MESSAGE_FUNCTION>

#<HEURISTICS>

#</HEURISTICS>