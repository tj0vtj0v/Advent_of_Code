from math import hypot


class Position:
    def __init__(self, pos_str):
        self.x, self.y, self.z = [int(x) for x in pos_str.split(",")]

    def distance(self, other):
        return hypot(self.x - other.x, self.y - other.y, self.z - other.z)

