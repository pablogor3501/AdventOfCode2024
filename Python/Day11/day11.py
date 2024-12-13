import sys

def getFormatedInput(inputFile):
    return {n: 1 for n in inputFile.split(" ")}

def addRock(rock, rocks):
    if (rock not in rocks.keys()): rocks[rock] = 1
    else: rocks[rock] += 1

def checkRocks(rocks, blinks):
    if (blinks == 0): return sum(rocks.values())
    tempRocks = {}
    for rock, amount in rocks.items():
        if (rock == '0'):
            tempRocks['1'] = tempRocks.get('1', 0) + amount
        elif (len(rock) % 2 == 0):
            middle = int(len(rock) / 2)
            newRockLeft, newRockRight = str(int(rock[:middle])), str(int( rock[middle:]))
            tempRocks[newRockLeft] = tempRocks.get(newRockLeft, 0) + amount
            tempRocks[newRockRight] = tempRocks.get(newRockRight, 0) + amount
        else:
            newRock = str(int(rock) * 2024)
            tempRocks[newRock] = tempRocks.get(newRock, 0) + amount
    return checkRocks(tempRocks, blinks - 1)

inputFile = open(sys.argv[1]).read()
totalRocks = getFormatedInput(inputFile)
result = [checkRocks(totalRocks, 25), checkRocks(totalRocks, 75)]

print(f"Result for Advent Of Code 2024 -> Part 1: {result[0]}, Part 2: {result[1]}")