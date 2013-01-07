class MineField:
    def __init__(self, size, grid):
        self.size = size
        rows, cols = size
        self.mines = {(r, c) for c in range(cols) for r in range(rows) if grid[r][c]}

    def hint(self):
        rows, cols = self.size
        return "\n".join(''.join(self.square_hint(r, c) for c in range(cols)) for r in range(rows))

    def square_hint(self, r, c):
        return '*' if (r, c) in self.mines else self.count_neighbours(r, c)

    def count_neighbours(self, r, c):
        neighbours = [(r - 1, c - 1), (r - 1, c + 0), (r - 1, c + 1),
                      (r + 0, c - 1),                 (r + 0, c + 1),
                      (r + 1, c - 1), (r + 1, c + 0), (r + 1, c + 1)]
        return str(sum(neighbour in self.mines for neighbour in neighbours))