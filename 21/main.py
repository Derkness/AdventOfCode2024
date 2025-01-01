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
            vertical = get_vertical(cur, goal)
            horizontal = get_horizontal(cur, goal)
            if cur[0] == 3 and goal[1] == 0:
                commands.append(vertical)
                commands.append(horizontal)
                cur = goal
            elif cur[1] == 0 and goal[0] == 3:
                commands.append(horizontal)
                commands.append(vertical)
                cur = goal
            elif cur[1] < goal[1]:
                commands.append(vertical)
                commands.append(horizontal)
                cur = goal
            elif cur[1] > goal[1]:
                commands.append(horizontal)
                commands.append(vertical)
                cur = goal
            else:
                commands.append(vertical)
                cur = goal
            commands.append("A")
        commands = "".join(commands)
        for _ in range(2):
            newCommands = []
            cur = (0, 2)
            for char in commands:
                goal = find_coords(char, PAD_TWO)
                vertical = get_vertical(cur, goal)
                horizontal = get_horizontal(cur, goal)
                if cur[0] == 1 and cur[1] == 0:
                    newCommands.append(horizontal)
                    newCommands.append(vertical)
                    cur = goal
                elif goal[0] == 1 and goal[1] == 0:
                    newCommands.append(vertical)
                    newCommands.append(horizontal)
                    cur = goal
                elif cur[1] < goal[1]:
                    newCommands.append(vertical)
                    newCommands.append(horizontal)
                    cur = goal
                elif cur[1] > goal[1]:
                    newCommands.append(horizontal)
                    newCommands.append(vertical)
                    cur = goal
                else:
                    newCommands.append(vertical)
                    cur = goal
                newCommands.append("A")
            commands = "".join(newCommands)
        print(len(commands))
        total += len(commands) * int(line[:-1])
    return total

def get_horizontal(start, end):
    startVal = start[1]
    endVal = end[1]
    if startVal < endVal:
        return ">" * (endVal-startVal)
    if startVal > endVal:
        return "<" * (startVal-endVal)
    return ""

def get_vertical(start, end):
    startVal = start[0]
    endVal = end[0]
    if startVal < endVal:
        return "v" * (endVal-startVal)
    if startVal > endVal:
        return "^" * (startVal-endVal)
    return ""

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

# Lets get some rules tommy boy
# We do want to always group the directions as one, but it's not as simple as down before left, or right before up, or whatever
# Depends on the PREVIOUS one (at the same level)
# for the numpad one, we can't ever hit bottom left corner, so if going from bot to left, has to be up first then left. Going from left to bottom is opposite
# for direction one, blank is top left corner, so from left corner is right first, and to left corner is down first.
#   I think, becuase it's just two tall, we can go like, if current is '<', then do all rights then up (if needed). If goal is not '>' then do all up/down, then sides
# ------------- ABOVE REFERENCES AVOIDING THE GAP -----------

# ------------- EFFICIENCY ----------------------------------
# Now, from some of the first attempts it very much depends what order I do things in. It's a given I only need one type of v/^, or one type of >/<. But it's hard to predict the order, sometimes it only matters 2 or 3 steps down. I also bet that pt2 is gonna be like "WOW you find out you need 100 robots" so I can't let anything like that creep in i think
# Because we always start on the top right, i think if we are moving left, we want left first then either the up or down. Otherwise, updown first

# Pt.2 SUCCESS!!!
#I was right about part 2! :D so happy about that! 
#Maybe i can do the equivalent of DFS? and do some sneaky cachin