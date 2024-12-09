import sys

def getFormatedInput(inputFile):
    formatedInput = []
    id = 0
    for i in range(0, len(inputFile), 2):
        if (i == len(inputFile) - 1):
            formatedInput.append([int(inputFile[-1]), 0, id])
        else:
            formatedInput.append([int(inputFile[i]), int(inputFile[i+1]), id])
        id += 1
    return formatedInput

def getDiskMap(formatedInput, file = False):
    diskMap = []
    if (file):
        for block in formatedInput:
            diskMap += [block[2]] * block[0] + block[3:] + ['.'] * block[1]
        return diskMap
    else:
        for block in formatedInput:
            diskMap += [block[2]] * block[0] + ['.'] * block[1]
        return diskMap

def getBlockDiskMap(formatedInput):
    diskMap = getDiskMap(formatedInput)
    last = 0
    for i in range(len(diskMap) - 1, 0, -1):
        if (diskMap[i] != '.' and i > last):
            for j in range(last, i - 1):
                if (diskMap[j] == '.'):
                    diskMap[i], diskMap[j] = diskMap[j], diskMap[i]
                    last = j
                    break
    return diskMap

def getFileDiskMap(formatedInput):
    for i in range(len(formatedInput) - 1, 0, -1):
        for j in range(i):
            freeSpace = formatedInput[j][1]
            if (formatedInput[i][0] != '.' and formatedInput[i][0] <= freeSpace):
                formatedInput[j][1] -= formatedInput[i][0]
                formatedInput[j].extend([formatedInput[i][2]] * formatedInput[i][0])
                formatedInput[i][2] = '.'
                break
    return getDiskMap(formatedInput, True)

def getCheckSum(compactDiskMap, file = False):
    checkSum = 0
    if (file):
        for i in range(len(compactDiskMap)):
            if (compactDiskMap[i] != '.'): 
                checkSum += i * compactDiskMap[i]
        return checkSum
    else:
        for i in range(len(compactDiskMap)):
            if (compactDiskMap[i] == '.'): break
            checkSum += i * compactDiskMap[i]
        return checkSum

inputFile = open(sys.argv[1]).read()
formatedInput = getFormatedInput(inputFile)
blockDiskMap = getBlockDiskMap(formatedInput)
fileDiskMap = getFileDiskMap(formatedInput.copy())
result = [getCheckSum(blockDiskMap), getCheckSum(fileDiskMap, True)]

print(f"Result for Advent Of Code 2024 -> Part 1: {result[0]}, Part 2: {result[1]}")