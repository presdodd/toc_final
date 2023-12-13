from src.cfg_representation import CFG

def CFGtoCNF(cfg: CFG):
    #isolate the variables 
    nonTerminals = set(cfg.nonTerminals)
    terminals = list(cfg.terminals)
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
    
    #find all rules that contain the leftside Nonterminal of an eproduction
    #create a new rule for each rule that had that leftside Noterminal but erased.
    newRules = []
    for source in emptyProductions:
        for rule in productionRules:
            rightSide = rule[1]
            if source in rightSide:
                temp = rightSide.copy()
                temp.remove(source)
                newRightSide = temp
                newProductionRule = (rule[0],newRightSide)
                newRules.append(newProductionRule)
    for i in newRules:
        productionRules.append(i)

    #remove all productions with a single non terminal on right 
    for i in productionRules:
        if len (i[1]) == 1:
            for j in i[1]:
                for q in nonTerminals:
                    if str(q) == i[1][0]:
                        productionRules.remove(i)
  
    #to create new productions of new Nonterminal names, start at capital A. If A already
    #exists, pick the next one after. 
    letter = ord('A')
    if chr(letter) in nonTerminals:
        letter += 1
    
    updateDict = {}
    #identify all terminals and create a B -> b proudction accordingly 
    for terminal in terminals:
        if terminal == [''] or terminal == '':
            continue
        newNonTerminal = chr(letter) 
        nonTerminals.add(chr(letter))
        newRule = (newNonTerminal,[terminal])
        updateDict[terminal] = newNonTerminal
        productionRules.append(newRule)
        letter += 1

    #replace all non terminal symbols with the terminal symobls.
    #for example, S -> ( S ), replace ( with A and ) with B and so on
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

    #if there is a rule with a rightside production longer that 2, create new productions
    #to shorten the length. For example, S -> ABC turns into S -> AD with D -> BC
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
                nonTerminals.add(str(newLetter))

                newRules.append(newRule)
                rightSide.remove(letter1)
                rightSide.remove(letter2)
                rightSide.append(newLetter)
                length -= 1
            productionRules[index] = (rule[0],rightSide)

    #complete the list of production rules
    productionRules.extend(newRules)
    #make sure the empty string is not in the terminals
    if '' in terminals:
        terminals.remove('')
    #update the original cfg with the new values for the (non)terminals and productions
    cfg.nonTerminals = set(nonTerminals)
    cfg.productionRules = productionRules
    cfg.terminals = set(terminals)
    return cfg