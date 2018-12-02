from itertools import product

class Minefield:
    def __init__(self, mf):
        self.minefield = mf

    def __str__(self):
        s = '\n'
        for row in self.hint:
            for cell in row:
                s += cell
            s += '\n'
        return s

    @property
    def minefield(self):
        return self._mf

    @minefield.setter
    def minefield(self, inp):
        rows = inp.split('\n')[2:-1]  # ignore metadata row and empty last row
        self._mf = [[c == '*' for c in row] for row in rows]

    @property
    def width(self):
        return len(self.minefield[0])

    @property
    def height(self):
        return len(self.minefield)

    @property
    def hint(self):
        return [
            [self._count_neighbors(x, y)
            for x in range(self.width)]
            for y in range(self.height)
        ]

    def _count_neighbors(self, x, y):
        if self.minefield[y][x]:
            return '*'
        deltas = set(product([-1, 0, 1], repeat=2)) - set([(0, 0)])
        neighbors = [(x + dx, y + dy)
                    for (dx, dy) in deltas
                    if self._validate(x+dx, y+dy)
        ]
        return str(sum(self.minefield[y][x] for x, y in neighbors))

    def _validate(self, x, y):
        return x in range(self.width) and y in range(self.height)
