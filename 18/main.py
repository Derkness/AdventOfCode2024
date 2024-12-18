from enum import Enum


class Node:
    def __init__(self, x: int, y: int, shortestValue: int):
        self.x = x
        self.y = y
        self.shortestValue = shortestValue
        self.fromNode: Node | None = None
        self.visited: bool = False
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ") - " + str(self.shortestValue)

class NodeMap:
    def __init__(self):
        self.nodes: list[Node] = []
        
    def add_to_node(self, node: Node):
        self.nodes += [node]
    
    def find_node(self, x, y):
        for node in self.nodes:
            if node.x == x and node.y == y:
                return node
        return None
    
    def remove_node(self, x, y):
        for index, node in enumerate(self.nodes):
            if node.x == x and node.y == y:
                return self.nodes.pop(index)
            
    def get_closest_node_to_start(self) -> int | None:
        closestNode = Node(-1,-1, 1_000_000_000_000_00)
        if (len([x for x in self.nodes if x.visited == False]) == 0):
            return None
        for node in self.nodes:
            if (node.visited == True):
                continue
            if (node.shortestValue < closestNode.shortestValue):
                closestNode = node
        if closestNode.x == -1:
            return None
        return self.nodes.index(closestNode)

    def find_nodes_indexes(self, cur: Node) -> list[int]:
        neighbours = [(cur.x-1, cur.y), (cur.x+1, cur.y), (cur.x, cur.y-1), (cur.x, cur.y+1)]
        indexes = []
        for node in self.nodes:
            if (node.x, node.y) in neighbours:
                indexes.append(self.nodes.index(node))
        return indexes

def part_1():
    SIZE = 70
    LIMIT = 1024 # For part 2, trial and error (binary search ish) gave me 2856 blocked it (24, 32)
    nodeMap = NodeMap()
    for xIndex in range(SIZE + 1):
        for yIndex in range(SIZE + 1):
            nodeMap.add_to_node(Node(xIndex, yIndex, 1_000_000_000_000_000))
    goal = nodeMap.find_node(SIZE, SIZE)
    instructions = []
    instructionCount = 0
    with open("input.txt", "r") as file:
        for line in file:
            instructionCount+=1
            if instructionCount > LIMIT:
                print(instructions[-1])
                break
            instructions.append([int(x) for x in line.strip().split(",")])
    for instruction in instructions:
        nodeMap.remove_node(instruction[1], instruction[0])
    nodeMap.find_node(0,0).shortestValue = 0

    while True:
        curIndex = nodeMap.get_closest_node_to_start()
        if (curIndex == None):
            break
        cur = nodeMap.nodes[curIndex]
        indexes = nodeMap.find_nodes_indexes(cur)
        for index in indexes:
            node = nodeMap.nodes[index]
            newDistance = cur.shortestValue + 1
            if (newDistance < node.shortestValue):
                node.shortestValue = newDistance
                node.fromNode = cur
        cur.visited = True
    shortest_path: list[Node] = []
    lookat = goal
    while lookat.fromNode != None:
        shortest_path.append(lookat.fromNode)
        lookat = lookat.fromNode
    
    return len(shortest_path)

if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    