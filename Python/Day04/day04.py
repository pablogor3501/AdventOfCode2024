import sys
import re

def checkXMASCombinations(matrix, line, ch):
    combs = [''.join((matrix[line][ch+i]) for i in range(4) if (ch + i < len(matrix[i]))),
             ''.join((matrix[line+i][ch-i]) for i in range(4) if (line + i < len(matrix) and ch - i >= 0)),
             ''.join((matrix[line+i][ch+i]) for i in range(4) if (line + i < len(matrix) and ch + i < len(matrix[i]))),
             ''.join((matrix[line+i][ch])  for i in range(4) if (line + i < len(matrix)))]
    return combs.count("XMAS") + combs.count("SAMX")

def checkMASCombinations(matrix, line, ch):
    xmas = ''.join((matrix[line+i][ch+j]) for i in range(3) for j in range(3) if (line + i < len(matrix) and ch + j < len(matrix[i])))
    regex = "(M.M.A.S.S|M.S.A.M.S|S.M.A.S.M|S.S.A.M.M)"
    return len(re.findall(regex, xmas))

result = [0,0]
formatedInput = [list(line) for line in open(sys.argv[1]).read().split("\n")]

for i in range(len(formatedInput)):
    for j in range(len(formatedInput[i])):
        result[0] += checkXMASCombinations(formatedInput, i, j)
        result[1] += checkMASCombinations(formatedInput, i, j)

print(f"Result for Advent Of Code 2024 -> Part 1: {result[0]}, Part 2: {result[1]}")