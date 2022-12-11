class Day04:

    def __init__(self):
        print("Day 4 Part 1: " + self.solve_first_puzzle())
        print("Day 4 Part 2: " + self.solve_second_puzzle())

    def solve_first_puzzle(self) -> str:
        input_data = open("Day04_input.txt", "r")
        counter = 0
        for line in input_data:
            line = line.removesuffix("\n")
            elv1, elv2 = line.split(",")
            elv1_begin, elv1_end = elv1.split("-")
            elv2_begin, elv2_end = elv2.split("-")
            elv1_begin = int(elv1_begin)
            elv1_end = int(elv1_end)
            elv2_begin = int(elv2_begin)
            elv2_end = int(elv2_end)
            contain = False
            if elv1_begin >= elv2_begin and elv1_end <= elv2_end:
                contain = True
            if elv2_begin >= elv1_begin and elv2_end <= elv1_end:
                contain = True
            if contain:
                counter += 1
        return str(counter)

    def solve_second_puzzle(self) -> str:
        input_data = open("Day04_input.txt", "r")
        counter = 0
        for line in input_data:
            line = line.removesuffix("\n")
            elv1, elv2 = line.split(",")
            elv1_begin, elv1_end = elv1.split("-")
            elv2_begin, elv2_end = elv2.split("-")
            elv1_begin = int(elv1_begin)
            elv1_end = int(elv1_end)
            elv2_begin = int(elv2_begin)
            elv2_end = int(elv2_end)
            contain = False
            if elv1_begin in range(elv2_begin, elv2_end + 1) or elv2_begin in range(elv1_begin, elv1_end + 1) or elv1_end in range(elv2_begin, elv2_end + 1) or elv2_end in range(elv1_begin, elv1_end + 1):
                contain = True
            if contain:
                counter += 1

        return str(counter)
