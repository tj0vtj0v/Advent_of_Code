class Dial:
    def __init__(self, start_position: int = 0, length: int = 10):
        self.position = start_position % length
        self.length = length

        self.password1 = 0
        self.password2 = 0

    def turn_left(self, positions: int) -> None:
        visited_positions = self.generate_positions(-positions-1, -1)
        self.position = visited_positions[-1]

        self.password2 += visited_positions.count(0)
        if self.position == 0:
            self.password1 += 1

    def turn_right(self, positions: int) -> None:
        visited_positions = self.generate_positions(positions+1)
        self.position = visited_positions[-1]

        self.password2 += visited_positions.count(0)
        if self.position == 0:
            self.password1 += 1 # 6211 < x < 7282

    def generate_positions(self, delta: int, increment: int = 1) -> list[int]:
        return [x % self.length for x in range(self.position, self.position + delta, increment)][1:]
