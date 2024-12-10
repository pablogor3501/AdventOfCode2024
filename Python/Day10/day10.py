import sys
import numpy as np

moveDirection = {
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1]
}

def getFormatedInput(inputFile):
    input = [[int(n) for n in line] for line in inputFile.split("\n")]
    return np.array(input)

def getTrailheadStart(formatedInput):
    zeros = np.where(formatedInput == 0)
    zerosPos = [[zeros[0][i], zeros[1][i]] for i in range(len(zeros[0]))]
    return zerosPos

def notOutOfMap(nextPosY, nextPosX, maxY, maxX):
    return not (nextPosY > (maxY - 1) or nextPosY < 0 or nextPosX > (maxX - 1) or nextPosX < 0)

def getNextStep(pos, height, map, result, reached):
    posY, posX, nextHeight = pos[0], pos[1], height + 1
    for move in moveDirection.values():
        nextPosY, nextPosX = posY + move[0], posX + move[1]
        nextPos = [nextPosY, nextPosX]
        if notOutOfMap(nextPosY, nextPosX, len(map), len(map[posY])):
            if (height == 9 and pos not in reached):
                result[0] += 1
            elif (height == 9):
                result[1] += 1
                break
            reached.append(pos)
            if (map[nextPosY, nextPosX] == nextHeight):
                getNextStep(nextPos, nextHeight, map, result, reached)

inputFile = open(sys.argv[1]).read()
map = getFormatedInput(inputFile)
trailheadStarts = getTrailheadStart(map)
result = [0, 0]

for trailheadStart in trailheadStarts:
    getNextStep(trailheadStart, 0, map, result, reached = [])

print(f"Result for Advent Of Code 2024 -> Part 1: {result[0]}, Part 2: {result[1]}")