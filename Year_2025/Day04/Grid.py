from DayTemplate import InputData


class Grid:
    grid: list[list[str]]

    def __init__(self, data: InputData):
        self.create_grid_from_input(data)

        self.rows = len(self.grid)
        self.columns = len(self.grid[0])

    def create_grid_from_input(self, data: InputData):
        self.grid = []
        for line in data:
            self.grid.append([x for x in line.strip()])

        return self.grid

    def get_neighbors(self, row: int, col: int):
        neighbors = []
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if r == row and c == col:
                    continue

                if 0 <= r < self.rows and 0 <= c < self.columns:
                    neighbors.append(self.grid[r][c])

        return neighbors

    def iterate_paper_removal(self):
        cells = self.get_cells_to_change()
        self.change_cells(cells)

        return len(cells)

    def get_cells_to_change(self):
        cells = []

        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row][col] == "@" and self.get_neighbors(row, col).count("@") < 4:
                    cells.append((row, col))

        return cells

    def change_cells(self, cells: list[tuple[int, int]]):
        for cell in cells:
            self[cell] = "x"


    def __setitem__(self, key: tuple[int, int], value):
        self.grid[key[0]][key[1]] = value

