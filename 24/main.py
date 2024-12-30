from collections import deque
from copy import deepcopy
from enum import Enum
import itertools


class Operation(Enum):
    AND = 0,
    OR = 1,
    XOR = 2,
    
    def __repr__(self):
        if (self.value[0] == 0):
            return "AND"
        if (self.value[0] == 1):
            return "OR"
        if (self.value[0] == 2):
            return "XOR"
        
    def __str__(self):
        return self.__repr__()

class Wire:
    def __init__(self, name: str, value):
        self.value = value
        self.name = name
        self.contributed: list[Wire] = []
    
    def add_contribution(self, contributions):
        self.contributed += contributions
    
    def reset_if_not_initial(self):
        if self.name[0] == 'x' or self.name[0] == 'y':
            return
        self.value = None
        
    def __repr__(self):
        return f"{self.name}: {self.value}"
    
    def is_output(self):
        return self.name[0] == 'z'
    
    def is_input(self):
        return self.name[0] == 'x' or self.name[0] == 'y'
    
    def __lt__(self, other):
        return int(self.name[1:]) > int(other.name[1:])
    
    def get_original_contributions(self):
        return [x for x in self.contributed if x.is_input()]
        
    # It is bad if a higher bit is affecting this, lower bit
    def suspicious(self):
        if not self.is_output():
            return False
        originalContributions = [int(x.name[1:]) for x in self.get_original_contributions()]
        myIndex = int(self.name[1:])
        if len(originalContributions) > (myIndex+1)*2:
            return True
        for contribution in originalContributions:
            if myIndex < contribution:
                return True
        return False
        
        
class Rule:
    def __init__(self, left: Wire, right: Wire, target: Wire, operation: Operation):
        self.left = left
        self.right = right
        self.target = target
        self.operation = operation
        
    def operate(self):
        match self.operation:
            case Operation.AND:
                self.target.value = self.left.value & self.right.value
            case Operation.OR:
                self.target.value = self.left.value | self.right.value
            case Operation.XOR:
                self.target.value = self.left.value ^ self.right.value
        self.target.add_contribution(self.left.contributed + [self.left])
        self.target.add_contribution(self.right.contributed + [self.right])
    
    def prepared(self):
        if self.left.value is None or self.right.value is None:
            return False
        return True
    
    def __repr__(self):
        return f"{self.left.name} {self.operation} {self.right.name} -> {self.target.name}"
                
            

def part_1():
    wires: list[Wire] = []
    rules: list[Rule] = []
    with open("input.txt", "r") as file:
        for line in file:
            if (len(line.strip()) == 0):
                continue
            if ':' in line:
                line = line.strip().split(": ")
                wires.append(Wire(line[0], int(line[1])))
            else:
                leftText, operation, rightText, _, targetText = line.strip().split()
                left = find_by_name(wires, leftText)
                if left is None:
                    left = Wire(leftText, None)
                    wires.append(left)
                right = find_by_name(wires, rightText)
                if right is None:
                    right = Wire(rightText, None)
                    wires.append(right)
                target = find_by_name(wires, targetText)
                if target is None:
                    target = Wire(targetText, None)
                    wires.append(target)
                rules.append(Rule(left, right, target, Operation[operation]))
    while len(rules) != 0:
        for index, rule in enumerate(rules):
            if not rule.prepared():
                continue
            rule.operate()
            rules.pop(index)
    outputWires: list[Wire] = [x for x in wires if x.is_output()]
    outputWires.sort()
    outputBits = "".join([str(x.value) for x in outputWires])
    return int(outputBits, 2)

# This method just isnt good here. Gotta do something new
def part_2():
    wires: list[Wire] = []
    rules: list[Rule] = []
    with open("input.txt", "r") as file:
        for line in file:
            if (len(line.strip()) == 0):
                continue
            if ':' in line:
                line = line.strip().split(": ")
                wires.append(Wire(line[0], int(line[1])))
            else:
                leftText, operation, rightText, _, targetText = line.strip().split()
                left = find_by_name(wires, leftText)
                if left is None:
                    left = Wire(leftText, None)
                    wires.append(left)
                right = find_by_name(wires, rightText)
                if right is None:
                    right = Wire(rightText, None)
                    wires.append(right)
                target = find_by_name(wires, targetText)
                if target is None:
                    target = Wire(targetText, None)
                    wires.append(target)
                rules.append(Rule(left, right, target, Operation[operation]))
    # pairs = itertools.combinations(rules, 2)
    # print(sum(1 for x in (itertools.combinations(pairs, 4))))
    # even for example two, there were so many here it took a CRAZY amount of time.
    while len(rules) != 0:
        for index, rule in enumerate(rules):
            if not rule.prepared():
                continue
            rule.operate()
            rules.pop(index)
    outputWires = [x for x in wires if x.is_output()]
    outputWires.sort()
    for wire in outputWires:
        if not wire.suspicious():
            continue
        print(wire)
        [print("    ",x) for x in wire.contributed if x.is_input()]
    outputBits = "".join([str(x.value) for x in outputWires])
    return int(outputBits, 2)
    
    
    
def find_by_name(wires: list[Wire], name: str):
    for wire in wires:
        if wire.name == name:
            return wire
    return None

if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    print("part 2:", part_2())
