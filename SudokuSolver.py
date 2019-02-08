#################################################################################################################################
#                                                                                                                               #
#                                                                                                                               #
#                                                                                                                               #
#################################################################################################################################

import time

puzzleFile = open('s03c.txt', 'r')
puzzle = puzzleFile.read()
numbered = [ord(i) for i in puzzle]

#temp = []
#for i in range(15,15+3):
#    temp.append(i)
#print(temp)

#print(puzzle[135])

allNum = [49,50,51,52,53,54,55,56,57]
possibilities = [allNum[:]] * 182
asciiNumCode = ['1','2','3','4','5','6','7','8','9']
notNumbers = []

for i in range(181):
    if numbered[i] == 35:
        notNumbers.append(i)
    elif not numbered[i] == 32:
        possibilities[i] = [numbered[i]]

################Check for single values#################

def RowCheck(numbered, possibilities):              #something is very wrong with this function
    for i in range(15,169,14):
        for j in range(i,i+11):
            for k in possibilities[j]:
                solution = 1
                for m in range(i,i+11):
                    if not m in notNumbers and k in possibilities[m] and not m == j:
                        solution = 0
                if solution == 1:
                    if type(k) == int:
                        possibilities[j] = [k]
                    else:
                        possibilities[j] = k
    return possibilities

def ColCheck(numbered, possibilities):
    for i in range(15,26):
        for j in range(i,169,14):
            for k in possibilities[j]:
                solution = 1
                for m in range(i,169,14):
                    if not m in notNumbers and k in possibilities[m] and not m == j:
                        solution = 0
                if solution == 1:
                    if type(k) == int:
                        possibilities[j] = [k]
                    else:
                        possibilities[j] = k
    return possibilities

def BoxCheck(numbered, possibilities):
    i = 15
    counter = 0
    while i < 136:
        counter += 1
        for j in range(i,i+29,14):
            for k in range(j,j+3):
                for m in possibilities[k]:
                    solution = 1
                    for n in range(i,i+29,14):
                        for x in range(n,n+3):
                            if m in possibilities[x] and not x == k:
                                solution = 0
                    if solution == 1:
                        if type(m) == int:
                            possibilities[k] = [m]
                        else:
                            possibilities[k] = m
        if counter == 3:
            counter = 0
            i += 48
        else:
            i += 4
    return possibilities

################"Cross out" values######################

def RowCross(numbered, allNum, possibilities):
    for i in range(0,169,14):
        for j in range(i,i+12):
            if numbered[j] in allNum:
                for k in range(i,i+12):
                    if numbered[j] in possibilities[k]:
                        temp = possibilities[k][:]
                        temp.remove(numbered[j])
                        if type(temp) == int:
                            possibilities[k] = [temp[:]]
                        else:
                            possibilities[k] = temp[:]
    return possibilities

def ColCross(numbered, allNum, possibilities):
    for i in range(12):
        for j in range(i,i+169,14):
            if numbered[j] in allNum:
                for k in range(i,i+169,14):
                    if numbered[j] in possibilities[k]:
                        temp = possibilities[k][:]
                        temp.remove(numbered[j])
                        if type(temp) == int:
                            possibilities[k] = [temp[:]]
                        else:
                            possibilities[k] = temp[:]
    return possibilities

def BoxCross(numbered, allNum, possibilities):
    i = 15
    counter = 0
    while i < 136:
        counter += 1
        for j in range(i,i+29,14):
            for k in range(j,j+3):
                if numbered[k] in allNum:
                    for m in range(i,i+29,14):
                        for n in range(m,m+3):
                            if numbered[k] in possibilities[n]:
                                temp = possibilities[n][:]
                                temp.remove(numbered[k])
                                if type(temp) == int:
                                    possibilities[n] = [temp[:]]
                                else:
                                    possibilities[n] = temp[:]
        if counter == 3:
            counter = 0
            i += 48
        else:
            i += 4
    return possibilities

def CrossPositionSolutions(numbered, puzzle, allNum, possibilities):
    for i in range(181):
        if not i in notNumbers and numbered[i] == 32:
            if len(possibilities[i]) == 1:
                numbered[i] = possibilities[i][0]
                puzzle = puzzle[:i] + str(chr(possibilities[i][0])) + puzzle[i+1:]
    return numbered, puzzle

def CheckErrors(numbered, puzzle):
    for i in range(15,169,14):
        tempValues = []
        for j in range(i,i+12):
            if not numbered[j] == 32 and not j in notNumbers:
                if numbered[j] in tempValues:
                    print(puzzle, end = '\n\n')
                    raise Exception('Duplicates in a row. Second one found at position {0}'.format(j))
                else:
                    tempValues.append(numbered[j])
    for i in range(12):
        tempValues = []
        for j in range(i,i+169,14):
            if not numbered[j] == 32 and not j in notNumbers:
                if numbered[j] in tempValues:
                    print(puzzle, end = '\n\n')
                    raise Exception('Duplicates in a column. Second one found at position {0}'.format(j))
                else:
                    tempValues.append(numbered[j])
    i = 15
    counter = 0
    while i < 136:
        counter += 1
        tempValues = []
        for j in range(i,i+29,14):
            for k in range(j,j+3):
                if not numbered[k] == 32 and not k in notNumbers:
                    if numbered[k] in tempValues:
                        print(puzzle, end = '\n\n')
                        raise Exception('Duplicates in a box. Second one found at position {0}'.format(k))
                    else:
                        tempValues.append(numbered[k])
        if counter == 3:
            counter = 0
            i += 48
        else:
            i += 4

    return
            

def RunCheck(numbered, puzzle, allNum, possibilities):          #there is a function that removes too many possibilities, number 80 becomes []
    print(possibilities[80])
    possibilities = RowCheck(numbered, possibilities)
    print('1')
    numbered, puzzle = CrossPositionSolutions(numbered, puzzle, allNum, possibilities)
    CheckErrors(numbered, puzzle)
    possibilities = ColCheck(numbered, possibilities)
    print('1')
    numbered, puzzle = CrossPositionSolutions(numbered, puzzle, allNum, possibilities)
    CheckErrors(numbered, puzzle)
    possibilities = BoxCheck(numbered, possibilities)
    print('1')
    numbered, puzzle = CrossPositionSolutions(numbered, puzzle, allNum, possibilities)
    CheckErrors(numbered, puzzle)
    possibilities = RowCross(numbered, allNum, possibilities)
    print('1')
    numbered, puzzle = CrossPositionSolutions(numbered, puzzle, allNum, possibilities)
    CheckErrors(numbered, puzzle)
    possibilities = ColCross(numbered, allNum, possibilities)
    print('1')
    numbered, puzzle = CrossPositionSolutions(numbered, puzzle, allNum, possibilities)
    CheckErrors(numbered, puzzle)
    possibilities = BoxCross(numbered, allNum, possibilities)
    print('1')
    numbered, puzzle = CrossPositionSolutions(numbered, puzzle, allNum, possibilities)
    CheckErrors(numbered, puzzle)
    print('2')
    numbered, puzzle = CrossPositionSolutions(numbered, puzzle, allNum, possibilities)
    CheckErrors(numbered, puzzle)
    return possibilities, numbered, puzzle

def CheckSolution(notNumbers, numbered):
    solution = 1
    for i in range(181):
        if not i in notNumbers:
            if numbered[i] == 32:
                solution = 0
    return solution



#for i in range(20):
#    #print(possibilities)
#    #time.sleep(1)
#    possibilities, numbered, puzzle = RunCheck(numbered, puzzle, allNum, possibilities)
#    print(puzzle, end = '\n\n')
#    if CheckSolution(notNumbers, numbered):
#        print('solution found')

print(puzzle, end = '\n\n')

while not CheckSolution(notNumbers, numbered):
    possibilities, numbered, puzzle = RunCheck(numbered, puzzle, allNum, possibilities)
    print(puzzle, end = '\n\n')
    if CheckSolution(notNumbers, numbered):
        print('solution found')