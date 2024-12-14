from math import floor


class Robot:
    def __init__(self, xPos: int, yPos: int, xVel: int, yVel: int):
        self.xPos = xPos
        self.yPos = yPos
        self.xVel = xVel
        self.yVel = yVel
        
    def __repr__(self):
        return str(self.xPos )+ ', ' + str(self.yPos )+ ' - ' + str(self.xVel )+ ', ' + str(self.yVel)
    
    def move(self, maxX, maxY):
        newX = self.xPos + self.xVel
        if (newX < 0):
            newX += maxX
        newY = self.yPos + self.yVel
        if (newY < 0):
            newY += maxY
        self.xPos = newX % (maxX)
        self.yPos = newY % (maxY)
        
    def get_quadrant(self, maxX, maxY):
        # print(str(self.xPos) + ',' + str(self.yPos))
        if (self.xPos == floor(maxX/2)):
            return 0
        if (self.yPos == floor(maxY/2)):
            return 0
        
        if self.xPos <= maxX/2:
            if self.yPos <= maxY/2:
                return 1
            return 2
        if self.yPos<= maxY/2:
            return 3
        return 4
    # 1 2
    # 3 4

def part_1():
    robots: list[Robot] = []
    maxX = 101
    maxY = 103
    with open("input.txt", "r") as file:
        for line in file:
            line = [x[2:].split(',') for x in line.strip().split(" ")]
            robots.append(Robot(int(line[0][0]), int(line[0][1]), int(line[1][0]), int(line[1][1])))
    for i in range(5041):
        for robot in robots:
            robot.move(maxX, maxY)
    robotsInQuadrants = []
    for robot in robots:
        quad = robot.get_quadrant(maxX, maxY)
        robotsInQuadrants.append(quad)
    return robotsInQuadrants.count(1) * robotsInQuadrants.count(2) * robotsInQuadrants.count(3) * robotsInQuadrants.count(4)

def part_2():
    robots: list[Robot] = []
    maxX = 101
    maxY = 103
    with open("input.txt", "r") as file:
        for line in file:
            line = [x[2:].split(',') for x in line.strip().split(" ")]
            robots.append(Robot(int(line[0][0]), int(line[0][1]), int(line[1][0]), int(line[1][1])))
    for attemptNum in range(10000):
        for robot in robots:
            robot.move(maxX, maxY)
        allCords = [(x.xPos, x.yPos) for x in robots]
        # if its a pattern then probably no 2 on the same spot?
        if len(set(allCords)) == len(allCords):
            return attemptNum + 1
    return None

if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    print("part 2:", part_2())