from src.pda_representation import PDA
from src.cfg_representation import CFG
# Write a function that can translate a CFG into a PDA following the algorithm discussed during week 8 of class

def CFG_To_PDA(cfg: CFG):
    Q = {"1", "2", "3", "4"}
    sigma = set()
    gamma = {"T", cfg.startingSymbol}
    R = {("3", "4", "", "T")}
    E = {("1", "2", "", "T"), ("2", "3", "", cfg.startingSymbol)}
    s = "1"
    F = {"4"}

    pda = PDA(Q, sigma, gamma, R, E, s, F)

    i = 5
    # rule = (nonTerminal, [terminals and nonTerminals]) e.g. rule = ("S", ["a","S","b"])
    for rule in cfg.productionRules:
        pda.addRTransition("3", str(i), "", rule[0]) # e.g. 3 --(*,-S)--> 5

        # iterate backwards
        rule[1].reverse()
        for item in rule[1]:
            pda.addETransition(str(i), str(i+1), "", item)
            i += 1
        # turn list back to normal
        rule[1].reverse()
        # add an empty transition back to 3
        pda.addETransition(str(i), "3", "", "")
        i += 1

    # adding transitions for nonTerminals
    for t in cfg.terminals:
        pda.addRTransition("3", "3", t, t)

    return pda