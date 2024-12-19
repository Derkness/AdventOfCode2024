from functools import cache

NOT_FOUND = 1_000_000_000_000

def part_1():
    needs: list[str] = []
    options: set[str] = []
    with open("input.txt", "r") as file:
        gettingOptions = True
        for line in file:
            if (len(line.strip()) == 0):
                gettingOptions = False
                continue
            if gettingOptions:
                options = frozenset({x for x in line.strip().split(", ")})
                continue
            needs.append(line.strip())
    
    total = 0
    for need in needs:
        total += check_viable(need, options)
    return total

def part_2():
    needs: list[str] = []
    options: set[str] = []
    with open("input.txt", "r") as file:
        gettingOptions = True
        for line in file:
            if (len(line.strip()) == 0):
                gettingOptions = False
                continue
            if gettingOptions:
                options = frozenset({x for x in line.strip().split(", ")})
                continue
            needs.append(line.strip())
    
    total = 0
    for need in needs:
        total += how_many_ways(need, options)
    return total
    
def check_viable(need: str, options: set[str]) -> int:
    needed = how_many_needed(need, options, 0)
    if needed == NOT_FOUND:
        print("Can't do")
        return 0
    print("Possible. Cheapest uses", needed, "towels.")
    return 1

@cache
def how_many_needed(need: str, options: set[str], costSoFar: int) -> int:
    if len(need) == 0:
        return costSoFar
    viableOptions = [x for x in options if fits(need, x)]
    costs = []
    for option in viableOptions:
        costs.append(how_many_needed(need[len(option):], options, costSoFar + 1))
    return min(costs) if len(costs) != 0 else NOT_FOUND

@cache
def how_many_ways(need: str, options: set[str]) -> int:
    if len(need) == 0:
        return 1
    viableOptions = [x for x in options if fits(need, x)]
    ways = 0
    for option in viableOptions:
        ways += how_many_ways(need[len(option):], options)
    return ways

def fits(need: str, option: str) -> bool:
    if len(option) > len(need):
        return False
    for index, char in enumerate(option):
        if char != need[index]:
            return False
    return True

if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    print("part 2:", part_2())
    