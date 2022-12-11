from anytree import Node, RenderTree


class Day07:
    sum = 0
    sum_min = 0

    def __init__(self):
        day7_1 = self.solve_first_puzzle()
        print("Day 7 Part 1: " + day7_1[0])
        print("Day 7 Part 2: " + self.solve_second_puzzle(day7_1[1], day7_1[2]))

    def create_tree(self):
        input_data = open("Day07_input.txt", "r")
        first_directory = Node("Backslash", kwargs=["dir", "Backslash"])
        current_directory = first_directory
        current_directory_data = []
        for line in input_data:
            line = line.removesuffix("\n")
            if line[0] == "$":
                if len(current_directory_data) != 0:
                    for element in current_directory_data:
                        if element[0].isdigit():
                            Node(element[1], parent=current_directory, kwargs=["file", element[1], element[0]])
                        else:
                            Node(element[1], parent=current_directory, kwargs=["dir", element[1]])
                    current_directory_data = []
                if line[2:4] == "cd":
                    if line[5] == "/":
                        current_directory = first_directory
                    elif line[5:7] == "..":
                        current_directory = current_directory.parent
                    else:
                        for child in current_directory.children:
                            if child.kwargs[1] == line[5:]:
                                current_directory = child
            else:
                a, b = line.split(" ")
                current_directory_data.append([a, b])

        # for pre, fill, node in RenderTree(first_directory):
        #    print("%s%s" % (pre, node.name))

        current_directory = first_directory
        return current_directory

    def solve_first_puzzle(self) -> str:
        current_node = self.create_tree()
        system_size = self.rek_sum_nodes(current_node)
        return [str(Day07.sum), current_node, system_size]

    def rek_sum_nodes(self, current_directory):
        sum = 0
        for child in current_directory.children:
            if child.kwargs[0] == "file":
                sum += int(child.kwargs[2])
            else:
                sum += self.rek_sum_nodes(child)
        if sum < 100000:
            Day07.sum += sum
        return sum

    def solve_second_puzzle(self, current_node, system_size) -> str:
        system_size = 30000000 - (70000000 - system_size)
        self.rek_smallest_node(current_node, system_size)
        return str(Day07.sum_min)

    def rek_smallest_node(self, current_directory, system_size):
        sum = 0
        for child in current_directory.children:
            if child.kwargs[0] == "file":
                sum += int(child.kwargs[2])
            else:
                sum += self.rek_smallest_node(child, system_size)
        if sum > system_size:
            if Day07.sum_min > sum or Day07.sum_min == 0:
                Day07.sum_min = sum
        return sum
