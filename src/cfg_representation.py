class CFG:
    def __init__(self, nonTerminals, terminals, productionRules, startingSymbol):
        self.nonTerminals = nonTerminals # Set of Characters
        self.terminals = terminals # Set of characters
        self.productionRules = productionRules # Set of tuples (input, [output])
                                               # where input is a nonTerminal
                                               # and output is a list of terminals and nonterminal
        self.startingSymbol = startingSymbol # Single character that is in nonTerminals

        # make sure every element in terminals is not in nonTerminals
        # make sure the first element in every tuple in production rules is in nonTerminals
        # make sure starting symbol is in nonTerminals