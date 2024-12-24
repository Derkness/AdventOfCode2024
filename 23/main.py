class Computer:
    def __init__(self, name: str):
        self.name = name
        self.connections: set[Computer] = set()
    
    def add_link(self, other):
        self.connections.add(other)

    def __repr__(self):
        return "Name: " + self.name + ". Links to " + ",".join([x.name for x in self.connections])
    
    def __eq__(self, value):
        return self.name == value.name
    
    def __hash__(self):
        return ord(self.name[0])*1000+ord(self.name[1])

def part_1():
    input = []
    with open("input.txt", "r") as file:
        for line in file:
            input.append(line.strip().split('-'))
    party: list[Computer] = []
    for link in input:
        left = find_by_name(party, link[0])
        if left is None:
            left = Computer(link[0])
            party.append(left)
        right = find_by_name(party, link[1])
        if right is None:
            right = Computer(link[1])
            party.append(right)
        left.add_link(right)
        right.add_link(left)
    triples = set()
    for computer in party:
        for firstConnetion in computer.connections:
            for secondConnection in computer.connections:
                if firstConnetion == secondConnection:
                    continue
                if secondConnection in firstConnetion.connections:
                    triples.add(tuple(sorted((computer.name, firstConnetion.name, secondConnection.name))))
    triples = {x for x in triples if x[0][0] == 't' or x[1][0] == 't' or x[2][0] == 't'}
    return len(triples)

def find_by_name(computers: list[Computer], name: str):
    for computer in computers:
        if computer.name == name:
            return computer
    return None

def part_2():
    input = []
    with open("input.txt", "r") as file:
        for line in file:
            input.append(line.strip().split('-'))
    party: list[Computer] = []
    for link in input:
        left = find_by_name(party, link[0])
        if left is None:
            left = Computer(link[0])
            party.append(left)
        right = find_by_name(party, link[1])
        if right is None:
            right = Computer(link[1])
            party.append(right)
        left.add_link(right)
        right.add_link(left)
    cliques = []
    bron_kerbosch(set(), set(party), set(), cliques)
    biggest: tuple[list[Computer], int] = ([],0)
    for clique in cliques:
        if len(clique) > biggest[1]:
            biggest = (clique, len(clique))
    return ",".join(sorted([x.name for x in biggest[0]]))

# Some algo to find all 'maximal cliques' (subsets of a graph that are fully connected, and theres no more nodes to add into the subnodes that will also be interconnected)
def bron_kerbosch(currentClique: set[Computer], remaining: set[Computer], past: set[Computer], cliques: list[list[Computer]]):
    if len(remaining) == len(past) == 0:
        cliques.append(list(currentClique))
        return
    for computer in list(remaining):
        neighbors = computer.connections
        bron_kerbosch(currentClique | {computer}, remaining & neighbors, past & neighbors, cliques) # R ⋃ {v}        P ⋂ N(v)        X ⋂ N(v)
        remaining.remove(computer)
        past.add(computer)
                
if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    print("part 2:", part_2())
