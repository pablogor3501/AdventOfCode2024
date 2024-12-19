import sys
import numpy as np

SPACE_WIDTH = 101
SPACE_HEIGHT = 103

class Robot:
    def __init__(self, pos, vel):
        self.pos = list(map(int, pos))
        self.vel = list(map(int, vel))
    
    def __str__(self):
        return f"Position {self.pos}, velocity {self.vel}"
    
    def calculateRealPos(self):
        self.pos[0] = self.pos[0] % SPACE_WIDTH
        self.pos[1] = self.pos[1] % SPACE_HEIGHT

def getFormatedInput(inputFile):
    robots = []
    for robotData in inputFile.split("\n"):
        data = robotData.split(" ")
        robots.append(Robot(data[0].lstrip("p=").split(','), data[1].lstrip("v=").split(',')))
    return robots

def getQuadrantTotal(robots):
    quadrants = [0, 0, 0, 0]
    for robot in robots:
        if (robot.pos[0] < (SPACE_WIDTH - 1) / 2 and robot.pos[1] < (SPACE_HEIGHT - 1) / 2): quadrants[0] += 1
        elif (robot.pos[0] > (SPACE_WIDTH - 1) / 2 and robot.pos[1] < (SPACE_HEIGHT - 1) / 2): quadrants[1] += 1
        elif (robot.pos[0] <(SPACE_WIDTH - 1) / 2 and robot.pos[1] > (SPACE_HEIGHT - 1) / 2): quadrants[2] += 1
        elif (robot.pos[0] > (SPACE_WIDTH - 1) / 2 and robot.pos[1] > (SPACE_HEIGHT - 1) / 2): quadrants[3] += 1
    return np.prod(np.array(quadrants))

def PrettyPrint(robots):
    space = ''
    robotPositions = {tuple(robot.pos) for robot in robots}
    for i in range(SPACE_WIDTH):
        for j in range(SPACE_HEIGHT):
            if ((i, j) in robotPositions): space += 'O'
            else: space += ' '
        space += "\n"
    return space


inputFile = open(sys.argv[1]).read()
robots = getFormatedInput(inputFile)
total, seconds = 0, 0
while True:
    for robot in robots:
        robot.pos = [(robot.pos[i] + robot.vel[i]) for i in range(len(robot.pos))]
        robot.calculateRealPos()
    space = PrettyPrint(robots)
    seconds += 1
    if (seconds == 100): total = getQuadrantTotal(robots)
    if ('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO' in space): break

result = [total, seconds]
print(f"Result for Advent Of Code 2024 -> Part 1: {result[0]}, Part 2: {result[1]}")