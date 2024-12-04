def part_1():
    lines = []
    with open("input.txt", "r") as file:
        for line in file:
            lines.append([x for x in line.strip()])
    count=0
    for x, line in enumerate(lines):
        for y, value in enumerate(line):
            if (value == 'X'):
                for changeX in [-1, 0, 1]:
                    for changeY in [-1, 0, 1]:
                        if changeX == 0 and changeY == 0:
                            continue
                        count+=look_along_pt_1(lines, x, y, changeX, changeY)
    return count
                
def look_along_pt_1(lines, x, y, changeX, changeY):
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
    return 1

def part_2():
    lines = []
    with open("input.txt", "r") as file:
        for line in file:
            lines.append([x for x in line.strip()])
    count=0
    for x, line in enumerate(lines):
        for y, value in enumerate(line):
            if (value == 'A'):
                count+=look_along_pt_2(lines, x, y)
    return count
                
def look_along_pt_2(lines, x, y):
    
    # Check bounds
    if (x-1 < 0 or y-1 < 0):
        return 0
    if (x+1 >= len(lines) or y+1 >= len(lines[0])):
        return 0
    
    # Disqualify when an 'X' or an 'A' is in the cross
    if (lines[x-1][y-1] == 'X' or lines[x+1][y-1] == 'X' or lines[x+1][y+1] == 'X' or lines[x-1][y+1] == 'X'):
        return 0
    if (lines[x-1][y-1] == 'A' or lines[x+1][y-1] == 'A' or lines[x+1][y+1] == 'A' or lines[x-1][y+1] == 'A'):
        return 0
    
    # Check the MAS cross in a hideous but easily written way
    if (lines[x-1][y-1] == "M"):
        if (lines[x+1][y+1] != "S"):
            return 0
    if (lines[x-1][y-1] == "S"):
        if (lines[x+1][y+1] != "M"):
            return 0
    
    if (lines[x+1][y-1] == "M"):
        if (lines[x-1][y+1] != "S"):
            return 0
    if (lines[x+1][y-1] == "S"):
        if (lines[x-1][y+1] != "M"):
            return 0
    
    if (lines[x+1][y+1] == "M"):
        if (lines[x-1][y-1] != "S"):
            return 0
    if (lines[x+1][y+1] == "S"):
        if (lines[x-1][y-1] != "M"):
            return 0
    
    if (lines[x-1][y+1] == "M"):
        if (lines[x+1][y-1] != "S"):
            return 0
    if (lines[x-1][y+1] == "S"):
        if (lines[x+1][y-1] != "M"):
            return 0
        
    # is valid!
    return 1

if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    print("part 2:", part_2())