def find_trailhead_score(x: int, y: int, prevVal: int, lines) -> set[tuple[int, int]]:
    if x < 0 or y < 0:
        return set()
    if x >= len(lines) or y >= len(lines[0]):
        return set()
    value = lines[x][y]
    if value != prevVal + 1:
        return set()
    if (value == 9):
        return set([(x, y)])
    return find_trailhead_score(x-1, y, value, lines).union(find_trailhead_score(x+1, y, value, lines), find_trailhead_score(x, y-1, value, lines), find_trailhead_score(x, y+1, value, lines))

def find_rating(x: int, y: int, prevVal: int, lines) -> int:
    if x < 0 or y < 0:
        return 0
    if x >= len(lines) or y >= len(lines[0]):
        return 0
    value = lines[x][y]
    if value != prevVal + 1:
        return 0
    if (value == 9):
        return 1
    return find_rating(x-1, y, value, lines) + find_rating(x+1, y, value, lines) + find_rating(x, y-1, value, lines) + find_rating(x, y+1, value, lines)

def part_1():
    lines = []
    with open("input.txt", "r") as file:
        for line in file:
            lines.append([-1 if x == '.' else int(x) for x in line.strip()])
    total = 0
    for xIndex, line in enumerate(lines):
        for yIndex, value in enumerate(line):
            if (value == 0):
                total += len(find_trailhead_score(xIndex, yIndex, -1, lines))
    return total

def part_2():
    lines = []
    with open("input.txt", "r") as file:
        for line in file:
            lines.append([-1 if x == '.' else int(x) for x in line.strip()])
    total = 0
    for xIndex, line in enumerate(lines):
        for yIndex, value in enumerate(line):
            if (value == 0):
                total += find_rating(xIndex, yIndex, -1, lines)
    return total
    

if __name__ == "__main__":
    print("part 1:", part_1())
    print("part 2:", part_2())
    