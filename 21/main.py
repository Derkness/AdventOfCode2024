import math


PAD_ONE = [
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    ["-1","0","A"],
]

PAD_TWO = [
    ["","^","A"],
    ["<","v",">"]
]

def part_1():
    lines = []
    with open("input.txt", "r") as file:
        for line in file:
            lines.append(line.strip())
    total = 0
    for line in lines:
        cur = (3, 2)
        commands = []
        for char in line:
            goal = find_coords(char, PAD_ONE)
            while cur != goal:
                if goal[1] > cur[1]:
                    cur = (cur[0], cur[1] + 1)
                    commands.append(">")
                    continue
                if goal[0] < cur[0]:
                    cur = (cur[0] - 1, cur[1])
                    commands.append("^")
                    continue
                if goal[1] < cur[1]:
                    cur = (cur[0], cur[1] - 1)
                    commands.append("<")
                    continue
                if goal[0] > cur[0]:
                    cur = (cur[0] + 1, cur[1])
                    commands.append("v")
                    continue
            commands.append("A")
        # [print(x, end="") for x in commands]
        # print("")
        for _ in range(2):
            newCommands = []
            cur = (0, 2)
            for char in commands:
                goal = find_coords(char, PAD_TWO)
                while cur != goal:
                    if cur == (0,0):
                        print('ss')
                    if goal[1] < cur[1]:
                        cur = (cur[0], cur[1] - 1)
                        newCommands.append("<")
                        continue
                    if goal[0] > cur[0]:
                        cur = (cur[0] + 1, cur[1])
                        newCommands.append("v")
                        continue
                    if goal[0] < cur[0]:
                        cur = (cur[0] - 1, cur[1])
                        newCommands.append("^")
                        continue
                    if goal[1] > cur[1]:
                        cur = (cur[0], cur[1] + 1)
                        newCommands.append(">")
                        continue
                newCommands.append("A")
            commands = newCommands
            # [print(x, end="") for x in commands]
            # print("")
        [print(x, end="") for x in commands]
        print("")
        total += len(commands) * int(line[:-1])
    return total

def best_button(prevCord, nextCord, cur):
    options = []
    if (prevCord[0] < nextCord[0]):
        options.append("v")
    else:
        options.append("^")
        
    if (prevCord[1] < nextCord[1]):
        options.append(">")
    else:
        options.append("<")

    optionCords = [find_coords(x, PAD_TWO) for x in options]
    distances = [distance_between_points(cur, x) for x in optionCords]
    if (distances[0] < distances[1]):
        return options[0]
    return options[1]

def distance_between_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    

def find_coords(char, map):
    for xIndex, line in enumerate(map):
        for yIndex, val in enumerate(line):
            if val == char:
                return (xIndex, yIndex)
    
if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
