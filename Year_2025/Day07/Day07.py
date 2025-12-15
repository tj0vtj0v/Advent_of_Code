from Day07.BeamSimulator import BeamSimulator
from DayTemplate import Day


class Day07(Day):
    def __init__(self):
        super().__init__()

        self.beam_simulator = BeamSimulator(self.data)
        self.beam_simulator.simulate()

    def part1(self) -> str:
        return str(self.beam_simulator.splits)

    def part2(self) -> str:
        return str(sum(self.beam_simulator.rays.values()))
