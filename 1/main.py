def part_1():
    first=[]
    second=[]
    with open("input.txt", "r") as file:
        for line in file:
            line = line.split(" ")
            first.append(int(line[0]))
            second.append(int(line[1]))
    first.sort()
    second.sort()
    
    total = 0
    for one, two in zip(first, second):
        total += abs(one - two)

    return total

def part_2():
    first=[]
    second=[]
    with open("input.txt", "r") as file:
        for line in file:
            line = line.split(" ")
            first.append(int(line[0]))
            second.append(int(line[1]))
    
    total = 0
    for value in first:
        total += value * second.count(value)

    return total

if __name__ == "__main__":
    totalValue = 0
    print(part_2())