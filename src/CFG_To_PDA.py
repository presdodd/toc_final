from src.pda_representation import PDA
from src.cfg_representation import CFG
# Write a function that can translate a CFG into a PDA following the algorithm discussed during week 8 of class

def CFG_To_PDA(cfg: CFG):
    Q = {"1", "2", "3", "4"}
    sigma = {}
    gamma = {"T", "S"}
    R = {("3", "4", "", "T")}
    E = {("1", "2", "", "T"), ("2", "3", "", "S")}
    s = "1"
    F = {"4"}

    pda = PDA(Q, sigma, gamma, R, E, s, F)
    i = 5
    for rule in cfg.productionRules:
        pda.addRTransition("3", str(i), "", rule[0])


        for item in rule[1].reversed():
            if (item not in pda.stackAlphabet):
                pda.stackAlphabet.add(item)
            pda.addETrantition(str(i), str(i+1), "", item)
            i += 1
        # add an empty transition back to 3
        i += 1

    for t in cfg.terminals:
        pda.addRTransition("3", "3", t, t)



