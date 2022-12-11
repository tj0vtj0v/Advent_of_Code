class Day05:

    def __init__(self):
        print("Day 5 Part 1: " + self.solve_first_puzzle())
        print("Day 5 Part 2: " + self.solve_second_puzzle())

    def solve_first_puzzle(self) -> str:
        warehouse = self.create_ware()
        input_data = open("Day05_input.txt", "r")
        for line in input_data:
            line = line.removesuffix("\n")
            if len(line) != 0:
                if line[0] != "[" and line[0] != " ":
                    amount = int(line[line.find("move") + 5:line.find("from") - 1])
                    source = int(line[line.find("from") + 5:line.find("to") - 1])
                    destination = int(line[line.find("to") + 3:])
                    for x in range(amount):
                        warehouse[destination - 1].append(warehouse[source - 1].pop())
        temp = []
        for x in warehouse:
            temp.append(x[-1])
        return str(temp)

    def solve_second_puzzle(self) -> str:
        warehouse = self.create_ware()
        input_data = open("Day05_input.txt", "r")
        for line in input_data:
            line = line.removesuffix("\n")
            if len(line) != 0:
                if line[0] != "[" and line[0] != " ":
                    amount = int(line[line.find("move") + 5:line.find("from") - 1])
                    source = int(line[line.find("from") + 5:line.find("to") - 1])
                    destination = int(line[line.find("to") + 3:])
                    for x in range(-amount, 0):
                        warehouse[destination - 1].append(warehouse[source - 1][x])
                    for y in range(amount):
                        warehouse[source - 1].pop()
        temp = []
        for x in warehouse:
            temp.append(x[-1])
        return str(temp)

    def create_ware(self) -> list:
        warehouse = [[], [], [], [], [], [], [], [], []]
        input_data = open("Day05_input.txt", "r")
        for line in input_data:
            if line[0] == "[":
                if line[0] == "[":
                    warehouse[0].insert(0, line[1])
                if line[4] == "[":
                    warehouse[1].insert(0, line[5])
                if line[8] == "[":
                    warehouse[2].insert(0, line[9])
                if line[12] == "[":
                    warehouse[3].insert(0, line[13])
                if line[16] == "[":
                    warehouse[4].insert(0, line[17])
                if line[20] == "[":
                    warehouse[5].insert(0, line[21])
                if line[24] == "[":
                    warehouse[6].insert(0, line[25])
                if line[28] == "[":
                    warehouse[7].insert(0, line[29])
                if len(line) > 32:
                    if line[32] == "[":
                        warehouse[8].insert(0, line[33])
        return warehouse
