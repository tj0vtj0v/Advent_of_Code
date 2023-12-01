import os
import math

inputfile = open(os.path.join(os.path.dirname(__file__), 'input_monkeys.txt'), "r")
inputtext = inputfile.readlines()

monkeys = []
monkey = []
for line in inputtext:
    line = line.removesuffix("\n")
    if "  Starting items: " in line:
        line = line.removeprefix("  Starting items: ")
        monkey.append(line.split(", "))
    elif "  Operation: new = " in line:
        line = line.removeprefix("  Operation: new = ")
        monkey.append(line)
    elif "  Test: divisible by " in line:
        line = line.removeprefix("  Test: divisible by ")
        monkey.append(line)
    elif "    If true: throw to monkey " in line:
        line = line.removeprefix("    If true: throw to monkey ")
        monkey.append(line)
    elif "    If false: throw to monkey " in line:
        line = line.removeprefix("    If false: throw to monkey ")
        monkey.append(line)
    elif line == "":
        monkey.append(0)
        monkeys.append(monkey)
        monkey = []
monkey.append(0)
monkeys.append(monkey)

for count in range(20):
    for monkey in monkeys:
        round = []
        for item in monkey[0]:
            monkey[5] += 1
            worry = int(item)
            worry = int(eval(monkey[1].replace("old", "worry")))

            worry = math.floor(worry / 3)
            if worry % int(monkey[2]) == 0:
                monkeys[int(monkey[3])][0].append(worry)
            else:
                monkeys[int(monkey[4])][0].append(worry)
        monkey[0] = []

inspection = []
for monkey in monkeys:
    inspection.append(monkey[5])
inspection.sort()
print("monkey business in 20 rounds: " + str(inspection[-1] * inspection[-2]))

for count in range(10000):
    for monkey in monkeys:
        round = []
        for item in monkey[0]:
            monkey[5] += 1
            worry = int(item)
            worry = int(eval(monkey[1].replace("old", "worry")))

            # worry = math.floor(worry/3)
            worry = worry % math.lcm(11, 5, 7, 2, 17, 13, 3, 19)
            if worry % int(monkey[2]) == 0:
                monkeys[int(monkey[3])][0].append(worry)
            else:
                monkeys[int(monkey[4])][0].append(worry)
        monkey[0] = []

inspection = []
for monkey in monkeys:
    inspection.append(monkey[5])
inspection.sort()
print("monkey business in 10000 rounds: " + str(inspection[-1] * inspection[-2]))
