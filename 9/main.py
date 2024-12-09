from copy import deepcopy
from enum import Enum


def part_1():
    line = []
    memory = []
    with open("input.txt", "r") as file:
        for content in file:
            line = [x for x in content]
            for index, val in enumerate(line):
                if index % 2 == 0: # File
                    memory = memory + [index//2] * int(val)
                else:
                    memory = memory + ['.'] * int(val)
    previousBlankSpot = 0
    while '.' in memory:
        firstBlankSpot = memory.index('.', previousBlankSpot)
        lastElement = '.'
        while lastElement =='.':
            lastElement = memory.pop()
        if firstBlankSpot >= len(memory):
            memory = [x for x in memory if x != '.'] + [lastElement]
            break
        memory[firstBlankSpot] = lastElement
        previousBlankSpot = firstBlankSpot
    retVal = 0
    for index, value in enumerate(memory):
        retVal += index * value
    return retVal

class BlockType(Enum):
    FREE = 0,
    FULL = 1,

class Block:
    def __init__(self, type: BlockType, length: int, value: str | int):
        self.type = type
        self.length = length
        self.value = value
        self.moved = False

    def __repr__(self):
        if self.type == BlockType.FREE:
            return "." * self.length
        elif self.type == BlockType.FULL:
            return str(self.value) * self.length
    
def sortFunc(e):
    return e[0]

def part_2():
    line = []
    memory: list[Block] = []
    with open("input.txt", "r") as file:
        for content in file:
            line = [x for x in content]
            for index, val in enumerate(line):
                if index % 2 == 0: # File
                    memory.append(Block(BlockType.FULL, int(val), int(index)//2))
                else:
                    memory.append(Block(BlockType.FREE, int(val), '.'))
    
    insertions = []
    found = False
    for spotIndex, spot in enumerate(reversed(memory)):
        found = False
        if spot.type is BlockType.FULL:
            for possibleSpotIndex, possibleSpot in enumerate(memory[:(len(memory)-spotIndex)]):
                if (possibleSpot.type is BlockType.FREE and possibleSpot.length >= spot.length):
                    possibleSpot.length -= spot.length
                    insertions.append((possibleSpotIndex, deepcopy(spot)))
                    spot.moved = True
                    spot.type = BlockType.FREE
                    spot.value = '.'
                    found = True
                    break
            if found:
                continue
    insertions.sort(key=lambda insert : insert[0])
    for insertion in reversed(insertions):
        insertion[1].moved = True
        memory.insert(insertion[0], insertion[1])
    retVal = 0
    flattened = []
    for x in memory:
        flattened = flattened + [x.value]*x.length
    for index, value in enumerate(flattened):
        if (value == '.'):
            continue
        retVal += index * int(value)
    return retVal
                
if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    print("part 2:", part_2())
    