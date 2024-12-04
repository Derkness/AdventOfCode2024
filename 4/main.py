usedParts=[]

def part_1():
    global usedParts
    lines = []
    with open("input.txt", "r") as file:
        for line in file:
            lines.append([x for x in line.strip()])
    count=0
    for x, line in enumerate(lines):
        for y, value in enumerate(line):
            perIndex = 0
            if (value == 'X'):
                for changeX in [-1, 0, 1]:
                    for changeY in [-1, 0, 1]:
                        if changeX == 0 and changeY == 0:
                            continue
                        count+=look_along(lines, x, y, changeX, changeY)
                        perIndex+=look_along(lines, x, y, changeX, changeY)
            # print(x, y, perIndex)
                        
    # for x, line in enumerate(lines):
    #     for y, value in enumerate(line):
    #         if any(used[0] == x and used[1] == y for used in usedParts):
    #             print(value, end="")
    #         else:
    #             print('.', end="")
    #     print("")
    return count
                
def look_along(lines, x, y, changeX, changeY):
    global usedParts
    if (x+(3*changeX) < 0 or y+(3*changeY) < 0):
        return 0
    if (x+(3*changeX) >= len(lines) or y+(3*changeY) >= len(lines[0])):
        return 0
    if (lines[x+(1*changeX)][y+(1*changeY)] != 'M'):
        return 0
    if (lines[x+(2*changeX)][y+(2*changeY)] != 'A'):
        return 0
    if (lines[x+(3*changeX)][y+(3*changeY)] != 'S'):
        return 0
    usedParts.append([x, y])
    usedParts.append([x+(1*changeX), y+(1*changeY)])
    usedParts.append([x+(2*changeX), y+(2*changeY)])
    usedParts.append([x+(3*changeX), y+(3*changeY)])
    return 1
             
if __name__ == "__main__":
    totalValue = 0
    # part_1()
    print(part_1())

# 2441 TOO HIGH
# 2427 