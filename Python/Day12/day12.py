import sys
import numpy as np
from operator import add

perimeterChecks = {
    0: [0, 1],
    1: [1, 0],
    2: [0, -1],
    3: [-1, 0]
}

diagonalChecks = {
    0: [1, 1],
    1: [1, -1],
    2: [-1, -1],
    3: [-1, 1]
}

def getFormatedInput(inputFile):
    input = [[plant for plant in line] for line in inputFile.split("\n")]
    return np.array(input)

def validPos(posY, posX, maxY, maxX):
    return (0 <= posY <= maxY - 1 and 0 <= posX <= maxX - 1)

def getNextDirID(currentDirectionID):
    return (currentDirectionID + 1) % 4

def getRegion(posY, posX, plant, region, formatedInput):
    region.add((posY, posX))
    for check in perimeterChecks.values():
        nextY, nextX = posY + check[0], posX + check[1]
        if validPos(nextY, nextX, len(formatedInput), len(formatedInput[posY])):
            if (formatedInput[nextY][nextX] == plant and (nextY, nextX) not in region):
                getRegion(nextY, nextX, plant, region, formatedInput)

def getPlants(formatedInput):
    regions = dict()
    for i in range(len(formatedInput)):
        for j in range(len(formatedInput[i])):
            plant = formatedInput[i][j]
            region = set()
            pos = (i, j)
            if (plant not in regions.keys()):
                getRegion(i, j, plant, region, formatedInput)
                regions[plant] = [region]
            else:
                if (not any([pos in regions[plant][k] for k in range(len(regions[plant]))])):
                    getRegion(i, j, plant, region, formatedInput)
                    regions[plant].append(region)
    return regions

def getPerimeter(pos, formatedInput):
    perimeter = 0
    for check in perimeterChecks.values():
        nextY, nextX = pos[0] + check[0], pos[1] + check[1]
        if validPos(nextY, nextX, len(formatedInput), len(formatedInput[pos[0]])):
            perimeter += 1 if (formatedInput[pos[0]][pos[1]] != formatedInput[nextY][nextX]) else 0
        else:
            perimeter += 1        
    return perimeter

def getSides(pos, region):
    dirsInRegion = []
    sides = 0
    for k, check in perimeterChecks.items():
        nextY, nextX = pos[0] + check[0], pos[1] + check[1]
        if ((nextY, nextX) in region): dirsInRegion.append(k)

    match len(dirsInRegion):
        case 0: sides = 4
        case 1: sides = 2
        case 2:
            intDir = list(map(add, perimeterChecks[dirsInRegion[0]], perimeterChecks[dirsInRegion[1]]))
            interiorY, interiorX = pos[0] + intDir[0], pos[1] + intDir[1]
            sides = 1 + ((interiorY, interiorX) not in region) if (sum(dirsInRegion) % 2 != 0) else 0
        case 3:
            diff = list(set(diagonalChecks.keys()) - set(dirsInRegion))
            diff.append(diff[0] - 1 if (diff[0] != 0) else 3)
            for k, check in diagonalChecks.items():
                interiorY, interiorX = pos[0] + check[0], pos[1] + check[1]
                sides += 1 if ((interiorY, interiorX) not in region and k not in diff) else 0
        case 4:
            for check in diagonalChecks.values():
                interiorY, interiorX = pos[0] + check[0], pos[1] + check[1]
                sides += 1 if ((interiorY, interiorX) not in region) else 0
    
    return sides

def getData(plants, formatedInput):
    plantData = dict()
    for plant, regions in plants.items():
        plantData[plant] = []
        for region in regions:
            area, perimeter, sides = 0, 0, 0
            for pos in region:
                perimeter += getPerimeter(pos, formatedInput)
                sides += getSides(pos, region)
                area += 1
            plantData[plant].append((area, perimeter, sides))
    return plantData

def getTotalPrice(data):
    totalPerimeter, totalSides = 0, 0
    for values in data.values():
        for value in values:
            totalPerimeter += value[0] * value[1]
            totalSides += value[0] * value[2]
    return [totalPerimeter, totalSides]

inputFile = open(sys.argv[1]).read()
formatedInput = getFormatedInput(inputFile)
plants = getPlants(formatedInput)
data = getData(plants, formatedInput)
result = getTotalPrice(data)

print(f"Result for Advent Of Code 2024 -> Part 1: {result[0]}, Part 2: {result[1]}")