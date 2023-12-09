class PDA:
    def __init__(self, states, inputAlphabet, stackAlphabet, RTransitionFunctions, ETransitionFunctions, startState, acceptingStates):
        self.states = states # set of Strings, usually numerical characters
        self.inputAlphabet = inputAlphabet # set of strings, the lower case chars in the class examples
        self.stackAlphabet = stackAlphabet # set of strings
        #  a char is consumed
        self.RTransitionFunctions = RTransitionFunctions # set of tuples structured as: (start state, end state, terminal, stack symbol cosumed)
        # a char is not consumed
        self.ETransitionFunctions = ETransitionFunctions # set of tuples structured as: (start state, end state, terminal, stack symbol added)
        self.startState = startState # string, has to be in states
        self.acceptingStates = acceptingStates # list of strings, all in states

    def addRTransition(self, startState, endState, strAdded, stackRemoved):
        return

    def addETrantition(self, startState, endState, strAdded, stackAdded):
        return

