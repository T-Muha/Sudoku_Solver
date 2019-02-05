puzzleFile = open('S_One.txt', 'r')
puzzle = puzzleFile.read()
numbered = [ord(i) for i in puzzle if not i == 35]

#temp = []
#for i in range(1,10):
#    temp.append(i)
#print(temp)

allNum = [1,2,3,4,5,6,7,8,9]
possibilities = [allNum[:]] * 81
asciiNumCode = ['1','2','3','4','5','6','7','8','9']
notNumbers = []

for i in range(81):
    if numbered[i] == 35:
        notNumbers.append(i)

def RowCheck(numbered, puzzle, allNum, possibilities):
    for i in range(1,72):
        for j in range(i,i+9):
            if numbered[j] in allNum:
                for k in range(j,j+9):
                    possibilities[k].remove(numbered[j])
    return possibilities

def ColCheck(numbered, puzzle, allNum, possibilities):
    for i in range(1,10):
        for j in range(i,i+72):
            if numbered[j] in allNum:
                for k in range(j,j+72):
                    possibilities[k].remove[numbered[j]]
    return possibilities

def CheckPositionSolutions(numbered, puzzle, allNum, possibilities):
    for i in range(81):
        if not i in notNumbers and numbered[i] == 32:
            if len(possibilities[i]) == 1:
                numbered[i] = possibilities[i]
                puzzle[i] = asciiNumCode[possibilities[i]-1]
    return numbered, puzzle

def RunCheck(numbered, puzzle, allNum, possibilities):
    possibilities = RowCheck(numbered, puzzle, allNum, possibilities)
    possibilities = ColCheck(numbered, puzzle, allNum, possibilities)
    CheckPositionSolutions(numbered, puzzle, allNum, possibilities)
    return possibilities, numbered, puzzle

def CheckSolution(notNumbers, numbered):
    solution = 1
    for i in range(1,82):
        if not i in notNumbers:
            if not numbered[i] == 32:
                solution = 0
    return solution

possibilities, numbered, puzzle = RunCheck(numbered, puzzle, allNum, possibilities)
print(puzzle)
if CheckSolution(notNumbers, numbered):
    print('solution found')