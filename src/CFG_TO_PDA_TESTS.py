import unittest
from src.pda_representation import PDA
from src.cfg_representation import CFG
from src.CFG_To_PDA import CFG_To_PDA


class TestCFG_To_PDA(unittest.TestCase):
    def test1(self):
        cfg1 = CFG({"E", "L"}, {"x", "(", ")"},
                   [("E", ["(", "L", ")"]), ("E", ["x"]), ("L", ["L", "E"]), ("L", ["E", "E"])],
                  "E")
        print("INPUT:")
        cfg1.CFGPrint()
        print("\n")
        pda1 = CFG_To_PDA(cfg1)
        print("OUTPUT:")
        pda1.PDAPrint()
        print("\n")

        correctPda1 = PDA(
            {'1', '11', '6', '7', '13', '8', '4', '2', '14', '16', '10', '15', '3', '9', '5', '12'},
            {'x', ')', '('},
            {'x', 'L', '(', 'T', ')', 'E'},
            {('3', '9', '', 'E'), ('3', '14', '', 'L'), ('3', '11', '', 'L'), ('3', '3', 'x', 'x'), ('3', '3', ')', ')'),
             ('3', '4', '', 'T'), ('3', '3', '(', '('), ('3', '5', '', 'E')},
            {('1', '2', '', 'T'), ('9', '10', '', 'x'), ('15', '16', '', 'E'), ('7', '8', '', '('), ('14', '15', '', 'E'),
             ('13', '3', '', ''), ('8', '3', '', ''), ('6', '7', '', 'L'), ('10', '3', '', ''), ('11', '12', '', 'E'),
             ('2', '3', '', 'E'), ('5', '6', '', ')'), ('12', '13', '', 'L'), ('16', '3', '', '')},
            "1",
            {'4'}
        )

        self.assertEqual(self.checkPdaEquals(pda1, correctPda1), True)

    def test2(self):
        cfg2 = CFG(
            {'S', 'A', 'C'},
            {'a', 'b'},
            [('S', ['A', 'b']), ('S', ['b', 'A']), ('A', ['C', 'A', 'C']), ('A', ['a']), ('C', ['a']), ('C', ['b'])],
            'S'
        )
        print("INPUT:")
        cfg2.CFGPrint()
        print("\n")
        pda2 = CFG_To_PDA(cfg2)
        print("OUTPUT:")
        pda2.PDAPrint()
        print("\n")

        correctPda2 = PDA(
            {'10', '8', '15', '9', '13', '18', '17', '19', '2', '20', '14', '11', '12', '4', '1', '7', '3', '5', '6', '16'},
            {'a', 'b'},
            {'a', 'T', 'C', 'A', 'b', 'S'},
            {('3', '5', '', 'S'), ('3', '15', '', 'A'), ('3', '8', '', 'S'), ('3', '3', 'a', 'a'), ('3', '19', '', 'C'), ('3', '17', '', 'C'), ('3', '3', 'b', 'b'), ('3', '11', '', 'A'), ('3', '4', '', 'T')},
            {('17', '18', '', 'a'), ('19', '20', '', 'b'), ('11', '12', '', 'C'), ('7', '3', '', ''),
             ('18', '3', '', ''), ('2', '3', '', 'S'), ('13', '14', '', 'C'), ('16', '3', '', ''), ('5', '6', '', 'b'),
             ('20', '3', '', ''), ('8', '9', '', 'A'), ('15', '16', '', 'a'), ('10', '3', '', ''), ('9', '10', '', 'b'),
             ('1', '2', '', 'T'), ('6', '7', '', 'A'), ('14', '3', '', ''), ('12', '13', '', 'A')},
            '1',
            {'4'}
        )

        self.assertEqual(self.checkPdaEquals(pda2, correctPda2), True)

    def test3(self):
        print("INPUT:")
        cfg3 = CFG({"1"}, {"b"},
                   [('1', ['b'])],
                   "1")
        cfg3.CFGPrint()
        print("\n")
        pda3 = CFG_To_PDA(cfg3)
        print("OUTPUT:")
        pda3.PDAPrint()
        print("\n")

        correctPda3 = PDA(
            {'1', '4', '2', '3', '5', '6'},
            {'b'},
            {'T', '1', 'b'},
            {('3', '4', '', 'T'), ('3', '3', 'b', 'b'), ('3', '5', '', '1')},
            {('5', '6', '', 'b'), ('6', '3', '', ''), ('1', '2', '', 'T'), ('2', '3', '', '1')},
            "1",
            {'4'}
        )

        self.assertEqual(self.checkPdaEquals(pda3, correctPda3), True)





    def checkPdaEquals(self, pda1:PDA, pda2:PDA): # check if 2 pdas are equal
        self.assertEqual(pda1.states, pda2.states)
        self.assertEqual(pda1.inputAlphabet, pda2.inputAlphabet)
        self.assertEqual(pda1.stackAlphabet, pda2.stackAlphabet)
        self.assertEqual(pda1.RTransitionFunctions, pda2.RTransitionFunctions)
        self.assertEqual(pda1.ETransitionFunctions, pda2.ETransitionFunctions)
        self.assertEqual(pda1.startState, pda2.startState)
        self.assertEqual(pda1.acceptingStates, pda2.acceptingStates)
        return True


