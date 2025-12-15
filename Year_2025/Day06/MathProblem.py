from DayTemplate import InputData


class MathProblem:
    def __init__(self, numbers: tuple[str], operator: str):
        self.numbers = numbers
        self.operator = operator

    def solve(self):
        return eval(self.operator.join(self.numbers))

    @staticmethod
    def convert_input_to_math_problem(data: InputData, invert=False) -> list["MathProblem"]:
        problems = []
        rows =  [r for r in data]
        current_data = ['' for _ in rows]
        current = ['' for _ in data]

        for i in range(max(len(x) for x in data)):
            for row_id, row in enumerate(rows):
                current[row_id] = row[i] if i < len(row) else ' '

            if len(set(current)) == 1 and current[0] == ' ':
                problems.append(MathProblem.to_problem(current_data, invert))
                current_data = ['' for _ in rows]
                continue


            for row_id, row in enumerate(rows):
                current_data[row_id] += row[i] if i < len(row) else ' '

        problems.append(MathProblem.to_problem(current_data, invert))

        return problems

    @staticmethod

    def to_problem(data, invert=False) -> "MathProblem":
        nums = tuple(data[:-1])
        if not invert:
            return MathProblem(nums, data[-1])

        t_nums = ['' for _ in range(len(nums[0]))]
        for id_row, row in enumerate(nums):
            for id_col, col in enumerate(row):
                t_nums[id_col] += col

        return MathProblem(tuple(t_nums), data[-1])
