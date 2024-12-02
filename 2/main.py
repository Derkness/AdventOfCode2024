def part_1():
    safeCount = 0
    with open("input.txt", "r") as file:
        for line in file:
            line = line.split()
            safeCount += checkSafe(line)
    return safeCount 

def checkSafe(line):
    differences = [int(line[x]) - int(line[x+1]) for x in range(len(line)-1)]
    allDescending = all(x > 0 for x in differences)
    allAscending = all(x < 0 for x in differences)
    if (not allDescending and not allAscending):
        return 0
    for difference in differences:
        if abs(difference) > 3 or abs(difference) == 0:
            return 0
    return 1

def part_2():
    safeCount = 0
    with open("input.txt", "r") as file:
        for line in file:
            line = line.split()
            safeCount += checkTolerantSafe(line)
    return safeCount 

def checkTolerantSafe(line):
    differences = [int(line[x]) - int(line[x+1]) for x in range(len(line)-1)]
    allDescending = all(x > 0 for x in differences)
    allAscending = all(x < 0 for x in differences)
    if (not allDescending and not allAscending):
        subWorks = 0
        for index, _ in enumerate(line):
            newLine = [line[innerIndex] for innerIndex,_ in enumerate(line) if innerIndex != index]
            subWorks += checkSafe(newLine)
        return 0 if subWorks == 0 else 1
    for difference in differences:
        if abs(difference) > 3 or abs(difference) == 0:
            subWorks = 0
            for index, _ in enumerate(line):
                newLine = [line[innerIndex] for innerIndex,_ in enumerate(line) if innerIndex != index]
                subWorks += checkSafe(newLine)
            return 0 if subWorks == 0 else 1
    return 1
            
if __name__ == "__main__":
    totalValue = 0
    print(part_2())
