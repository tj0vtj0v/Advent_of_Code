from Day06.MathProblem import MathProblem
from DayTemplate import Day


class Day06(Day):
    def __init__(self):
        super().__init__()


    def part1(self) -> str:
        problems = MathProblem.convert_input_to_math_problem(self.data)
        return str(sum(problem.solve() for problem in problems))


    def part2(self) -> str:
        problems = MathProblem.convert_input_to_math_problem(self.data, True)
        return str(sum(problem.solve() for problem in problems))