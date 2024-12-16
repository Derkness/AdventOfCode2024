import sys
from enum import Enum

shortest_path = []

class Direction(Enum):
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3,
    
    def __repr__(self):
        if (self.value[0] == 0):
            return "NORTH"
        if (self.value[0] == 1):
            return "EAST"
        if (self.value[0] == 2):
            return "SOUTH"
        if (self.value[0] == 3):
            return "WEST"

class Node:
    def __init__(self, x: int, y: int, shortestValue: int):
        self.x = x
        self.y = y
        self.shortestValue = shortestValue
        self.fromNode: Node | None = None
        self.couldHaveComeFrom: list[Node] = []
        self.visited: bool = False
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ") - " + str(self.shortestValue)

def part_1():
    unvisitedNodes: list[Node] = []
    currentDirection = Direction.EAST
    goal = None
    with open("input.txt", "r") as file:
        for xIndex, line in enumerate(file):
            for yIndex, val in enumerate(line.strip()):
                if val == 'S':
                    unvisitedNodes.append(Node(xIndex, yIndex, 0))
                    continue
                if val == 'E':
                    goal = Node(xIndex, yIndex, 1_000_000_000_000_000)
                    unvisitedNodes.append(goal)
                    continue
                if val == '#':
                    continue
                unvisitedNodes.append(Node(xIndex, yIndex, 1_000_000_000_000_000))
    while True:
        curIndex = get_closest_node_to_start(unvisitedNodes)
        if (curIndex == None):
            break
        cur = unvisitedNodes[curIndex]
        indexes = find_nodes_indexes(unvisitedNodes, cur)
        if cur.fromNode != None:
            currentDirection = get_relative_direction(cur.fromNode, cur)
        for index in indexes:
            node = unvisitedNodes[index]
            newDistance = cur.shortestValue
            newDirection = get_relative_direction(cur, node)
            if newDirection == currentDirection:
                newDistance += 1
            else:
                match currentDirection:
                    case Direction.SOUTH:
                        if newDirection != Direction.NORTH:
                            newDistance += 1001
                        else:
                            continue
                    case Direction.NORTH:
                        if newDirection != Direction.SOUTH:
                            newDistance += 1001
                        else:
                            continue
                    case Direction.WEST:
                        if newDirection != Direction.EAST:
                            newDistance += 1001
                        else:
                            continue
                    case Direction.EAST:
                        if newDirection != Direction.WEST:
                            newDistance += 1001
                        else:
                            continue
            if (newDistance < node.shortestValue):
                node.shortestValue = newDistance
                node.fromNode = cur
        unvisitedNodes.pop(curIndex)
    global shortest_path
    lookat = goal
    while lookat.fromNode != None:
        shortest_path.append(lookat.fromNode)
        lookat = lookat.fromNode
    return goal

nodes_on_paths = set()

def part_2():
    unvisitedNodes: list[Node] = []
    currentDirection = Direction.EAST
    goal = None
    start = None
    with open("input.txt", "r") as file:
        for xIndex, line in enumerate(file):
            for yIndex, val in enumerate(line.strip()):
                if val == 'S':
                    start = Node(xIndex, yIndex, 0)
                    unvisitedNodes.append(start)
                    continue
                if val == 'E':
                    goal = Node(xIndex, yIndex, 1_000_000_000_000_000)
                    unvisitedNodes.append(goal)
                    continue
                if val == '#':
                    continue
                unvisitedNodes.append(Node(xIndex, yIndex, 1_000_000_000_000_000))
    while True:
        curIndex = get_closest_node_to_start(unvisitedNodes)
        if (curIndex == None):
            break
        cur = unvisitedNodes[curIndex]
        indexes = find_nodes_indexes(unvisitedNodes, cur)
        if cur.fromNode != None:
            currentDirection = get_relative_direction(cur.fromNode, cur)
        for index in indexes:
            node = unvisitedNodes[index]
            node.couldHaveComeFrom += [cur]
            newDistance = cur.shortestValue
            newDirection = get_relative_direction(cur, node)
            if newDirection == currentDirection:
                newDistance += 1
            else:
                match currentDirection:
                    case Direction.SOUTH:
                        if newDirection != Direction.NORTH:
                            newDistance += 1001
                        else:
                            continue
                    case Direction.NORTH:
                        if newDirection != Direction.SOUTH:
                            newDistance += 1001
                        else:
                            continue
                    case Direction.WEST:
                        if newDirection != Direction.EAST:
                            newDistance += 1001
                        else:
                            continue
                    case Direction.EAST:
                        if newDirection != Direction.WEST:
                            newDistance += 1001
                        else:
                            continue
            if (newDistance < node.shortestValue):
                node.shortestValue = newDistance
                node.fromNode = cur
        unvisitedNodes[curIndex].visited = True
    print(goal.couldHaveComeFrom)
    nodes_on_chosen_path = set()
    lookat = goal
    nodes_on_chosen_path.add(goal)
    while lookat.fromNode != None:
        nodes_on_chosen_path.add(lookat.fromNode)
        lookat = lookat.fromNode
        #  Consider that if its too slow
    global nodes_on_paths
    get_path_cost(goal, Direction.SOUTH, start, 0, goal.shortestValue, [])
    print(len(nodes_on_paths))
    return goal.shortestValue
considered = set()
def get_path_cost(node: Node, currentDirection: Direction, start: Node, cost_so_far: int, best_cost: int, path_so_far: list[Node]):
    global considered
    if node in considered:
        return cost_so_far
    considered.add(node)
    global nodes_on_paths
    if cost_so_far > best_cost:
        return -1
    if (node.x == start.x and node.y == start.y):
        nodes_on_paths.update(path_so_far)
        return cost_so_far
    all_costs = []
    couldHave = node.couldHaveComeFrom
    smallestCould = couldHave[0]
    for could in couldHave:
        if could.shortestValue < smallestCould.shortestValue:
            smallestCould = could
    couldHave = [x for x in couldHave if x.shortestValue == smallestCould.shortestValue]
    for next in node.couldHaveComeFrom:
        newDirection = get_relative_direction(node, next)
        newDistance = cost_so_far
        if newDirection == currentDirection:
            newDistance += 1
        else:
            match currentDirection:
                case Direction.SOUTH:
                    if newDirection != Direction.NORTH:
                        newDistance += 1001
                case Direction.NORTH:
                    if newDirection != Direction.SOUTH:
                        newDistance += 1001
                case Direction.WEST:
                    if newDirection != Direction.EAST:
                        newDistance += 1001
                case Direction.EAST:
                    if newDirection != Direction.WEST:
                        newDistance += 1001
        all_costs.append(get_path_cost(next, newDirection, start, newDistance, best_cost, path_so_far + [node]))
    return min(all_costs)

def get_nodes(node: Node) -> list[Node]:
    if len(node.fromNode2) == 0:
        return [node]
    nodes = [node]
    for fromNode in node.fromNode2:
        nodes += [x for x in get_nodes(fromNode)]
    return nodes
            
def get_relative_direction(fromPoint: Node, toPoint: Node):
    if fromPoint.x > toPoint.x:
        return Direction.NORTH
    if fromPoint.x < toPoint.x:
        return Direction.SOUTH
    if fromPoint.y > toPoint.y:
        return Direction.WEST
    if fromPoint.y < toPoint.y:
        return Direction.EAST
    
def find_nodes_indexes(unvisitedNodes: list[Node], cur: Node) -> list[int]:
    neighbours = [(cur.x-1, cur.y), (cur.x+1, cur.y), (cur.x, cur.y-1), (cur.x, cur.y+1)]
    indexes = []
    for node in unvisitedNodes:
        if (node.x, node.y) in neighbours:
            indexes.append(unvisitedNodes.index(node))
    return indexes
        
def get_closest_node_to_start(unvisitedNodes: list[Node]) -> int | None:
    closestNode = Node(-1,-1, 1_000_000_000_000_00)
    if (len([x for x in unvisitedNodes if x.visited == False]) == 0):
        return None
    for node in unvisitedNodes:
        if (node.visited == True):
            continue
        if (node.shortestValue < closestNode.shortestValue):
            closestNode = node
    return unvisitedNodes.index(closestNode)
    
def get_cardinal_neighbour_indexes(x: int, y:int, twod_array: list[list]) -> set:
    maxX = len(twod_array)
    maxY = len(twod_array[0])
    if not check_array_bounds(x, y, maxX, maxY):
        return set()
    options = set()
    options = options.union({(x-1, y)}) if check_array_bounds(x-1, y, maxX, maxY) and twod_array[x-1][y] else options
    options = options.union({(x+1, y)}) if check_array_bounds(x+1, y, maxX, maxY) and twod_array[x+1][y] else options
    options = options.union({(x, y-1)}) if check_array_bounds(x, y-1, maxX, maxY) and twod_array[x][y-1] else options
    options = options.union({(x, y+1)}) if check_array_bounds(x, y+1, maxX, maxY) and twod_array[x][y+1] else options
    return options
        
def check_array_bounds(x: int, y: int, maxX: int, maxY: int) -> bool:
    if x < 0 or y < 0:
        return False
    if x >= maxX or y >= maxY:
        return False
    return True
    
if __name__ == "__main__":
    totalValue = 0
    # print("part 1:", part_1())
    print("part 2:", part_2())