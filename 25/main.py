

def part_1():
    locks: list[list[int]] = []
    keys: list[list[int]] = []
    with open("input.txt", "r") as file:
        working = []
        for line in file:
            if (len(line.strip()) == 0):
                if '.' in working[0]:
                    transposed = list(map(list, zip(*working)))
                    keys.append([x.count('#') - 1 for x in transposed])
                if '#' in working[0]:
                    transposed = list(map(list, zip(*working)))
                    locks.append([x.count('#') - 1 for x in transposed])
                working.clear()
                continue
            working.append([x for x in line.strip()])
        if '.' in working[0]:
            transposed = list(map(list, zip(*working)))
            keys.append([x.count('#') - 1 for x in transposed])
        if '#' in working[0]:
            transposed = list(map(list, zip(*working)))
            locks.append([x.count('#') - 1 for x in transposed])
    success = 0
    for lock in locks:
        for key in keys:
            slot = [sum(x) for x in zip(lock, key)]
            if any(x > 5 for x in slot):
                continue
            success += 1
    return success
if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    # print("part 2:", part_2())
