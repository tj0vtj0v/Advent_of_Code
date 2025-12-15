class Machine:
    def __init__(self, lamps: str, weights: str):
        self.target = [char == '#' for char in lamps]
        self.weight = [int(w) for w in weights.split(',')]

        self.buttons = []

    def add_button(self, button: str):
        self.buttons.append([int(b) for b in button.split(',')])

    def press_button_on(self, lamps: list[bool], button_id: int):
        for lamp in self.buttons[button_id]:
            lamps[lamp] = not lamps[lamp]

        return lamps

    def min_switches(self):
        frontier = [([False for _ in self.target], 0)]

        while frontier:
            state, steps = frontier.pop(0)
            if state == self.target:
                return steps
            for button_id in range(len(self.buttons)):
                frontier.append((self.press_button_on(state.copy(), button_id), steps + 1))


        raise Exception("No solution found")
