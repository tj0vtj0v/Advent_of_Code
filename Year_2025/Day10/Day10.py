import re

from Day10.Machine import Machine
from DayTemplate import Day


class Day10(Day):
    def __init__(self):
        super().__init__(test=False)

        self.machines = []

        for line in self.data:
            lamps = line.split(' ')[0].strip("[]")
            buttons = re.findall(r"\(([^)]+)\)", line)
            weights = line.split('{')[1].strip("{}")

            machine = Machine(lamps, weights)
            for button in buttons:
                machine.add_button(button)

            self.machines.append(machine)

    def part1(self) -> str:
        return str(sum(m.min_switches() for m in self.machines))


