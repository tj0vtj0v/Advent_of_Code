class InputData:
    lines: list[str]

    def __init__(self):
        self.lines = []

    def __iter__(self):
        return iter(self.lines)

    def __len__(self):
        return len(self.lines)

    def __getitem__(self, index):
        return self.lines[index]

    def get_items_from_input(self, seperating_line=''):
        items = []
        item = InputData()
        for line in self:
            if line.strip() != seperating_line:
                item.lines.append(line)
            else:
                items.append(item)
                item = InputData()
        items.append(item)

        return items


class Day:
    def __init__(self, separator=None, test=False):
        self.separator = separator
        self.test = test
        self.data = self.read_input(self.separator)

    def solve(self) -> None:
        self.data = self.read_input(self.separator)

        part1_answer = self.part1()
        part2_answer = self.part2()

        self.print_answer(part1_answer, part2_answer)

    def part1(self) -> str:
        return "Not solved yet."

    def part2(self) -> str:
        return "Not solved yet."

    def read_input(self, separator=None) -> InputData:
        input_data = InputData()

        directory = 'tests' if self.test else 'inputs'
        for line in open(f"{directory}/{self.__class__.__name__}.txt".lower()):
            if separator is None or separator not in line:
                input_data.lines.append(line.removesuffix("\n"))
            else:
                for x in line.removesuffix("\n").split(separator):
                    input_data.lines.append(x)

        return input_data

    def print_answer(self, part1: str, part2: str) -> None:
        print((
            f"""
Solutions for {self.__class__.__name__}:
Part 1:
\t{part1}
Part 2:
\t{part2}

"""))
