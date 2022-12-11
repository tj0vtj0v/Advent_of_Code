class Day06:

    def __init__(self):
        print("Day 6 Part 1: " + self.solve_first_puzzle())
        print("Day 6 Part 2: " + self.solve_second_puzzle())

    def solve_first_puzzle(self) -> str:
        input_data = open("Day06_input.txt", "r")
        input = input_data.read()
        for index in range(len(input)):
            temp = []
            temp.append(input[index])
            temp.append(input[index + 1])
            temp.append(input[index + 2])
            temp.append(input[index + 3])
            temp = set(temp)
            temp = list(temp)
            if len(temp) == 4:
                return str(index+4)

    def solve_second_puzzle(self) -> str:
        input_data = open("Day06_input.txt", "r")
        input = input_data.read()
        for index in range(len(input)):
            temp = []
            for x in range(14):
                temp.append(input[index + x])
            temp = set(temp)
            temp = list(temp)
            if len(temp) == 14:
                return str(index + 14)
