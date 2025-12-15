class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __repr__(self):
        return f"Coordinate({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def path_to(self, other):
        path = [self]
        current = self
        while current != other:
            if current.x > other.x:
                new = Coordinate(current.x-1, current.y)
            elif current.x < other.x:
                new = Coordinate(current.x+1, current.y)
            elif current.y > other.y:
                new = Coordinate(current.x, current.y-1)
            elif current.y < other.y:
                new = Coordinate(current.x, current.y+1)
            else:
                raise ValueError("Shit hit the fan")

            path.append(new)
            current = new

        return path
