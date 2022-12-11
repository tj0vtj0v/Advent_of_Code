import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
inputtext = inputfile.readlines()

monkeys = []
monkey = []
for line in inputtext:
    linetext = line.removesuffix("\n")
    
    if "Starting items:" in linetext:
        linetext = linetext.removeprefix("  Starting items: ")
        items = linetext.split(", ")
        monkey.append(items)
    if "Operation:" in linetext:
        linetext = linetext.removeprefix("  Operation: ")
        operation = linetext.removeprefix("new = ")
        monkey.append(operation)
    if "Test:" in linetext:
        linetext = linetext.removeprefix("  Test: divisible by ")
        monkey.append(int(linetext))
    if "  If true: throw to monkey" in linetext:
        linetext = linetext.removeprefix("    If true: throw to monkey ")
        monkey.append(int(linetext))
    if "  If false: throw to monkey" in linetext:
        linetext = linetext.removeprefix("    If false: throw to monkey ")
        monkey.append(int(linetext))
    if "" == linetext:
        monkey.append(0)
        monkeys.append(monkey)
        monkey = []
monkey.append(0)
monkeys.append(monkey)

import math

for count in range(20):
    change = []
    for monkey in monkeys:
        print(monkey)
        change.append([])
    
    for monkey in monkeys:
        
        for item in monkey[0]:
            monkey[5] += 1
            worry = int(item)
            worry = eval(monkey[1].replace("old", "worry"))
            worry = math.floor(worry / 3)
            if worry%monkey[2] == 0:
                change[monkey[3]].append(worry)
            else:
                change[monkey[4]].append(worry)
    counter = 0 
    for monkey in monkeys:
        monkey[0] = change[counter]
        counter+=1


inspections = []
for monkey in monkeys:
    inspections.append(monkey[-1])
inspections.sort()
print(inspections[-1]*inspections[-2])







#20294 too low

















































