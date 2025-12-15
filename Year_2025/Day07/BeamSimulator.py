from DayTemplate import InputData


class BeamSimulator:
    def __init__(self, data: InputData):
        self.splitter = []
        for row in data:
            self.splitter.append([i for i, char in enumerate(row) if char == '^'])

        self.field_size = len(data[0])

        self.rays = {i: 0 for i in range(self.field_size)}

        self.start_ray = data[0].find("S")
        self.rays[self.start_ray] = 1

        self.splits = 0

    def simulate_row(self, row_index):
        new_rays = {i: 0 for i in range(self.field_size)}
        for ray, amount in self.rays.items():
            if ray in self.splitter[row_index]:
                new_rays[ray - 1] += amount
                new_rays[ray + 1] += amount
                if amount > 0:
                    self.splits += 1
            else:
                new_rays[ray] += amount

        self.rays = new_rays

    def simulate(self):
        for row_index in range(len(self.splitter)):
            self.simulate_row(row_index)
