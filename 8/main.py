from fractions import Fraction


def part_1():
    lines = []
    antennasByGroup: dict[str,list[tuple[int,int]]] = {}
    antennodes = set()
    with open("input.txt", "r") as file:
        for xIndex, line in enumerate(file):
            line = line.strip()
            lines.append(line)
            for yIndex, val in enumerate(line):
                if val != '.':
                   antennasByGroup[val] =antennasByGroup.get(val, []) + [(xIndex, yIndex)]
    for antennaType, antennaGroup in antennasByGroup.items():
        for i in range(len(antennaGroup)):
            for j in range(len(antennaGroup)):
                if (i == j):
                    continue
                ant1 = antennaGroup[i]
                ant2 = antennaGroup[j]
                gradientX = ant2[0]-ant1[0]
                gradientY = ant2[1]-ant1[1]
                antennodes.add((ant2[0] + gradientX, ant2[1] + gradientY))
                antennodes.add((ant1[0] - gradientX, ant1[1] - gradientY))
    
    maxX = len(lines)
    maxY = len(lines[0])
    
    return len({x for x in antennodes if (x[0] >= 0 and x[1] >= 0 and x[0] < maxX and x[1] < maxY)})

def part_2():
    lines = []
    antennasByGroup: dict[str,list[tuple[int,int]]] = {}
    antennodes = set()
    with open("input.txt", "r") as file:
        for xIndex, line in enumerate(file):
            line = line.strip()
            lines.append(line)
            for yIndex, val in enumerate(line):
                if val != '.':
                   antennasByGroup[val] = antennasByGroup.get(val, []) + [(xIndex, yIndex)]
    for antennaType, antennaGroup in antennasByGroup.items():
        for i in range(len(antennaGroup)):
            for j in range(len(antennaGroup)):
                if (i == j):
                    continue
                ant1 = antennaGroup[i]
                ant2 = antennaGroup[j]
                gradientX = ant2[0]-ant1[0]
                gradientY = ant2[1]-ant1[1]
                
                # This looks a bit weird but its just a cheap way to get the simplest form, so theres no "gaps" just bc the gradient is 2x or whatever it needs to be.
                FractionForm = Fraction(gradientX, gradientY)
                gradientX = FractionForm.numerator
                gradientY = FractionForm.denominator
                
                for k in range(len(lines)):
                    antennodes.add((ant2[0] + (gradientX*k), ant2[1] + (gradientY*k)))
                    antennodes.add((ant1[0] - (gradientX*k), ant1[1] - (gradientY*k)))
    
    maxX = len(lines)
    maxY = len(lines[0])
    
    return len({x for x in antennodes if (x[0] >= 0 and x[1] >= 0 and x[0] < maxX and x[1] < maxY)})
    
if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    print("part 2:", part_2())