def part_1():
    successes = 0
    with open("input.txt", "r") as file:
        for line in file:
            goal, method = line.split(":")
            numbers = [int(x) for x in method.strip().split()]
            numberOfGaps = len(numbers) - 1
            bitLength = len(to_base_string(pow(2,numberOfGaps)-1, 2))
            for convertToBit in range(pow(2,numberOfGaps)):
                workToGoal = numbers[0]
                bits = to_base_string(convertToBit, 2)
                while (len(bits) < bitLength):
                    bits = '0' + bits
                for index, bit in enumerate(bits):
                    if bit == '0':
                        workToGoal *= numbers[index+1]
                    else:
                        workToGoal += numbers[index+1]
                if workToGoal == int(goal):
                    successes += int(goal)
                    break
    return successes

def part_2():
    successes = 0
    with open("input.txt", "r") as file:
        for index, line in enumerate(file):
            goal, method = line.split(":")
            numbers = [int(x) for x in method.strip().split()]
            numberOfGaps = len(numbers) - 1
            bitLength = len(to_base_string(pow(3,numberOfGaps)-1, 3))
            for convertToBit in range(pow(3,numberOfGaps)):
                workToGoal = numbers[0]
                bits = to_base_string(convertToBit, 3)
                while (len(bits) < bitLength):
                    bits = '0' + bits
                for index, bit in enumerate(bits):
                    if bit == '0':
                        workToGoal *= numbers[index+1]
                    elif bit == '1':
                        workToGoal += numbers[index+1]
                    elif bit == '2':
                        workToGoal = int(str(workToGoal) + str(numbers[index+1]))
                if workToGoal == int(goal):
                    successes += int(goal)
                    break
    return successes
                    
def to_base_string(n: int, base: int) -> str:
    if n == 0:
        return "0"
    output = []
    n = abs(n)
    while n > 0:
        output.append(str(n % base))
        n //= base
    return ''.join(reversed(output))
            
            
if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    print("part 2:", part_2())
    