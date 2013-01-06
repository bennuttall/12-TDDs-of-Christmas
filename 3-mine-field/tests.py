from mine_field import MineField
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        size = (3, 4)
        grid = [[1, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0]]
        self.minefield = MineField(size, grid)

    def test_process_input(self):
        self.assertIsInstance(self.minefield, MineField)

    def test_output(self):
        hint_grid = self.minefield.hint()
        expected = "*211\n12*1\n0111"
        self.assertEqual(hint_grid, expected)


if __name__ == '__main__':
    unittest.main()