# toc_final

Theory of Computation Final Option 2
Preston Dodd and Jack Anlauf both completed course evals on 12/9

### AUTHORS:
JACK ANLAUF
PRESTON DODD

### TOOLING:
Python only

### SOURCES:
(src/cfg_representation.py) #to define a CFG object
(src/pda_representation.py) #to define a PDA object
(src/CFG_TO_CNF.py) #to convert a CFG into CNF
(src/CFG_TO_CNF_TESTS.py) #to test CFG_TO_CNF.py
(src/CFG_To_PDA.py) #to convert a CFG into a PDA
(src/CFG_TO_PDA_TESTS.py) #to test CFG_To_PDA.py
(src/TESTING.txt) #txt file documenting the testing.

###REQUIRED FUNCTIONS:
CFG is defined in cfg_representation.py. 
We modeled it after the set theoretic description G = {N, Σ, P, S}, with N, Σ, P, S being renamed for our ease of use. 
Rules are represented by a list of tuples of the format (str, \[str\]),
where the first string is the left side of a production and the list is the right side. 
File contains checks to make sure inputs are valid CFGs.  

PDA is defined in pda_representation.py
We modeled it after the set theoretic description like we did for CFG. M = (Q,Σ,Γ,R,E,s,F)
R is represented as a list of tuples of the format (startState, endState, terminal, stackSymbolConsumed) 
E is represented as a list of tuples of the format (startState, endState, terminal, stackSymbolAdded)
Terminal is the string that is added to the output. 
Terminal and stack symbol can be empty.  
File contains checks to make sure inputs are valid CFGs.  
Also contains functions to safely add R and E transitions. 

CFG_To_PDA as defined in CFG_To_PDA.py
Takes a CFG object, creates a new PDA based off the algorithm in the lecture notes, and returns it. 
Utilizes functions defined in PDA to safely add transitions

CFGtoCNF in CFG_TO_CNF.py
this function takes CFG object, runs several algorithms, and returns the same CFG oject
with its Terminals, NonTerminals, and Production rules changed to conform with CNF standards


### STATUS:
THE CFG and PDA data types are working and thoroughly designed

It was decided not to do part 3 of option 2, to generate a graphviz file. No work was done related to this part of the assignment.

CFGtoPDA successfully transforms a given CFG into a Push Down Automata

CFGtoCNF successfully transforms a given CFG into Chomsky Normal Form

Tests Successfully created and ran