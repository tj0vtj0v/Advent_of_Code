class Day09:

    def __init__(self):
        print("Day 9 Part 1: " + self.solve_first_puzzle())
        print("Day 9 Part 2: " + self.solve_second_puzzle())

    def solve_first_puzzle(self) -> str:
        input_data = open("Day09_input.txt", "r")
        visited = [[0, 0]]
        current_pos_T = [0, 0]
        current_pos_H = [0, 0]
        for line in input_data:
            line = line.removesuffix("\n")
            step = line.split(" ")
            for x in range(int(step[1])):
                next_pos_H = current_pos_H.copy()
                if step[0] == "R":
                    next_pos_H[0] += 1
                elif step[0] == "L":
                    next_pos_H[0] -= 1
                elif step[0] == "U":
                    next_pos_H[1] += 1
                elif step[0] == "D":
                    next_pos_H[1] -= 1

                if abs(next_pos_H[0] - current_pos_T[0]) > 1 or abs(next_pos_H[1] - current_pos_T[1]) > 1:
                    current_pos_T = current_pos_H
                    visited.append(current_pos_T)
                current_pos_H = next_pos_H

        done = []
        for element in visited:
            done.append(str(element[0]) + str(element[1]))
        return str(len(set(done)))

    def solve_second_puzzle(self) -> str:
        input_data = open("Day09_input.txt", "r")
        visited = [[0, 0]]
        current_pos = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        for line in input_data:
            line = line.removesuffix("\n")
            step = line.split(" ")
            for x in range(int(step[1])):
                if step[0] == "R":
                    current_pos[0][0] += 1
                elif step[0] == "L":
                    current_pos[0][0] -= 1
                elif step[0] == "U":
                    current_pos[0][1] += 1
                elif step[0] == "D":
                    current_pos[0][1] -= 1

                for index in range(1, len(current_pos)):
                    if current_pos[index - 1][0] - current_pos[index][0] == 2:
                        if current_pos[index - 1][1] > current_pos[index][1]:
                            current_pos[index][0] += 1
                            current_pos[index][1] += 1
                        elif current_pos[index - 1][1] < current_pos[index][1]:
                            current_pos[index][0] += 1
                            current_pos[index][1] -= 1
                        else:
                            current_pos[index][0] += 1

                    elif current_pos[index - 1][0] - current_pos[index][0] == -2:
                        if current_pos[index - 1][1] > current_pos[index][1]:
                            current_pos[index][0] -= 1
                            current_pos[index][1] += 1
                        elif current_pos[index - 1][1] < current_pos[index][1]:
                            current_pos[index][0] -= 1
                            current_pos[index][1] -= 1
                        else:
                            current_pos[index][0] -= 1

                    elif current_pos[index - 1][1] - current_pos[index][1] == 2:
                        if current_pos[index - 1][0] > current_pos[index][0]:
                            current_pos[index][0] += 1
                            current_pos[index][1] += 1
                        elif current_pos[index - 1][0] < current_pos[index][0]:
                            current_pos[index][0] -= 1
                            current_pos[index][1] += 1
                        else:
                            current_pos[index][1] += 1

                    elif current_pos[index - 1][1] - current_pos[index][1] == -2:
                        if current_pos[index - 1][0] > current_pos[index][0]:
                            current_pos[index][0] += 1
                            current_pos[index][1] -= 1
                        elif current_pos[index - 1][0] < current_pos[index][0]:
                            current_pos[index][0] -= 1
                            current_pos[index][1] -= 1
                        else:
                            current_pos[index][1] -= 1

                    if index == len(current_pos) - 1:
                        visited.append(current_pos[index].copy())

        done = []
        for element in visited:
            done.append(str(element[0]) + str(element[1]))
        return str(len(set(done)))
