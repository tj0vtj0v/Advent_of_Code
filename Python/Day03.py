class Day03:

    def __init__(self):
        print("Day 3 Part 1: " + self.solve_first_puzzle())
        print("Day 3 Part 2: " + self.solve_second_puzzle())

    def solve_first_puzzle(self) -> str:
        input_data = open("Day03_input.txt", "r")
        values = {}
        prio = 0
        for v in range(1, 27):
            values[chr(v + 96)] = v
        for v in range(27, 53):
            values[chr(v+38)] = v
        for line in input_data:
            line = line.removesuffix("\n")
            start_second_half = int(len(line) / 2)
            done = []
            for x in line[:start_second_half]:
                for y in line[start_second_half:]:
                    if x in done:
                        break
                    elif x == y:
                        prio += values.get(x)
                        done.append(x)
                        break
        return str(prio)

    def solve_second_puzzle(self) -> str:
        input_data = open("Day03_input.txt", "r")
        group = []
        values = {}
        prio = 0
        done = False
        for v in range(1, 27):
            values[chr(v + 96)] = v
        for v in range(27, 53):
            values[chr(v+38)] = v
        for line in input_data:
            line = line.removesuffix("\n")
            group.append(line)
            if len(group) == 3:
                for x in group[0]:
                    for y in group[1]:
                        if x == y and not done:
                            for z in group[2]:
                                if x == z:
                                    prio += values.get(x)
                                    done = True
                                    break
                group = []
                done = False
        return str(prio)
