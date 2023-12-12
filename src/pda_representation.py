from typing import Set, Tuple


class PDA:
    def __init__(self, states: Set[str],
                 inputAlphabet: Set[str],
                 stackAlphabet: Set[str],
                 RTransitionFunctions: Set[Tuple[str, str, str, str]],
                 ETransitionFunctions: Set[Tuple[str, str, str, str]],
                 startState: str,
                 acceptingStates: Set[str]):
        self.states = states  # set of Strings, usually numerical characters
        self.inputAlphabet = inputAlphabet  # set of strings, the lower case chars in the class examples
        self.stackAlphabet = stackAlphabet  # set of strings

        self.checkRule(RTransitionFunctions)
        self.checkRule(ETransitionFunctions)

        # a char is consumed e.g. stack symbol on top of stack is popped and consumed
        self.RTransitionFunctions = RTransitionFunctions  # set of tuples structured as: (start state, end state, terminal, stack symbol cosumed)
        # a char is not consumed e.g. symbol is pushed onto stack
        self.ETransitionFunctions = ETransitionFunctions  # set of tuples structured as: (start state, end state, terminal, stack symbol added)

        # check in set of states
        if startState not in states:
            raise Exception("startState = " + startState + " not in set of states")
        self.startState = startState  # string, has to be in states

        # check in set of states
        for state in acceptingStates:
            if state not in states:
                raise Exception("state = " + state + " not in set of states")
        self.acceptingStates = acceptingStates  # set of strings, all in states
        self.output = []
        self.stack = []

    # check transition functions are possible given set of states and alphabets
    def checkRule(self, functions):
        for rule in functions:
            if rule[0] not in self.states:
                raise Exception("startState = " + str(rule[0]) + " is not in set of states")
            if rule[1] not in self.states:
                raise Exception("endState = " + str(rule[1]) + " is not in set of states")
            if rule[2] not in self.inputAlphabet and rule[2] != "":
                raise Exception("terminal = " + str(rule[2]) + " is not in set inputAlphabet")
            if rule[3] not in self.stackAlphabet and rule[3] != "":
                raise Exception("stack symbol = " + str(rule[3]) + " is not in set stackAlphabet")
        return

    def addRTransition(self, startState: str, endState: str, strAdded: str, stackConsumed: str):
        if startState in self.states:
            if endState not in self.states: # note: state that is titled "" is possible
                self.states.add(endState)  # added new state to set of states

            if strAdded not in self.inputAlphabet and strAdded != "":
                self.inputAlphabet.add(strAdded)

            if stackConsumed not in self.stackAlphabet and stackConsumed != "":
                self.stackAlphabet.add(stackConsumed)

            self.RTransitionFunctions.add((startState, endState, strAdded, stackConsumed))

        else:
            raise Exception("startState = " + startState + " is not in set of states")
        return

    def addETransition(self, startState: str, endState: str, strAdded: str, stackAdded: str):
        if startState in self.states:
            if endState not in self.states: # note: state that is titled "" is possible
                self.states.add(endState)

            if strAdded not in self.inputAlphabet and strAdded != "":
                self.inputAlphabet.add(strAdded)

            if stackAdded not in self.stackAlphabet and stackAdded != "":
                self.stackAlphabet.add(stackAdded)

            self.ETransitionFunctions.add((startState, endState, strAdded, stackAdded))

        else:
            raise Exception("startState = " + startState + " is not in set of states")
        return

    def PDAPrint(self):
        print("states = "+str(self.states))
        print("inputAlphabet = "+str(self.inputAlphabet))
        print("stackAlphabet = "+str(self.stackAlphabet))
        print("RTransitionFunctions = "+str(self.RTransitionFunctions))
        print("ETransitionFunctions = " + str(self.ETransitionFunctions))
        print("startState = " + self.startState)
        print("acceptingStates = " + str(self.acceptingStates))