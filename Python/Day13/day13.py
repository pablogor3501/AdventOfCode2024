import sys
import numpy as np

def getSolution(bA, bB, p):
    a, b = np.array([[bA[0], bB[0]], [bA[1], bB[1]]]), np.array(p)
    solution = [float(n) for n in np.linalg.solve(a, b)]
    valid = all([(abs(n - round(n)) < 10**-3) for n in solution])
    return [round(n) for n in solution], valid

'''
def getSolution(bA, bB, p):
    A, b = np.array([[bA[0], bB[0]], [bA[1], bB[1]]]), np.array(p)
    AInv = np.linalg.inv(A)
    solution = [float(n) for n in np.dot(AInv, b)]
    valid = all([(abs(n - round(n)) < 10**-3) for n in solution])
    return [round(n) for n in solution], valid

def getSolution(bA, bB, p):    
    a, b = np.array([[bA[0], bB[0]], [bA[1], bB[1]]]), np.array(p)
    func = lambda x: x[0] * 3 + x[1] + np.linalg.norm(a @ x - b)
    sol = [float(n) for n in minimize(func, np.zeros(2), method='Nelder-Mead', bounds=((0, None), (0, None))).x]
    valid = all([(abs(n - round(n)) < 10**-3) for n in solution])
    return [round(n) for n in solution], valid

def getSolution(bA, bB, p):
    a, b = np.array([[bA[0], bB[0]], [bA[1], bB[1]]]), np.array(p)
    sol = [float(n) for n in linalg.solve(a, b)]
    valid = all([(abs(n - round(n)) < 10**-3) for n in solution])
    return [round(n) for n in solution], valid
'''

inputFile = open(sys.argv[1]).read()
machines = [machine for machine in inputFile.split("\n\n")]
result = [0, 0]
for machine in machines:
    info = machine.split("\n")
    buttonA = [int(n) for n in info[0].lstrip("Button A: X+").split(", Y+")]
    buttonB = [int(n) for n in info[1].lstrip("Button A: X+").split(", Y+")]
    price = [int(n) for n in info[2].lstrip("Prize: X=").split(", Y=")]
    solution, validSolution = getSolution(buttonA, buttonB, price)
    if (solution[0] <= 100 and solution[1] <= 100 and validSolution):
        result[0] += solution[0] * 3 + solution[1] * 1
    price = [p + 10000000000000 for p in price]
    solution, validSolution = getSolution(buttonA, buttonB, price)
    if (validSolution):
        print(solution)
        result[1] += solution[0] * 3 + solution[1] * 1

print(f"Result for Advent Of Code 2024 -> Part 1: {result[0]}, Part 2: {result[1]}")