import sys
import itertools

formatedInput = open(sys.argv[1]).read().split("\n")
equations = []
result = [0, 0]

for line in formatedInput:
    lineData = line.split(": ")
    equations.append([lineData[0], lineData[1].split(" ")])

for equation in equations:
    eqResult, eqOperands = equation[0], equation[1]
    numOperations = (len(eqOperands) - 1)
    solutions = { True: 0, False: 0 }
    for operators in itertools.product("+*|", repeat=numOperations):
        obtainedRes = eqOperands[0]
        for i in range(numOperations):
            obtainedRes = str(eval(obtainedRes + operators[i] + eqOperands[i + 1])) if (operators[i] != "|") else f'{obtainedRes}{eqOperands[i + 1]}'
        if (obtainedRes == eqResult):
            solutions["|" in operators] = int(eqResult)
            break
    result[0] += solutions[False]
    result[1] += solutions[True] + solutions[False]

print(f"Result for Advent Of Code 2024 -> Part 1: {result[0]}, Part 2: {result[1]}")