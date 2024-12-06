from copy import deepcopy
from enum import Enum


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class Guard:
    def __init__(self, x: int, y: int, dir: Direction):
        self.x = x
        self.y = y
        self.dir = dir
        
    def check_bounds(self, map):
        xBound = len(map)
        yBound = len(map[0])
        
        nextX = None
        nextY = None
        
        match self.dir:
            case Direction.NORTH:
                nextX = self.x-1
                nextY = self.y
            case Direction.EAST:
                nextX = self.x
                nextY = self.y+1
            case Direction.SOUTH:
                nextX = self.x+1
                nextY = self.y
            case Direction.WEST:
                nextX = self.x
                nextY = self.y-1
        
        if nextX >= xBound or nextY >= yBound:
            return False
        if nextX < 0 or nextY < 0:
            return False
        return True
        
    def move(self, map):
        match self.dir:
            case Direction.NORTH:
                if map[self.x-1][self.y] == '#':
                    self.dir = Direction.EAST
                else:
                    self.x = self.x-1
                return (self.x, self.y)
            
            case Direction.EAST:
                if map[self.x][self.y+1] == '#':
                    self.dir = Direction.SOUTH
                else:
                    self.y = self.y+1
                return (self.x, self.y)
                
            case Direction.SOUTH:
                if map[self.x+1][self.y] == '#':
                    self.dir = Direction.WEST
                else:
                    self.x = self.x+1
                return (self.x, self.y)
                
            case Direction.WEST:
                if map[self.x][self.y-1] == '#':
                    self.dir = Direction.NORTH
                else:
                    self.y = self.y-1
                return (self.x, self.y)

    def move_2(self, map):
        match self.dir:
            case Direction.NORTH:
                if map[self.x-1][self.y] == '#':
                    self.dir = Direction.EAST
                else:
                    self.x = self.x-1
                return (self.x, self.y, self.dir)
            
            case Direction.EAST:
                if map[self.x][self.y+1] == '#':
                    self.dir = Direction.SOUTH
                else:
                    self.y = self.y+1
                return (self.x, self.y, self.dir)
                
            case Direction.SOUTH:
                if map[self.x+1][self.y] == '#':
                    self.dir = Direction.WEST
                else:
                    self.x = self.x+1
                return (self.x, self.y, self.dir)
                
            case Direction.WEST:
                if map[self.x][self.y-1] == '#':
                    self.dir = Direction.NORTH
                else:
                    self.y = self.y-1
                return (self.x, self.y, self.dir)

def part_1():
    lines = []
    guard = None
    with open("input.txt", "r") as file:
        for xIndex, line in enumerate(file):
            if guard is None:
                for yIndex, value in enumerate(line):
                    if value == "^":
                        guard = Guard(xIndex, yIndex, Direction.NORTH)
            lines.append([x for x in line.strip()])
    visited = set()
    visited.add((guard.x, guard.y))
    
    while(guard.check_bounds(lines)):
        visited.add(guard.move(lines))

    return visited, len(visited)

def part_2():
    lines = []
    guard = None
    with open("input.txt", "r") as file:
        for xIndex, line in enumerate(file):
            if guard is None:
                for yIndex, value in enumerate(line):
                    if value == "^":
                        guard = Guard(xIndex, yIndex, Direction.NORTH)
            lines.append([x for x in line.strip()])
    
    pathTaken, _ = part_1()
    
    loopsFound = 0
    for step in pathTaken:
        if lines[step[0]][step[1]] == '#':
            continue
        if value == '^':
            continue
        lines[step[0]][step[1]] = '#'
        loopsFound += 1 if check_loop(deepcopy(guard), lines) else 0
        lines[step[0]][step[1]] = '.'
            
    return loopsFound

def check_loop(guard: Guard, lines: list[list[str]]):
    visited = set()
    visited.add((guard.x, guard.y, guard.dir))
    while(guard.check_bounds(lines)):
        nextPos = guard.move_2(lines)
        if nextPos in visited:
            return True
        visited.add(nextPos)
    return False
    

if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1()[1])
    print("part 2:", part_2())