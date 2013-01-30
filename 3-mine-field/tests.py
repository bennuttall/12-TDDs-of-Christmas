from mine_field import MineField
import unittest


class Test(unittest.TestCase):
    def test_reveal_empty_1x1_grid(self):
        grid = [[0]]
        minefield = MineField(grid)
        revealed_grid = minefield.reveal()
        expected = "0"
        self.assertEqual(revealed_grid, expected)

    def test_reveal_non_empty_1x1_grid(self):
        grid = [[1]]
        minefield = MineField(grid)
        revealed_grid = minefield.reveal()
        expected = "*"
        self.assertEqual(revealed_grid, expected)

    def test_reveal_empty_2x2_grid(self):
        grid = [[0, 0],
                [0, 0]]
        minefield = MineField(grid)
        revealed_grid = minefield.reveal()
        expected = "00\n00"
        self.assertEqual(revealed_grid, expected)

    def test_reveal_non_empty_2x2_grid(self):
        grid = [[1, 0],
                [0, 1]]
        minefield = MineField(grid)
        revealed_grid = minefield.reveal()
        expected = "*2\n2*"
        self.assertEqual(revealed_grid, expected)

    def test_reveal_3x4_grid(self):
        grid = [[1, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0]]
        minefield = MineField(grid)
        revealed_grid = minefield.reveal()
        expected = "*211\n12*1\n0111"
        self.assertEqual(revealed_grid, expected)


if __name__ == '__main__':
    unittest.main()