from typing import Set, Tuple, List


class CFG:
    def __init__(self, nonTerminals: Set[str], terminals: Set[str],
                 productionRules: List[Tuple[str, List[str]]], startingSymbol: str):

        # make sure every element in terminals is not in nonTerminals
        for t in terminals:
            if t in nonTerminals:
                raise Exception("terminal t = "+t+" is also in set of nonTerminals")

        self.nonTerminals = nonTerminals # Set of Characters
        self.terminals = terminals # Set of characters

        # making sure rules are made correctly
        for rule in productionRules:
            # check first element in every tuple in production rules is in nonTerminals
            if rule[0] not in nonTerminals:
                raise Exception("[0] = "+rule[0]+" in production rule is not in set of nonTerminals")
            # check elements are in either terminals or nonTerminals
            for s in rule[1]:
                if s not in terminals and s not in nonTerminals and s != '':
                    raise Exception("[1] = "+s+"in tuple is neither in set or terminals nor in set of nonTerminals")


        self.productionRules = productionRules # Set of tuples (input, [output])
                                               # where input is a nonTerminal
                                               # and output is a list of terminals and nonterminal

        # make sure starting symbol is in nonTerminals
        if startingSymbol not in nonTerminals:
            raise Exception("starting symbol = "+startingSymbol+" is not in set of nonTerminals")
        self.startingSymbol = startingSymbol # Single character that is in nonTerminals

    def CFGPrint(self):
        print("nonTerminals = "+str(self.nonTerminals))
        print("terminals = "+str(self.terminals))
        print("productionRules = "+str(self.productionRules))
        print("startingSymbol = "+self.startingSymbol)