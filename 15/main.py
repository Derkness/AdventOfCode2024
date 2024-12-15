moveable: list[tuple[int,int]] = []
def part_1():
    actions: list[str] = []
    map: list[list[str]] = []
    readingMap = True
    cur = (0,0)
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if readingMap:
                if line == "":
                    readingMap = False
                    continue
                map.append([x for x in line])
                continue
            for x in line:
                actions.append(x)
    for xIndex, line in enumerate(map):
        if '@' in line:
            cur = (xIndex, line.index('@'))
            line[line.index('@')] = '.'
    for action in actions:
        if (action == "^"):
            next = get_next_free_space(map, -1, 0, cur[0], cur[1])
            if (next == None):
                continue
            map[cur[0]-1][cur[1]], map[next[0]][next[1]] = map[next[0]][next[1]], map[cur[0]-1][cur[1]]
            cur = (cur[0]-1, cur[1])
        if (action == "v"):
            next = get_next_free_space(map, 1, 0, cur[0], cur[1])
            if (next == None):
                continue
            map[cur[0]+1][cur[1]], map[next[0]][next[1]] = map[next[0]][next[1]], map[cur[0]+1][cur[1]]
            cur = (cur[0]+1, cur[1])
        if (action == ">"):
            next = get_next_free_space(map, 0, 1, cur[0], cur[1])
            if (next == None):
                continue
            map[cur[0]][cur[1]+1], map[next[0]][next[1]] = map[next[0]][next[1]], map[cur[0]][cur[1]+1]
            cur = (cur[0], cur[1]+1)
        if (action == "<"):
            next = get_next_free_space(map, 0, -1, cur[0], cur[1])
            if (next == None):
                continue
            map[cur[0]][cur[1]-1], map[next[0]][next[1]] = map[next[0]][next[1]], map[cur[0]][cur[1]-1]
            cur = (cur[0], cur[1]-1)
    total = 0
    for xIndex, line in enumerate(map):
        for yIndex, val in enumerate(line):
            if val == 'O':
                total+= xIndex*100+yIndex
    return total

def get_next_free_space(map, xWalk, yWalk, xCurrent, yCurrent) -> tuple[int,int] | None:
    val = map[xCurrent][yCurrent]
    i = 1
    while val != '#':
        val = map[xCurrent+i*xWalk][yCurrent+i*yWalk]
        if (val == '.'):
            return (xCurrent+i*xWalk, yCurrent+i*yWalk)
        i+=1
    return None
    
def part_2():
    global moveable
    map_pt2: list[list[str]] = []
    actions: list[str] = []
    readingMap = True
    cur = (0,0)
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if readingMap:
                if line == "":
                    readingMap = False
                    continue
                next_row = []
                for val in line:
                    match val:
                        case '#':
                            next_row = next_row + (["#", "#"])
                        case 'O':
                            next_row = next_row + (["[", "]"])
                        case '.':
                            next_row = next_row + ([".", "."])
                        case '@':
                            next_row = next_row + (["@", "."])
                map_pt2.append(next_row)
                    
                continue
            for x in line:
                actions.append(x)
    for xIndex, line in enumerate(map_pt2):
        if '@' in line:
            cur = (xIndex, line.index('@'))
            line[line.index('@')] = '.'
    
    for action in actions:
        moveable.clear()
        canMove = True
        if action == '^':
            if map_pt2[cur[0]-1][cur[1]] == '#':
                continue
            if map_pt2[cur[0]-1][cur[1]] == '[':
                canMove = boxes_moved_as_part_of_action(map_pt2, (cur[0]-1, cur[1]), action)
            if map_pt2[cur[0]-1][cur[1]] == ']':
                canMove = boxes_moved_as_part_of_action(map_pt2, (cur[0]-1, cur[1]-1), action)
            if canMove:
                for boxToMove in moveable:
                    map_pt2[boxToMove[0]][boxToMove[1]], map_pt2[boxToMove[0]-1][boxToMove[1]] = map_pt2[boxToMove[0]-1][boxToMove[1]], map_pt2[boxToMove[0]][boxToMove[1]]
                    map_pt2[boxToMove[0]][boxToMove[1]+1], map_pt2[boxToMove[0]-1][boxToMove[1]+1] = map_pt2[boxToMove[0]-1][boxToMove[1]+1], map_pt2[boxToMove[0]][boxToMove[1]+1]
                cur = (cur[0]-1, cur[1])
                
        if action == 'v':
            if map_pt2[cur[0]+1][cur[1]] == '#':
                continue
            if map_pt2[cur[0]+1][cur[1]] == '[':
                canMove = boxes_moved_as_part_of_action(map_pt2, (cur[0]+1, cur[1]), action)
            if map_pt2[cur[0]+1][cur[1]] == ']':
                canMove = boxes_moved_as_part_of_action(map_pt2, (cur[0]+1, cur[1]-1), action)
            if canMove:
                for boxToMove in moveable:
                    map_pt2[boxToMove[0]][boxToMove[1]], map_pt2[boxToMove[0]+1][boxToMove[1]] = map_pt2[boxToMove[0]+1][boxToMove[1]], map_pt2[boxToMove[0]][boxToMove[1]]
                    map_pt2[boxToMove[0]][boxToMove[1]+1], map_pt2[boxToMove[0]+1][boxToMove[1]+1] = map_pt2[boxToMove[0]+1][boxToMove[1]+1], map_pt2[boxToMove[0]][boxToMove[1]+1]
                cur = (cur[0]+1, cur[1])
                
        if action == '<':
            if map_pt2[cur[0]][cur[1]-1] == '#':
                continue
            if map_pt2[cur[0]][cur[1]-1] == ']':
                canMove = boxes_moved_as_part_of_action(map_pt2, (cur[0], cur[1]-2), action)
            if canMove:
                for boxToMove in moveable:
                    map_pt2[boxToMove[0]][boxToMove[1]-1], map_pt2[boxToMove[0]][boxToMove[1]] = map_pt2[boxToMove[0]][boxToMove[1]], map_pt2[boxToMove[0]][boxToMove[1]-1]
                    map_pt2[boxToMove[0]][boxToMove[1]], map_pt2[boxToMove[0]][boxToMove[1]+1] = map_pt2[boxToMove[0]][boxToMove[1]+1], map_pt2[boxToMove[0]][boxToMove[1]]
                cur = (cur[0], cur[1]-1)
                
        if action == '>':
            if map_pt2[cur[0]][cur[1]+1] == '#':
                continue
            if map_pt2[cur[0]][cur[1]+1] == '[':
                canMove = boxes_moved_as_part_of_action(map_pt2, (cur[0], cur[1]+1), action)
            if canMove:
                for boxToMove in moveable:
                    map_pt2[boxToMove[0]][boxToMove[1]+1], map_pt2[boxToMove[0]][boxToMove[1]+2] = map_pt2[boxToMove[0]][boxToMove[1]+2], map_pt2[boxToMove[0]][boxToMove[1]+1]
                    map_pt2[boxToMove[0]][boxToMove[1]], map_pt2[boxToMove[0]][boxToMove[1]+1] = map_pt2[boxToMove[0]][boxToMove[1]+1], map_pt2[boxToMove[0]][boxToMove[1]]
                cur = (cur[0], cur[1]+1)
        for spa in map_pt2:
            openBrace = False
            for letter in spa:
                if openBrace and letter != ']':
                    return
                if letter == '[':
                    openBrace = True
                if letter == ']':
                    openBrace = False
    total = 0
    for xIndex, line in enumerate(map_pt2):
        for yIndex, val in enumerate(line):
            if val == '[':
                total+= xIndex*100+yIndex
    return total

# Its not great, but this fills the global 'moveable' variable as a side effect
def boxes_moved_as_part_of_action(map_pt2: list[list[str]], boxLeft: tuple[int,int], direction: str) -> bool:
    if direction == '^':
        canMove = True
        if map_pt2[boxLeft[0]-1][boxLeft[1]] == '#' or map_pt2[boxLeft[0]-1][boxLeft[1]+1] == '#':
            return False
        if map_pt2[boxLeft[0]-1][boxLeft[1]] == '[':
            canMove &= boxes_moved_as_part_of_action(map_pt2, (boxLeft[0]-1, boxLeft[1]), direction)
        if map_pt2[boxLeft[0]-1][boxLeft[1]] == ']':
            canMove &= boxes_moved_as_part_of_action(map_pt2, (boxLeft[0]-1, boxLeft[1]-1), direction)
        if map_pt2[boxLeft[0]-1][boxLeft[1]+1] == '[':
            canMove &= boxes_moved_as_part_of_action(map_pt2, (boxLeft[0]-1, boxLeft[1]+1), direction)
        if canMove:
            if (boxLeft[0], boxLeft[1]) not in moveable:
                moveable.append((boxLeft[0], boxLeft[1]))
                moveable.sort(key=lambda x: x[0])
        return canMove
    
    if direction == 'v':
        canMove = True
        if map_pt2[boxLeft[0]+1][boxLeft[1]] == '#' or map_pt2[boxLeft[0]+1][boxLeft[1]+1] == '#':
            return False
        if map_pt2[boxLeft[0]+1][boxLeft[1]] == '[':
            canMove &= boxes_moved_as_part_of_action(map_pt2, (boxLeft[0]+1, boxLeft[1]), direction)
        if map_pt2[boxLeft[0]+1][boxLeft[1]] == ']':
            canMove &= boxes_moved_as_part_of_action(map_pt2, (boxLeft[0]+1, boxLeft[1]-1), direction)
        if map_pt2[boxLeft[0]+1][boxLeft[1]+1] == '[':
            canMove &= boxes_moved_as_part_of_action(map_pt2, (boxLeft[0]+1, boxLeft[1]+1), direction)
        if canMove:
            if (boxLeft[0], boxLeft[1]) not in moveable:
                moveable.append((boxLeft[0], boxLeft[1]))
                moveable.sort(key=lambda x: -x[0])
        return canMove
    
    if direction == '<':
        canMove = True
        if map_pt2[boxLeft[0]][boxLeft[1]-1] == '#':
            return False
        if map_pt2[boxLeft[0]][boxLeft[1]-1] == ']':
            canMove &= boxes_moved_as_part_of_action(map_pt2, (boxLeft[0], boxLeft[1]-2), direction)
        if canMove:
            if (boxLeft[0], boxLeft[1]) not in moveable:
                moveable.append((boxLeft[0], boxLeft[1]))
                moveable.sort(key=lambda x: x[1])
        return canMove
    
    if direction == '>':
        canMove = True
        if map_pt2[boxLeft[0]][boxLeft[1]+2] == '#':
            return False
        if map_pt2[boxLeft[0]][boxLeft[1]+2] == '[':
            canMove &= boxes_moved_as_part_of_action(map_pt2, (boxLeft[0], boxLeft[1]+2), direction)
        if canMove:
            if (boxLeft[0], boxLeft[1]) not in moveable:
                moveable.append((boxLeft[0], boxLeft[1]))
                moveable.sort(key=lambda x: -x[1])
        return canMove
        
if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    print("part 2:", part_2())