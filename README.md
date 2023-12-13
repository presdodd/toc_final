# toc_final

Theory of Computation Final Option 2
Preston Dodd and Jack Anlauf both completed course evals on 12/9

AUTHORS:
JACK ANLAUF
PRESTON DODD

TOOLING:
Python only

SOURCES:
(src/cfg_representation.py) #to define a CFG object
(src/pda_representation.py) #to define a PDA object
(src/CFG_TO_CNF.py) #to convert a CFG into CNF
(src/CFG_TO_CNF_TESTS.py) #to test CFG_TO_CNF.py
(src/CFG_To_PDA.py) #to convert a CFG into a PDA
(src/CFG_TO_PDA_TESTS.py) #to test CFG_To_PDA.py
(src/TESTING.txt) #txt file documenting the testing.

REQUIRED FUNCTIONS:
CFGtoCNF in CFG_TO_CNF.py
this function takes CFG object, runs several algorithms, and returns the same CFG oject
with its Terminals, NonTerminals, and Production rules changed to conform with CNF standards

STATUS:
THE CFG and PDA data types are working and thouroughly designed

It was decided not to do part 3 of option 2, to generate a graphviz file. No work was done related to this part of the assignment.

CFGtoCNF successfully transforms a given CFG into Chomsky Normal Form
