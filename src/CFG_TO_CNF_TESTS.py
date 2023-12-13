#cf = CFG(("L","S","R"),("[","]","8",",",""),
#           (("L",["[","S","]"]),
#            ("L",["[","]"]),
#            ("L",["8"]),
#            ("S",["L","R"]),
#            ("R",[""]),
#            ("R",[",","L","R"])),
#            "S")

# cfg2 = CFG(("S"),("(",")"),
#           (("S",["S","S"]),
#            ("S",["(","S",")"]),
#            ("S",[""])),
#            "S")


#printer function that print a list of productions into a readable form. 
# def printer(rules):
#     for rule in rules:
#         print(rule[0], "→", "".join(rule[1]))
