import unittest
from src.pda_representation import PDA
from src.cfg_representation import CFG
from src.CFG_To_PDA import CFG_To_PDA


class TestCFG_To_PDA(unittest.TestCase):
    def test1(self):
        cfg1 = CFG({"E", "L"}, {"x", "(", ")"},
                   (("E", ["(", "L", ")"]), ("E", ["x"]), ("L", ["L", "E"]), ("L", ["E", "E"])),
                  "E")
        cfg1.CFGPrint()
        print("\n")
        pda1 = CFG_To_PDA(cfg1)
        pda1.PDAPrint()
