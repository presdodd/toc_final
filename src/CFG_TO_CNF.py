try:
    from src.cfg_representation import CFG
except:
    from cfg_representation import CFG


cfg = CFG(("L","S","R"),("[","]","8",",",""),
          (("L",["[","S","]"]),
           ("L",["[","]"]),
           ("L",["8"]),
           ("S",["L","R"]),
           ("R",[""]),
           ("R",[",","L","R"])),
           "S")

cfg2 = CFG(("S"),("(",")"),
          (("S",["S","S"]),
           ("S",["(","S",")"]),
           ("S",[""])),
           "S")



def printer(rules):
    for rule in rules:
        print(rule[0], "→", "".join(rule[1]))



def CFGtoCNF(cfg: CFG):
    nonTerminals = set(cfg.nonTerminals)
    terminals = cfg.terminals
    productionRules = list(cfg.productionRules)
    startSymbol = cfg.startingSymbol
   
    #remove ε-productions X → _  and  #Remove unit productions X → Y
    emptyProductions = []
    for rule in productionRules:
        rightSide = rule[1]
        if rightSide == [""]:
            leftSide = rule[0]
            emptyProductions.append(leftSide)
            productionRules.remove(rule)
    
    newRules = []
    for source in emptyProductions:
        for rule in productionRules:
            rightSide = rule[1]
            if source in rightSide:
                
                dumby = rightSide.copy()
                dumby.remove(source)
                
                newRightSide = dumby
                
                
                newProductionRule = (rule[0],newRightSide)
                
                
                newRules.append(newProductionRule)
    

    for i in newRules:
        productionRules.append(i)

 

 
    for i in productionRules:
        if len (i[1]) == 1:
            for j in i[1]:
                for q in nonTerminals:
                    if str(q) == i[1][0]:
                        productionRules.remove(i)
  


    letter = ord('A')
    if chr(letter) in nonTerminals:
        letter += 1
    
    updateDict = {}

    for terminal in terminals:
        if terminal == [''] or terminal == '':
            continue
        newNonTerminal = chr(letter) 
        nonTerminals.add(chr(letter))
        newRule = (newNonTerminal,[terminal])
        updateDict[terminal] = newNonTerminal
        productionRules.append(newRule)
        letter += 1

    for rule in productionRules:
        if rule[0] in updateDict.values():
            continue

        rightSide = rule[1]

        if len(rightSide) == 1:
            continue
        for term in rightSide:

            index = rightSide.index(term)
            if term in updateDict.keys():
                rightSide[index] = updateDict[term]
        newRule = (rule[0],rightSide)

    newRules = []
    for rule in productionRules:

        rightSide = rule[1]
        if len(rightSide) > 2:
            index = productionRules.index(rule)
            length = len(rightSide)
            while length > 2:
                letter1 = rightSide[-2]
                letter2 = rightSide[-1]
                newLetter = chr(letter)
                letter += 1
                if chr(letter) in nonTerminals:
                    letter += 1
                newRule = (str(newLetter),[letter1,letter2])
                newRules.append(newRule)
                rightSide.remove(letter1)
                rightSide.remove(letter2)
                rightSide.append(newLetter)
                length -= 1
            productionRules[index] = (rule[0],rightSide)
            

    for i in newRules:
        productionRules.append(i)
    printer(productionRules)



#note that my use of the "letter" variable will overlap preexisting letters


CFGtoCNF(cfg2)