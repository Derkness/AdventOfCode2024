
cache = {}

def expand_stones(stone: int, currentIteration: int, totalIterations: int) -> int:
    global cache
    if cache.get((stone, currentIteration), -1) != -1:
        return cache.get((stone, currentIteration))
    if (currentIteration > totalIterations):
        cache[(stone, currentIteration)] = 1
        return 1
    if stone == 0:
        val = expand_stones(1, currentIteration+1, totalIterations)
        cache[(stone, currentIteration)] = val
        return val
    if len(str(stone)) %2 == 0:
        firsthalf, secondhalf = str(stone)[:len(str(stone))//2], str(stone)[len(str(stone))//2:]
        val = expand_stones(int(firsthalf), currentIteration+1, totalIterations) + expand_stones(int(secondhalf), currentIteration+1, totalIterations)
        cache[(stone, currentIteration)] = val
        return val
    return expand_stones(stone*2024, currentIteration+1, totalIterations)

def thingo():
    line = []
    with open("input.txt", "r") as file:
        for line in file:
            line = [int(x) for x in line.split()]
    all_stones = 0
    for stone in line:
        all_stones += expand_stones(stone, 1, 75)
    return all_stones
    

if __name__ == "__main__":
    print(thingo())
    