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

def part_2():
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
        count += fix_and_check_update(update, rules)
    return count
                    
def fix_and_check_update(update, rules):
    safe = True
    # Might need multiple run throughs. A weird bubblesort-ish sitch
    while (check_update(update, rules) == 0):
        for pageIndex in range(len(update)):
            for rule in rules:
                if (not(rule[0] in update and rule[1] in update)):
                    continue
                if rule[0] == update[pageIndex]:
                    if (rule[1] not in update[(pageIndex+1)::]):
                        safe = False
                        indexOther = update.index(rule[1])
                        update[pageIndex], update[indexOther] = update[indexOther], update[pageIndex]
                elif rule[1] == update[pageIndex]:
                    if (rule[0] not in update[:pageIndex]):
                        safe = False
                        indexOther = update.index(rule[0])
                        update[pageIndex], update[indexOther] = update[indexOther], update[pageIndex]

    return update[int((len(update)-1)/2)] if not safe else 0
    
if __name__ == "__main__":
    totalValue = 0
    print("part 1:", part_1())
    print("part 2:", part_2())
    