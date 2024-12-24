from collections import deque


def part_1():
    lines = []
    with open("input.txt", "r") as file:
        for line in file:
            lines.append(int(line.strip()))
    total = 0
    for line in lines:
        val = line
        for _ in range(2000):
            val = cycle(val)
        total += val
    return total

def cycle(val):
    newVal = mix(val, val*64)
    newVal = prune(newVal)
    newVal = mix(newVal, int(newVal/32))
    newVal = prune(newVal)
    newVal = mix(newVal, newVal*2048)
    newVal = prune(newVal)
    return newVal

def mix(old, new):
    return old ^ new

def prune(old):
    return old % 16777216

def part_2():
    lines = []
    with open("input.txt", "r") as file:
        for line in file:
            lines.append(int(line.strip()))
    deltas: dict[int, dict[tuple[int,int,int,int], int]] = {}
    for lindex, line in enumerate(lines):
        val = line
        history = deque(maxlen=4)
        history.append(val%10)
        for _ in range(2000):
            newVal = cycle(val)
            history.append(newVal%10-val%10)
            thingo = deltas.get(lindex, {})
            thingo[tuple(history)] = newVal%10
            deltas[lindex] = thingo
            val = newVal
    
    # Flatten this into a dictionary that is basically --- tuple: bananas from all monkeys for that tuple
    totals = {}
    for delta in deltas.values():
        for value in delta.items():
            totals[value[0]] = totals.get(value[0], 0) + value[1]
    totals = dict(sorted(totals.items(), key=lambda item: item[1]))
    return [x for x in totals.items()][-1]
                
if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    print("part 2:", part_2())
