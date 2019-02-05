#################################################################################################################################
#                                                                                                                               #
#                                                                                                                               #
#                                                                                                                               #
#################################################################################################################################


import time

puzzleFile = open('S_One.txt', 'r')
puzzle = puzzleFile.read()
#numbered = [ord(i) for i in puzzle if not i == 35]
numbered = [ord(i) for i in puzzle]

#temp = []
#for i in range(15,15+3):
#    temp.append(i)
#print(temp)

#print(puzzle[135])

allNum = [49,50,51,52,53,54,55,56,57]
possibilities = [allNum[:]] * 182
origPoss = []
for i in possibilities:
    origPoss.append(i[:])
asciiNumCode = ['1','2','3','4','5','6','7','8','9']
notNumbers = []

for i in range(181):
    if numbered[i] == 35:
        notNumbers.append(i)



################Check for single values#################

def RowCheck(numbered, possibilities):
    for i in range(15,169,14):
        for j in range(i,i+12):
            for k in possibilities[j]:
                if not (possibilities[j][k] == possibilities[x][y] for x in possibilities[j] for y in range(i,1+12) if (not y == k and not x == j)):
                    possibilities[j] = possibilities[j][k]
    return possibilities

def ColCheck(numbered, possibilities):
    for i in range(15,26):
        for j in range(i,169,14):
            for k in possibilities[j]:
                if not (possibilities[j][k] == possibilities[x][y] for x in possibilities[j] for y in range(i,169,14) if (not y == k and not x == j)):
                    possibilities[j] = possibilities[j][k]
    return possibilities

def BoxCheck(numbered, possibilities):
    i = 15
    counter = 0
    while i < 136:
        counter += 1
        for j in range(i,i+28,14):
            for k in range(j,j+3):
                for m in possibilities[k]:
                    if not (possibilities[k][m] == possibilities[x][y] for x in possibilities[k] for y in range(z,z+3) for z in range(i,i+28,14) if (not y == m and not x == k)):
                        possibilities[k] = possibilities[k][m]



                #if numbered[k] in allNum:
                #    for m in range(i,i+28,14):
                #        for n in range(m,m+3):
                #            if numbered[j] in possibilities[n]:
                #                temp = possibilities[n][:]
                #                temp.remove(numbered[j])
                #                possibilities[n] = temp[:]



        if counter == 3:
            counter = 0
            i += 6
        else:
            i += 4
    return possibilities




################"Cross out" values######################

def RowCross(numbered, puzzle, allNum, possibilities):
    for i in range(0,169,14):
        for j in range(i,i+12):
            if numbered[j] in allNum:
                for k in range(i,i+12):
                    if numbered[j] in possibilities[k]:
                        temp = possibilities[k][:]
                        temp.remove(numbered[j])
                        possibilities[k] = temp[:]
    return possibilities

def ColCross(numbered, puzzle, allNum, possibilities):
    for i in range(12):
        for j in range(i,i+169,14):
            if numbered[j] in allNum:
                for k in range(i,i+169,14):
                    if numbered[j] in possibilities[k]:
                        temp = possibilities[k][:]
                        temp.remove(numbered[j])
                        possibilities[k] = temp[:]
    return possibilities

def BoxCross(numbered, allNum, possibilities):
    i = 15
    counter = 0
    while i < 136:
        counter += 1
        for j in range(i,i+28,14):
            for k in range(j,j+3):
                if numbered[k] in allNum:
                    for m in range(i,i+28,14):
                        for n in range(m,m+3):
                            if numbered[j] in possibilities[n]:
                                temp = possibilities[n][:]
                                temp.remove(numbered[j])
                                possibilities[n] = temp[:]
        if counter == 3:
            counter = 0
            i += 6
        else:
            i += 4
    return possibilities

def CrossPositionSolutions(numbered, puzzle, allNum, possibilities):
    for i in range(181):
        if not i in notNumbers and numbered[i] == 32:
            if len(possibilities[i]) == 1:
                #print(puzzle[i-1], end = '  ')
                #print(puzzle[i], end = '  ')
                #print(puzzle[i+1])
                #input('   ')
                numbered[i] = possibilities[i][0]
                puzzle = puzzle[:i] + str(chr(possibilities[i][0])) + puzzle[i+1:]
    return numbered, puzzle

def RunCheck(numbered, puzzle, allNum, possibilities):
    possibilities = RowCross(numbered, puzzle, allNum, possibilities)
    possibilities = ColCross(numbered, puzzle, allNum, possibilities)
    possibilities = BoxCross(numbered, allNum, possibilities)
    possibilities = RowCheck(numbered, possibilities)
    possibilities = ColCheck(numbered, possibilities)
    numbered, puzzle = CrossPositionSolutions(numbered, puzzle, allNum, possibilities)
    return possibilities, numbered, puzzle

def CheckSolution(notNumbers, numbered):
    solution = 1
    for i in range(181):
        if not i in notNumbers:
            if not numbered[i] == 32:
                solution = 0
    return solution



#for i in range(20):
#    #print(possibilities)
#    #time.sleep(1)
#    possibilities, numbered, puzzle = RunCheck(numbered, puzzle, allNum, possibilities)
#    print(puzzle, end = '\n\n')
#    if CheckSolution(notNumbers, numbered):
#        print('solution found')

while not CheckSolution(notNumbers, numbered):
    possibilities, numbered, puzzle = RunCheck(numbered, puzzle, allNum, possibilities)
    print(puzzle, end = '\n\n')
    if CheckSolution(notNumbers, numbered):
        print('solution found')
    print(possibilities[39])
    print(possibilities[51])

#print(origPoss)
#print(possibilities)