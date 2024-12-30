import heapq as hq
import random

NOT_FOUND = 1_000_000_000_000

class Node:
    def __init__(self, x: int, y: int, wall: bool, shortest: int):
        self.x = x
        self.y = y
        self.wall = wall
        self.visited: bool = False
        self.fromNode: Node | None = None
        self.shortest = shortest
        self.id = random.randint(0,10000000000)
    
    def __repr__(self):
        visited = "Visited" if self.visited else "Unvisited"
        wall = "Wall" if self.wall else "Non-wall"
        return "(" + str(self.x) + "," + str(self.y) + ") - " + visited + " - " + wall
    
    def __eq__(self, value):
        if value is None:
            return False
        return self.x == value.x and self.y == value.y

    def __lt__(self, other):
        if (self.wall):
            return False
        if (self.visited):
            return False
        return self.shortest < other.shortest
    
    def __hash__(self):
        return self.id

class NodeMap:
    def __init__(self):
        self.nodes: list[Node] = []
        
    def add_to_node(self, node: Node):
        self.nodes += [node]
        
    def heapify(self):
        hq.heapify(self.nodes)
    
    def find_node(self, x, y):
        for node in self.nodes:
            if node.visited or node.wall:
                continue
            if node.x == x and node.y == y:
                return node
        return None
    
    def freely_find_node(self, x, y):
        for node in self.nodes:
            if node.x == x and node.y == y:
                return node
        return None
    
    def remove_node(self, x, y):
        for index, node in enumerate(self.nodes):
            if node.x == x and node.y == y:
                return self.nodes.pop(index)
    
    def unvisit_all(self, start: Node):
        for node in self.nodes:
            node.visited = False
            node.shortest = NOT_FOUND
        start.shortest = 0
            
    def get_closest_node_to_start(self) -> Node | None:
        closestNode = hq.heappop(self.nodes)
        if closestNode.visited or closestNode.wall:
            return None
        return closestNode

    def find_nodes_indexes(self, cur: Node) -> list[int]:
        neighbours = [(cur.x-1, cur.y), (cur.x+1, cur.y), (cur.x, cur.y-1), (cur.x, cur.y+1)]
        indexes = []
        for node in self.nodes:
            if node.wall:
                continue
            if (node.x, node.y) in neighbours:
                indexes.append(self.nodes.index(node))
        return indexes

    def find_nodes(self, cur: Node) -> list[Node]:
        neighbours = [(cur.x-1, cur.y), (cur.x+1, cur.y), (cur.x, cur.y-1), (cur.x, cur.y+1)]
        nodes = []
        for node in self.nodes:
            if node.wall:
                continue
            if (node.x, node.y) in neighbours:
                nodes.append(node)
        return nodes
    
    def find_nodes_walls(self, cur: Node) -> list[Node]:
        neighbours = [(cur.x-1, cur.y), (cur.x+1, cur.y), (cur.x, cur.y-1), (cur.x, cur.y+1)]
        nodes = []
        for node in self.nodes:
            if not node.wall:
                continue
            if (node.x, node.y) in neighbours:
                nodes.append(node)
        return nodes
    
    def get_max(self) -> tuple[int, int]:
        shortestX = 0
        shortestY = 0
        for node in self.nodes:
            if node.x > shortestX:
                shortestX = node.x
            if node.y > shortestY:
                shortestY = node.y
        return (shortestX, shortestY)
    
def build_node_map(input):
    nodes = NodeMap()
    start = None
    end = None
    for xIndex, line in enumerate(input):
        for yIndex, val in enumerate(line):
            if val == 'S':
                start = Node(xIndex, yIndex, False, 0)
                nodes.add_to_node(start)
                continue
            if val == 'E':
                end = Node(xIndex, yIndex, False, NOT_FOUND)
                nodes.add_to_node(end)
                continue
            nodes.add_to_node(Node(xIndex, yIndex, val == '#', NOT_FOUND))
    nodes.heapify()
    return (nodes, start, end)

def new_dijkstra(nodeMap: NodeMap, start: Node):
    distances = {}
    heap = [start]

    while heap:
        node = hq.heappop(heap)
        if node in distances:
            continue 
        
        distances[node] = -1
        for neighbour in nodeMap.find_nodes(node):
            if neighbour not in distances:
                if node.shortest + 1 < neighbour.shortest:
                    neighbour.shortest = node.shortest + 1
                    neighbour.fromNode = node
                hq.heappush(heap, neighbour)
    return None

def part_1():
    input = []
    walls = []
    with open("input.txt", "r") as file:
        for line in file:
            input.append([x for x in line.strip()])
    nodes, start, end = build_node_map(input)
    for xIndex, line in enumerate(input):
        for yIndex, val in enumerate(line):
            if val == 'S':
                start = Node(xIndex, yIndex, False, 0)
                nodes.add_to_node(start)
                continue
            if val == 'E':
                end = Node(xIndex, yIndex, False, NOT_FOUND)
                nodes.add_to_node(end)
                continue
            if val == "#":
                walls.append((xIndex, yIndex))
            nodes.add_to_node(Node(xIndex, yIndex, val == '#', NOT_FOUND))
    new_dijkstra(nodes, start)
    lookat = end
    wallCount = set()
    while lookat != None:
        wallCount.update({x for x in nodes.find_nodes_walls(lookat)})
        lookat = lookat.fromNode
    print(len(wallCount))        
    print(end.shortest)
    return None
    # costDiffs = []
    # frequencies = {}
    # for index, wall in enumerate(walls):
    #     # print(index/len(walls))
    #     input[wall[0]][wall[1]] = '.'
    #     nodes, start, end = build_node_map(input)
    #     costDiff = baseCost - djikstras(nodes, end)
    #     input[wall[0]][wall[1]] = '#'
    #     if costDiff > 0:
    #         # print(costDiff)
    #         frequencies[costDiff] = frequencies.get(costDiff, 0) + 1
    #         costDiffs.append(costDiff)
    #     nodes.unvisit_all(start)
    # totalAboveHundred = 0
    # for frequency in frequencies.keys():
    #     if frequency > 100:
    #         totalAboveHundred += frequencies[frequency]
    #     print(str(frequency) + ":", frequencies[frequency])
    # return totalAboveHundred
    


def djikstras(nodeMap: NodeMap, end: Node):
    allDistances = {}
    while True:
        cur = nodeMap.get_closest_node_to_start()
        if (cur == None):
            break
        if cur in allDistances:
            continue
        indexes = nodeMap.find_nodes_indexes(cur)
        for index in indexes:
            node = nodeMap.nodes[index]
            newDistance = cur.shortest + 1
            if (newDistance < node.shortest):
                node.shortest = newDistance
                node.fromNode = cur
        cur.visited = True
    shortest_path: list[tuple[int,int]] = []
    lookat = end
    while lookat.fromNode != None:
        shortest_path.append((lookat.fromNode.x, lookat.fromNode.y))
        lookat = lookat.fromNode
    
    # bounds = nodeMap.get_max()
    # for x in range(bounds[0] + 1):
    #     for y in range(bounds[1] + 1):
    #         if (x, y) in shortest_path:
    #             print("O", end="")
    #             continue
    #         node = nodeMap.freely_find_node(x, y)
    #         if (node.wall):
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print("")
    # print(end.shortest)
    # print("-----")
    return end.shortest
    
        
# def dfs(nodeMap: NodeMap, current: Node, costSoFar: int, end: Node) -> int:
#     current.visited = True
#     neighbours = [nodeMap.find_node(current.x-1, current.y), nodeMap.find_node(current.x+1, current.y), nodeMap.find_node(current.x, current.y-1), nodeMap.find_node(current.x, current.y+1)]
#     neighbours = [x for x in neighbours if x != None]
#     if current == end:
#         return costSoFar
#     if (len(neighbours) == 0):
#         return NOT_FOUND
#     costs = []
#     for neighbour in neighbours:
#         costs.append(dfs(nodeMap, neighbour, costSoFar + 1, end))
#     return min(costs)

if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    