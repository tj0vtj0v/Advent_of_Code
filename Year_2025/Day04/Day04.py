from Day04.Grid import Grid
from DayTemplate import Day


class Day04(Day):
    def __init__(self):
        super().__init__()
        self.solution_test_1 = 13
        self.solution_test_2 = 43

        self.grid = Grid(self.data)

    def solve(self) -> None:
        super().solve()

    def part1(self) -> str:
        return str(len(self.grid.get_cells_to_change()))

    def part2(self) -> str:
        total = 0
        removed = self.grid.iterate_paper_removal()

        while removed > 0:
            total += removed
            removed = self.grid.iterate_paper_removal()

        return str(total)
