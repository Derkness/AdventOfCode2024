def part_1():
    rules = []
    updates = []
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if '|' in line:
                rules.append([int(x) for x in line.split('|')])
            elif ',' in line:
                updates.append([int(x) for x in line.split(',')])
    count = 0
    for update in updates:
        count += check_update(update, rules)
    return count
                    
def check_update(update, rules):
    for pageIndex, page in enumerate(update):
        for rule in rules:
            if rule[0] == page:
                if (rule[1] in update) and (rule[1] not in update[(pageIndex+1)::]):
                    return 0
            elif rule[1] == page:
                if (rule[0] in update) and (rule[0] not in update[:pageIndex]):
                    return 0
    return update[int((len(update)-1)/2)]
    
if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())