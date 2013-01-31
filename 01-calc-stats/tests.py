import unittest
from calc_stats import CalcStats


class Test(unittest.TestCase):
    def test_minimum(self):
        values = [6, 9, 15, -2, 92, 11]
        calc = CalcStats(values)
        minimum = calc.min()
        self.assertEqual(minimum, -2)

    def test_maximum(self):
        values = [6, 9, 15, -2, 92, 11]
        calc = CalcStats(values)
        maximum = calc.max()
        self.assertEqual(maximum, 92)

    def test_length(self):
        values = [6, 9, 15, -2, 92, 11]
        calc = CalcStats(values)
        length = calc.len()
        self.assertEqual(length, 6)

    def test_average(self):
        values = [6, 9, 15, -2, 92, 11]
        calc = CalcStats(values)
        average = calc.ave()
        self.assertEqual(average, 21.833333)


if __name__ == '__main__':
    unittest.main()