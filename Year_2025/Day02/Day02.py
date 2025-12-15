from Day02.Range import Range
from DayTemplate import Day


class Day02 (Day):
    def __init__(self):
        super().__init__(",")
        self.solution_test_1 = 1227775554
        self.solution_test_2 = 4174379265

    def solve(self) -> None:
        super().solve()

    def part1(self) -> str:
        count = sum(Range(x).count_repeating_twice_ids() for x in self.data)

        return str(count)

    def part2(self) -> str:
        count = sum(Range(x).count_repeating_ids() for x in self.data)

        return str(count)