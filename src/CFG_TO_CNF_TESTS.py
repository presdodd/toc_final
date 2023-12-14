import unittest
from src.cfg_representation import CFG
from src.CFG_TO_CNF import CFGtoCNF

class TestCFGtoCNF(unittest.TestCase):
    def test1(self):
        cfg1 = CFG({"L","S","R"},("[","]","8",",",),
                   ([("L",["[","S","]"]),
                     ("L",["[","]"]),
                     ("L",["8"]),
                     ("S",["L","R"]),
                     ("R",[""]),
                     ("R",[",","L","R"])]),
                     "S")
        print("INPUT:")
        cfg1.CFGPrint()
        print("\n")
        cnf1 = CFGtoCNF(cfg1)
        print("OUTPUT:")
        cnf1.CFGPrint()
        print("\n")

        correctCNF1 = CFG({"L","S","R","A","B","C","D","E","F"},{"[","]","8",","},
                          ([("L",["A","E"]),
                            ("L",["A","B"]), 
                            ("L",["8"]), 
                            ("S",["L","R"]), 
                            ("R",["D","F"]), 
                            ("R",["D","L"]), 
                            ("A",["["]), 
                            ("B",["]"]), 
                            ("C",["8"]), 
                            ("D",[","]), 
                            ("E",["S","B"]), 
                            ("F",["L","R"])]),
                            "S")
        print("testing cnf1 production rules, terminals and nonterminals")
        (self.assertEqual(cnf1.productionRules, correctCNF1.productionRules))
        (self.assertEqual(cnf1.terminals, (correctCNF1.terminals)))
        (self.assertEqual(cnf1.nonTerminals, (correctCNF1.nonTerminals)))

    def test2(self):
        cfg2 = CFG(("S"),("(",")"),
          (("S",["S","S"]),
           ("S",["(","S",")"]),
           ("S",[""])),
           "S")
        print("INPUT:")
        cfg2.CFGPrint()
        print("\n")
        cnf2 = CFGtoCNF(cfg2)
        print("OUTPUT:")
        cnf2.CFGPrint()
        print("\n")
        correctCNF2 = CFG({"S","A","B","C"},{"(",")"},
                          ([("S",["S","S"]), 
                            ("S",["A","C"]), 
                            ("S",["A","B"]), 
                            ("A",["("]), 
                            ("B",[")"]), 
                            ("C",["S","B"])]),
                            "S")
        print("testing cnf2 production rules, terminals and nonterminals")
        (self.assertEqual(cnf2.productionRules, correctCNF2.productionRules))
        (self.assertEqual(cnf2.terminals, (correctCNF2.terminals)))
        (self.assertEqual(cnf2.nonTerminals, (correctCNF2.nonTerminals)))