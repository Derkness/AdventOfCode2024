import math
import random
from enum import Enum


def part_1():
    lines = []
    with open("input.txt", "r") as file:
        for line in file:
            lines.append([x for x in line.strip()])
    zones = []
    for xIndex, line in enumerate(lines):
        for yIndex, value in enumerate(line):
            if considered(zones, (xIndex, yIndex)):
                continue
            zones.append(build_zone(xIndex, yIndex, value, lines))
    total = 0
    for zone in zones:
        perimeter = 0
        for plot in zone:
            potentialNeighbours = []
            potentialNeighbours.append((plot[0]-1,plot[1]))
            potentialNeighbours.append((plot[0]+1,plot[1]))
            potentialNeighbours.append((plot[0],plot[1]-1))
            potentialNeighbours.append((plot[0],plot[1]+1))
            for potentialNeighbour in potentialNeighbours:
                if potentialNeighbour not in zone:
                    perimeter += 1
        total += perimeter * len(zone)
    return total

class Direction(Enum):
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3,
    
    def __repr__(self):
        if (self.value[0] == 0):
            return "NORTH"
        if (self.value[0] == 1):
            return "EAST"
        if (self.value[0] == 2):
            return "SOUTH"
        if (self.value[0] == 3):
            return "WEST"

def part_2():
    lines = []
    with open("input.txt", "r") as file:
        for line in file:
            lines.append([x for x in line.strip()])
            
    # Build zones
    zones: list[set[tuple[int, int]]] = []
    for xIndex, line in enumerate(lines):
        for yIndex, value in enumerate(line):
            if considered(zones, (xIndex, yIndex)):
                continue
            zones.append(build_zone(xIndex, yIndex, value, lines))
    
    totalSides = 0
    for zone in zones:
        bends = 0
        # Make outside of area. A ring around it
        outerArea: list[tuple[tuple[int,int], Direction]] = []
        for plot in zone:
            potentialNeighbours = []
            if (plot[0]-1,plot[1]) not in zone:
                outerArea.append(((plot[0],plot[1]), Direction.NORTH))
            if (plot[0]+1,plot[1]) not in zone:
                outerArea.append(((plot[0],plot[1]), Direction.SOUTH))
            if (plot[0],plot[1]-1) not in zone:
                outerArea.append(((plot[0],plot[1]), Direction.WEST))
            if (plot[0],plot[1]+1) not in zone:
                outerArea.append(((plot[0],plot[1]), Direction.EAST))
            for potentialNeighbour in potentialNeighbours:
                if plot in outerArea:
                    break
                if potentialNeighbour not in zone and plot:
                    outerArea.append(plot)
        # random.shuffle(outerArea) <--- Putting this in game me the right answer. I think that theres some edge case I was missing that only happened starting at certain indeces.
        currentWall = outerArea.pop()
        startedWall = currentWall[1]
        mostRecentWall = None
        # Traverse your way around, using a lot of logic to follow the path
        while len(outerArea) != 0:
            nextWall = None
            bestRanking = 10
            bestIndex = -1
            for potentialIndex, potentialNext in enumerate(outerArea):
                potentialRank = touching(currentWall, potentialNext)
                if potentialRank < bestRanking:
                    bestIndex = potentialIndex
                    bestRanking = potentialRank
            if bestRanking == 10:
                # couldn't find a good one
                nextWall = outerArea.pop()
                if (startedWall != mostRecentWall):
                    bends +=1
                startedWall = nextWall[1]
            else:
                nextWall = outerArea.pop(bestIndex)
            mostRecentWall = nextWall[1]
            if bestRanking != 10 and nextWall[1] != currentWall[1]:
                bends +=1
            currentWall = nextWall
        if (startedWall != mostRecentWall):
            bends +=1
        totalSides += bends * len(zone)
    return totalSides

# Priority for moving. Priorities turning on same spot, then go side to side, then go diagonal jump
def touching(f1: tuple[tuple[int, int], Direction], f2: tuple[tuple[int, int], Direction]) -> int:
    if f1[0] == f2[0]:
        # bc of enum value setup
        match f1[1]:
            case Direction.NORTH:
                if (f2[1] == Direction.SOUTH):
                    return 10
            case Direction.SOUTH:
                if (f2[1] == Direction.NORTH):
                    return 10
            case Direction.EAST:
                if (f2[1] == Direction.WEST):
                    return 10
            case Direction.WEST:
                if (f2[1] == Direction.EAST):
                    return 10
        return 0
    # vertical or horizontal, maintain side of grid
    if math.dist(f1[0], f2[0]) == 1:
        if f1[1] == f2[1]:
            return 1
    # diagonals!
    if (f1[0][0]-1, f1[0][1]-1) == f2[0]:
        if f1[1] == Direction.NORTH and f2[1] == Direction.EAST:
            return 2
        if f1[1] == Direction.WEST and f2[1] == Direction.SOUTH:
            return 2
    if (f1[0][0]+1, f1[0][1]+1) == f2[0]:
        if f1[1] == Direction.SOUTH and f2[1] == Direction.WEST:
            return 2
        if f1[1] == Direction.EAST and f2[1] == Direction.NORTH:
            return 2
    if (f1[0][0]-1, f1[0][1]+1) == f2[0]:
        if f1[1] == Direction.NORTH and f2[1] == Direction.WEST:
            return 2
        if f1[1] == Direction.EAST and f2[1] == Direction.SOUTH:
            return 2
    if (f1[0][0]+1, f1[0][1]-1) == f2[0]:
        if f1[1] == Direction.SOUTH and f2[1] == Direction.EAST:
            return 2
        if f1[1] == Direction.WEST and f2[1] == Direction.NORTH:
            return 2
    return 10
        
    
def considered(zones, point):
    for zone in zones:
        if point in zone:
            return True
    return False

def build_zone(xIndex: int, yIndex: int, value: str, lines: list) -> set:
    plots = [(xIndex, yIndex)]
    for plot in plots:
        neighbours = get_cardinal_neighbour_indexes(plot[0], plot[1], lines)
        neighbours = [x for x in neighbours if lines[x[0]][x[1]] == value and x not in plots]
        plots+= neighbours
    return set(plots)
    
def get_cardinal_neighbour_indexes(x: int, y:int, twod_array: list[list]) -> set:
    maxX = len(twod_array)
    maxY = len(twod_array[0])
    if not check_array_bounds(x, y, maxX, maxY):
        return set()
    options = set()
    options = options.union({(x-1, y)}) if check_array_bounds(x-1, y, maxX, maxY) else options
    options = options.union({(x+1, y)}) if check_array_bounds(x+1, y, maxX, maxY) else options
    options = options.union({(x, y-1)}) if check_array_bounds(x, y-1, maxX, maxY) else options
    options = options.union({(x, y+1)}) if check_array_bounds(x, y+1, maxX, maxY) else options
    return options
        
def check_array_bounds(x: int, y: int, maxX: int, maxY: int) -> bool:
    if x < 0 or y < 0:
        return False
    if x >= maxX or y >= maxY:
        return False
    return True
                
if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    print("part 2:", part_2())
    