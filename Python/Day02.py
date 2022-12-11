class Day02:

    def __init__(self):
        print("Day 1 Part 1: " + self.solve_first_puzzle())
        print("Day 1 Part 2: " + self.solve_second_puzzle())

    def solve_first_puzzle(self) -> str:
        input_data = open("Day02_input.txt", "r")
        score_item = 0
        score_win = 0
        for line in input_data:
            line = line.removesuffix("\n")
            if line[2] == "X":
                score_item += 1
            elif line[2] == "Y":
                score_item += 2
            elif line[2] == "Z":
                score_item += 3

            if line[0] == "A" and line[2] == "Y":
                score_win += 6
            elif line[0] == "B" and line[2] == "Z":
                score_win += 6
            elif line[0] == "C" and line[2] == "X":
                score_win += 6
            elif line[0] == "A" and line[2] == "X":
                score_win += 3
            elif line[0] == "B" and line[2] == "Y":
                score_win += 3
            elif line[0] == "C" and line[2] == "Z":
                score_win += 3

        return str(score_item + score_win)

    def solve_second_puzzle(self) -> str:
        input_data = open("Day02_input.txt", "r")
        score_win = 0
        score_item = 0
        for line in input_data:
            line = line.removesuffix("\n")
            if line[2] == "Y":
                score_win += 3
            elif line[2] == "Z":
                score_win += 6

            if line[2] == "Y":
                score_item += self.calculate_score(line[0])
            elif line[2] == "Z":
                if line[0] == "A":
                    score_win += 2
                elif line[0] == "B":
                    score_win += 3
                elif line[0] == "C":
                    score_win += 1
            elif line[2] == "X":
                if line[0] == "A":
                    score_win += 3
                elif line[0] == "B":
                    score_win += 1
                elif line[0] == "C":
                    score_win += 2

        return str(score_item + score_win)

    def calculate_score(self, input: str) -> int:
        if input == "A":
            return 1
        elif input == "B":
            return 2
        elif input == "C":
            return 3
