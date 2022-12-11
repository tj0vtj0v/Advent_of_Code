from Python.Day11_classes.Monkey import Monkey


class Day11:

    def __init__(self):
        print("Day 11 Part 1: " + self.solve_first_puzzle())

    def solve_first_puzzle(self) -> str:
        input_data = open("Day11_input.txt", "r")
        input_as_list = []
        for line in input_data:
            line = line.removesuffix("\n")
            input_as_list.append(line.strip())
        return self.create_monkeys(input_as_list)

    def create_monkeys(self, input_as_list: list) -> str:
        monkeys = []
        for line_index in range(len(input_as_list)):
            if input_as_list[line_index][:6] == "Monkey":
                monkeys.append(
                    Monkey(self.get_starting_items(input_as_list[line_index + 1]), input_as_list[line_index + 2][11:],
                           int(input_as_list[line_index + 3].split("by ")[1]), int(input_as_list[line_index + 4][-1]),
                           int(input_as_list[line_index + 5][-1])))
        return self.run_turns(monkeys)

    def get_starting_items(self, line: str) -> list:
        line = line.split(": ")[1]
        starting_items = line.split(", ")
        int_starting_items = []
        for element in starting_items:
            int_starting_items.append(int(element))
        return int_starting_items

    def run_turns(self, monkeys: list) -> str:
        for x in range(10000):
            for element in monkeys:
                element.do_turn(monkeys)
        return str(
            self.get_highest_monkey(monkeys) * self.get_highest_monkey(monkeys, self.get_highest_monkey(monkeys)))

    def get_highest_monkey(self, monkeys: list, ignore=0) -> int:
        highest_value = 0
        for element in monkeys:
            current_inspections = element.get_inspections()
            if current_inspections != ignore and current_inspections > highest_value:
                highest_value = current_inspections
        return highest_value
