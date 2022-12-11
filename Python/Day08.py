class Day08:

    def __init__(self):
        print("Day 8 Part 1: " + self.solve_first_puzzle())
        print("Day 8 Part 2: " + self.solve_second_puzzle())

    def solve_first_puzzle(self) -> str:
        file = open("Day08_input.txt", "r")
        forest = []
        not_seen_trees = 0
        for line in file:
            line = line.removesuffix("\n")
            forest.append([])
            for char in line:
                forest[-1].append(int(char))
        for index_y in range(len(forest)):
            for index_x in range(len(forest[index_y])):
                if not index_x == 0 and not index_y == 0 and not index_x == len(
                        forest[index_y]) - 1 and not index_y == len(forest) - 1:
                    current_height = forest[index_y][index_x]
                    visible = [True, True, True, True]
                    for current_index_x in range(len(forest[0])):
                        if current_index_x < index_x:
                            if forest[index_y][current_index_x] >= current_height:
                                visible[0] = False
                        if current_index_x > index_x:
                            if forest[index_y][current_index_x] >= current_height:
                                visible[1] = False
                    for current_index_y in range(len(forest)):
                        if current_index_y < index_y:
                            if forest[current_index_y][index_x] >= current_height:
                                visible[2] = False
                        if current_index_y > index_y:
                            if forest[current_index_y][index_x] >= current_height:
                                visible[3] = False
                    if True not in visible:
                        not_seen_trees += 1
        return str((len(forest[0]) * len(forest)) - not_seen_trees)

    def solve_second_puzzle(self) -> str:
        file = open("Day08_input.txt", "r")
        forest = []
        highest_score = 0
        for line in file:
            line = line.removesuffix("\n")
            forest.append([])
            for char in line:
                forest[-1].append(int(char))
        for index_y in range(len(forest)):
            for index_x in range(len(forest[index_y])):
                temp = [0, 0, 0, 0]

                counter = 0
                try:
                    next_tree_r = [forest[index_y][index_x + 1], index_x + 1]
                    while True:
                        if next_tree_r[1] < 0:
                            temp[0] = counter
                            break
                        counter += 1
                        if next_tree_r[0] >= forest[index_y][index_x]:
                            temp[0] = counter
                            break
                        next_tree_r = [forest[index_y][next_tree_r[1] + 1], next_tree_r[1] + 1]
                except IndexError:
                    temp[0] = counter

                try:
                    counter = 0
                    next_tree_l = [forest[index_y][index_x - 1], index_x - 1]
                    while True:
                        if next_tree_l[1] < 0:
                            temp[1] = counter
                            break
                        counter += 1
                        if next_tree_l[0] >= forest[index_y][index_x]:
                            temp[1] = counter
                            break
                        next_tree_l = [forest[index_y][next_tree_l[1] - 1], next_tree_l[1] - 1]
                except IndexError:
                    temp[1] = counter

                try:
                    counter = 0
                    next_tree_o = [forest[index_y - 1][index_x], index_y - 1]
                    while True:
                        if next_tree_o[1] < 0:
                            temp[2] = counter
                            break
                        counter += 1
                        if next_tree_o[0] >= forest[index_y][index_x]:
                            temp[2] = counter
                            break
                        next_tree_o = [forest[next_tree_o[1] - 1][index_x], next_tree_o[1] - 1]
                except IndexError:
                    temp[2] = counter

                try:
                    counter = 0
                    next_tree_u = [forest[index_y + 1][index_x], index_y + 1]
                    while True:
                        if next_tree_u[1] < 0:
                            temp[3] = counter
                            break
                        counter += 1
                        if next_tree_u[0] >= forest[index_y][index_x]:
                            temp[3] = counter
                            break
                        next_tree_u = [forest[next_tree_u[1] + 1][index_x], next_tree_u[1] + 1]
                except IndexError:
                    temp[3] = counter

                erg = temp[0] * temp[1] * temp[2] * temp[3]
                if erg > highest_score:
                    highest_score = erg

        return str(highest_score)
