from Day09.Coordinate import Coordinate
from DayTemplate import Day


class Day09(Day):
    def __init__(self):
        super().__init__(test=False)

        self.cords: list[Coordinate] = []
        self.wall: list[Coordinate] = []
        self.min_coordinate = Coordinate(9999999, 9999999)
        self.max_coordinate = Coordinate(0, 0)
        last: Coordinate = None
        for line in self.data:
            c = Coordinate(*[int(c) for c in line.split(",")])
            self.cords.append(c)

            self.min_coordinate.x = min(self.min_coordinate.x, c.x - 1)
            self.min_coordinate.y = min(self.min_coordinate.y, c.y - 1)
            self.max_coordinate.x = max(self.max_coordinate.x, c.x + 1)
            self.max_coordinate.y = max(self.max_coordinate.y, c.y + 1)

            if last is not None:
                self.wall += last.path_to(c)[:-1]
            last = c
        self.wall += last.path_to(self.cords[0])[:-1]

    def part1(self) -> str:
        maximum = 0
        for c1 in self.cords:
            for c2 in self.cords:
                if c1 == c2:
                    continue
                area = (abs(c1.x - c2.x) + 1) * (abs(c1.y - c2.y) + 1)
                if area > maximum:
                    maximum = area

        return str(maximum)
