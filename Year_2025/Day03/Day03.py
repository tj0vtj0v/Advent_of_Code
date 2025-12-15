from DayTemplate import Day


class Day03(Day):
    def __init__(self):
        super().__init__()
        self.solution_test_1 = 357
        self.solution_test_2 = 3121910778619

    def solve(self) -> None:
        super().solve()

    def part1(self) -> str:
        return str(sum(int(get_highest_substring(bank, 2)) for bank in self.data))

    def part2(self) -> str:
        return str(sum(int(get_highest_substring(bank, 12)) for bank in self.data))


def get_highest_substring(string_to_choose_from: str, num_to_choose: int) -> str:
    # break condition
    assert num_to_choose <= len(string_to_choose_from)
    if num_to_choose == 0:
        return ''
    if len(string_to_choose_from) == num_to_choose:
        return string_to_choose_from

    # recursive step
    get_highest_from = string_to_choose_from[:-(num_to_choose - 1)] if num_to_choose > 1 else string_to_choose_from
    maximum = max([int(x) for x in get_highest_from])
    max_ind = get_highest_from.find(str(maximum))

    # recursive call
    return string_to_choose_from[max_ind] + get_highest_substring(string_to_choose_from[max_ind + 1:], num_to_choose - 1)
