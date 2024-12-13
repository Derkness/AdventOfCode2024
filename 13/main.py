class Machine:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.o = 0
        self.p = 0
        self.val1 = 0
        self.val2 = 0
    
    def calculate_a_and_b(self) -> tuple[int, int] | None:
        numerator = self.o*self.val1-self.m*self.val2
        denominator = self.o*self.n-self.m*self.p
        b = numerator/denominator
        a = (self.val1-b*self.n)/self.m
        if a.is_integer() and a > 0:
            if b.is_integer() and b > 0:
                return (int(a), int(b))
        return None

def execute(addedGoal: int):
    lines: list[str] =[]
    with open("input.txt", "r") as file:
        for line in file:
            if (line.strip() == ""):
                continue
            lines.append(line.strip().split(":")[1].strip())
    machines: list[Machine] = []
    currentMachine: Machine = None
    for index, line in enumerate(lines):
        if index % 3 == 0:
            brokenUp = line.split(", ")
            currentMachine = Machine()
            currentMachine.m = int(brokenUp[0][2:])
            currentMachine.o = int(brokenUp[1][2:])
        elif index % 3 == 1:
            brokenUp = line.split(", ")
            currentMachine.n = int(brokenUp[0][2:])
            currentMachine.p = int(brokenUp[1][2:])
        elif index % 3 == 2:
            brokenUp = line.split(", ")
            currentMachine.val1 = int(brokenUp[0][2:]) + addedGoal
            currentMachine.val2 = int(brokenUp[1][2:]) + addedGoal
            machines.append(currentMachine)
    total = 0
    for machine in machines:
        retVal = machine.calculate_a_and_b()
        if retVal is None:
            continue
        a, b = retVal
        total += 3*a+b
    return total

if __name__ == "__main__":
    totalValue = 0
    print("part 1:", execute(0))
    print("part 2:", execute(10000000000000))