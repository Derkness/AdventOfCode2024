regA = 0
regB = 0
regC = 0
pc = 0
output = []
def part_1():
    instructions = []
    global regA
    global regB
    global regC
    global pc
    global output
    with open("input.txt", "r") as file:
        lineIndex = -1
        for line in file:
            lineIndex += 1
            if len(line.strip()) == 0:
                continue
            line = line.strip().split(": ")[1]
            if lineIndex == 0:
                regA = int(line)
                continue
            if lineIndex == 1:
                regB = int(line)
                continue
            if lineIndex == 2:
                regC = int(line)
                continue
            instructions = [int(x) for x in line.split(",")]
    function_map = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv,
    }
    while pc < len(instructions):
        function_map[instructions[pc]](instructions[pc+1])
        pc += 2
    return output
    
def get_combo_operand(operand):
    global regA
    global regB
    global regC
    if operand == 1 or operand == 2 or operand == 3:
        return operand
    if operand == 4:
        return regA
    if operand == 5:
        return regB
    if operand == 6:
        return regC
    raise Exception(operand, "- Not implemented")
    
# 0
def adv(operand):
    global regA
    regA = regA >> get_combo_operand(operand)
    
# 1
def bxl(operand):
    global regB
    regB = regB ^ operand
    
# 2
def bst(operand):
    global regB
    regB = get_combo_operand(operand)%8

# 3
def jnz(operand):
    global regA
    global pc
    if regA == 0:
        return
    pc = operand - 2
    
# 4
def bxc(operand):
    global regB
    global regC
    regB = regB ^ regC

# 5
def out(operand):
    output.append(get_combo_operand(operand) % 8)
    
# 6
def bdv(operand):
    global regA
    global regB
    regB = regA >> get_combo_operand(operand)
    
# 7
def cdv(operand):
    global regA
    global regC
    regC = regA >> get_combo_operand(operand)

# This code doesn't really work, so this will explain my method
# Discovered to get 16 outputs (length of goal array) I need between 8^15 and 8^16 as input value
# Found out that the output relies on the bits. Tried to desk check it by hand but couldn't get a consistent pattern (check attempts.md for attempts lol)
# So, just tested every number from 1 to 10000 or so and printed out each initial A value that got out[0] = 2, out[1] = 4, out[2] = 1, and out[3] = 6.
# Turned that into binary.
# Converted the bottom and top ranges into what they woudl be with that binary chopped off the right side
# Ran through the range, for each i appending that binary back
# Test each :P
# So, I guess to summaryise, reduce solution space by finding a pattern, then test everything.
# It took about 4 hours to run. If I had added an extra check (say out[4] or out[5]) the solution space would have been reduced more, but I was tired so.

def part_2():
    instructions = []
    global regA
    global regB
    global regC
    global pc
    global output
    with open("input.txt", "r") as file:
        lineIndex = -1
        for line in file:
            lineIndex += 1
            if len(line.strip()) == 0:
                continue
            line = line.strip().split(": ")[1]
            if lineIndex == 0:
                regA = int(line)
                continue
            if lineIndex == 1:
                regB = int(line)
                continue
            if lineIndex == 2:
                regC = int(line)
                continue
            instructions = [int(x) for x in line.split(",")]
    function_map = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv,
    }
    for i in range(1_305_800_000, 2_013_265_920):
        a = i
        i = int(bin(i)[2:] + '010101110010010', 2)
        output.clear()
        regA = i
        regB = 0
        regC = 0
        pc = 0
        while pc < len(instructions):
            function_map[instructions[pc]](instructions[pc+1])
            pc += 2
        if (a%5000 == 0):
            print(output)
            print(((a-1_073_741_824)/(2_013_265_920-1_073_741_824))*100, i)
        if instructions == output:
            return i

def check_viable(a):
    while True:
        b = (a % 8) ^ 6
        c = a >> b
        b = b ^ c
        b = (b^7)
        yield b % 8
        if a==2:
            break
if __name__ == "__main__":
    print("part 1:", part_1())
    # print("part 2:", part_2())
   