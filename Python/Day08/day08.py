import sys

def getAntennas(formatedInput):
    antennas = dict()
    for i in range(len(formatedInput)):
        for j in range(len(formatedInput[i])):
            antenna = formatedInput[i][j]
            if (antenna != '.'):
                if (antenna in antennas.keys()):
                    antennas[antenna].append((i, j))
                else:
                    antennas[antenna] = [(i, j)]
    return antennas

def validAN(an):
    return (0 <= an[0] < len(formatedInput) and 0 <= an[1] < len(formatedInput[0]))

def getFirstAN(antennas):
    antinodes = set()
    for positions in antennas.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                pos1, pos2 = positions[i], positions[j]
                distY, distX = pos2[0] - pos1[0], pos2[1] - pos1[1]
                an1 = (pos2[0] + distY, pos2[1] + distX)
                an2 = (pos1[0] - distY, pos1[1] - distX)
                if validAN(an1) and an1 not in antinodes:
                    antinodes.add(an1)
                if validAN(an2) and an2 not in antinodes:
                    antinodes.add(an2)
    return len(antinodes)

def getTotalAN(antennas):
    antinodes = set()
    for positions in antennas.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                pos1, pos2 = positions[i], positions[j]
                distY, distX = pos2[0] - pos1[0], pos2[1] - pos1[1]
                mult = 0
                while True:
                    an1 = (pos2[0] + distY * mult, pos2[1] + distX * mult)
                    an2 = (pos1[0] - distY * mult, pos1[1] - distX * mult)
                    if validAN(an1) and an1 not in antinodes:
                        antinodes.add(an1)
                    if validAN(an2) and an2 not in antinodes:
                        antinodes.add(an2)
                    mult += 1
                    if not validAN(an1) and not validAN(an2): break
    return len(antinodes)

formatedInput = [[ch for ch in line] for line in open(sys.argv[1]).read().split("\n")]
antennas = getAntennas(formatedInput)
result = [getFirstAN(antennas), getTotalAN(antennas)]

print(f"Result for Advent Of Code 2024 -> Part 1: {result[0]}, Part 2: {result[1]}")