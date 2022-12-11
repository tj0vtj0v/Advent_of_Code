class Day01:

    def __init__(self):
        print("Day 1 Part 1: " + self.solve_first_puzzle())
        print("Day 1 Part 2: " + self.solve_second_puzzle())

    def solve_first_puzzle(self) -> str:
        input_data = open("Day01_input.txt", "r")
        highest_proteins = 0
        recent_elve = 0
        for line in input_data:
            line = line.removesuffix("\n")
            if not line.isdigit():
                if recent_elve > highest_proteins:
                    highest_proteins = recent_elve
                    recent_elve = 0
                else:
                    recent_elve = 0
            else:
                recent_elve += int(line)
        return str(highest_proteins)

    def solve_second_puzzle(self) -> str:
        input_data = open("Day01_input.txt", "r")
        highest_proteins = [0, 0, 0]
        recent_elve = 0
        for line in input_data:
            line = line.removesuffix("\n")
            if not line.isdigit():
                if recent_elve > highest_proteins[0]:
                    highest_proteins[0] = recent_elve
                    highest_proteins.sort()
                    recent_elve = 0
                else:
                    recent_elve = 0
            else:
                recent_elve += int(line)
        return str(highest_proteins[0] + highest_proteins[1] + highest_proteins[2])
