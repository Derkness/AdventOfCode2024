import heapq as hq

def part_1():
    input = []
    start = None
    end = None
    with open("input.txt", "r") as file:
        for line in file:
            line = [x for x in line.strip()]
            if 'S' in line:
                start = (len(input), line.index('S'))
                line[line.index('S')] = '.'
            if 'E' in line:
                end = (len(input), line.index('E'))
                line[line.index('E')] = '.'
            input.append(line)
    nodes: dict[tuple[int,int], list[tuple[int,int]]] = {}
    for x, line in enumerate(input):
        for y, val in enumerate(line):
            if val == '.':
                neighbours = get_neighbours(input, x, y)
                nodes[(x,y)] = neighbours
    distances = dijkstra(nodes, start)
    best_distance = distances[end]
    better_than_100 = 0
    for topIndex, line in enumerate(input):
        print(str(int(100*(topIndex/len(input)))) + "%")
        for index, adjust in enumerate(line):
            if (adjust == '.'):
                continue
            input[topIndex][index] = '.'
            nodes: dict[tuple[int,int], list[tuple[int,int]]] = {}
            for x, line in enumerate(input):
                for y, val in enumerate(line):
                    if val == '.':
                        neighbours = get_neighbours(input, x, y)
                        nodes[(x,y)] = neighbours
            distances = dijkstra(nodes, start)
            if best_distance - distances[end] >= 100:
                better_than_100 += 1
            input[topIndex][index] = '#'
    return better_than_100
            
def get_neighbours(input, x, y):
    options = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [option for option in options if validate_neighbours(input, option[0], option[1])]

def validate_neighbours(input, x, y):
    if x < 0 or y < 0:
        return False
    if x >= len(input) or y >= len(input[0]):
        return False
    if (input[x][y] == '#'):
        return False
    return True

def dijkstra(graph, start):
    distances = {}
    heap = [(0, start)]

    while heap:
        dist, node = hq.heappop(heap)
        if node in distances:
            continue  # Already encountered before
        # We know that this is the first time we encounter node.
        #   As we pull nodes in order of increasing distance, this 
        #   must be the node's shortest distance from the start node.
        distances[node] = dist
        for neighbor in graph[node]:
            if neighbor not in distances:
                hq.heappush(heap, (dist + 1, neighbor))

    return distances        

if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    
    # 1366 too low