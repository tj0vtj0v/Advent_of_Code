from Day01.Dial import Dial
from DayTemplate import Day


class Day01(Day):
    def __init__(self):
        super().__init__()
        self.solution_test_1 = 3
        self.solution_test_2 = 6

        self.dial = Dial(50, 100)

    def solve(self) -> None:
        for action in self.data:
            if "L" in action:
                self.dial.turn_left(int(action.replace("L", "")))
            else:
                self.dial.turn_right(int(action.replace("R", "")))

        super().solve()

    def part1(self) -> str:
        return str(self.dial.password1)

    def part2(self) -> str:
        return str(self.dial.password2)
