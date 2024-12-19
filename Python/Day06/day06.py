import sys
import numpy as np

moveDirection = {
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1]
}

def getFormatedInput(inputFile):
    return np.array([[ch for ch in line] for line in inputFile.split("\n")])

def getInitialPos(map):
    initialPos = np.where(map == "^")
    return initialPos[0][0], initialPos[1][0]

def getNextDirID(currentDirectionID):
    return (currentDirectionID + 1) % 4

def checkOutOfMap(posY, posX, maxY, maxX):
    return (posY > (maxY - 1) or posY < 0 or posX > (maxX - 1) or posX < 0)

def getNextStep(posY, posX, direction):
    return posY + direction[0], posX  + direction[1]

def checkLoop(startY, startX, obsY, obsX, dirID, map):
    guardPosY, guardPosX = startY, startX
    directionID = dirID
    direction = moveDirection[directionID]
    tempMap = map.copy()
    tempMap[obsY][obsX] = "#"
    visited = set()
    while True:
        nextStepY, nextStepX = getNextStep(guardPosY, guardPosX, direction)
        if ((guardPosY, guardPosX, directionID) in visited): return True
        visited.add((guardPosY, guardPosX, directionID))
        if checkOutOfMap(nextStepY, nextStepX, len(tempMap), len(tempMap[guardPosY])): return False
        if (tempMap[nextStepY, nextStepX] == "#"):
            directionID = getNextDirID(directionID)
            direction = moveDirection[directionID]
        else:
            guardPosY, guardPosX = nextStepY, nextStepX

inputFile = open(sys.argv[1]).read()
map = getFormatedInput(inputFile)
initialPosY, initialPosX = getInitialPos(map)
guardPosY, guardPosX = getInitialPos(map)
directionID = 0
direction = moveDirection[directionID]
path = set()
result = [0, 0]

while(True):
    nextStepY, nextStepX = getNextStep(guardPosY, guardPosX, direction)
    path.add((guardPosY, guardPosX))
    if (map[guardPosY, guardPosX] != "X"):
        map[guardPosY, guardPosX] = "X"
        result[0] += 1
    if checkOutOfMap(nextStepY, nextStepX, len(map), len(map[guardPosY])): break
    if (map[nextStepY, nextStepX] == "#"):
        directionID = getNextDirID(directionID)
        direction = moveDirection[directionID]
        continue
    guardPosY, guardPosX = nextStepY, nextStepX

for pathY, pathX in path:
    if ((pathY, pathX) != (initialPosY, initialPosX)):
        result[1] += checkLoop(initialPosY, initialPosX, pathY, pathX, 0, map)

print(f"Result for Advent Of Code 2024 -> Part 1: {result[0]}, Part 2: {result[1]}")