from src.cfg_representation import CFG
#def __init__(self, nonTerminals: Set[str], terminals: Set[str],
 #                productionRules: Set[Tuple[str, List[str]]], startingSymbol: str):

# Algorithm:
# 1. Remove unit productions X → Y and ε-productions X → _
# 2. Replace terminal t with new nonterminal Tt, and add
#       Tt → t
# 3. Split X → Y1 ... Yk (for k > 2) into
#       X → Y1 Z1 Z1 → Y2 Z2 ... Z(k-2) → Y(k-1) Yk


# L -> [ S ]
# L -> [ ]
# L -> 8
# S -> L R
# R ->
# R -> , L R

cfg = CFG(("L","S","R"),("8","[","]",",",""),
          (("L",["[","S","]"]),
           ("L",["[","]"]),
           ("L",["8"]),
           ("S",["L","R"]),
           ("R",[""]),
           ("R",[",","L","R"])),
           "S")

def printer(rules):
    for rule in rules:
        print(rule[0], "→", "".join(rule[1]))

        

def CFGtoCNF(cfg: CFG):
    nonTerminals = cfg.nonTerminals
    terminals = cfg.terminals
    productionRules = list(cfg.productionRules)
    startSymbol = cfg.startingSymbol
 
    printer(productionRules)

    #remove ε-productions X → _


    #Remove unit productions X → Y
    




CFGtoCNF(cfg)