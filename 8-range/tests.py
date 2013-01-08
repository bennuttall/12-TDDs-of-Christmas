from range_class import Range
import unittest


class Test(unittest.TestCase):
    def test_can_create_range(self):
        r = Range(0, 10)
        the_range = r.range
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(the_range, expected)

    def test_check_integer_lies_in_range(self):
        r = Range(0, 10)
        two_in_range = r.in_range(2)
        twelve_in_range = r.in_range(12)
        self.assertTrue(two_in_range)
        self.assertFalse(twelve_in_range)

    def test_find_intersection_of_two_ranges(self):
        r1 = Range(0, 10)
        r2 = Range(6, 12)
        intersection = r1.intersection(r2)
        intersection2 = r2.intersection(r1)
        expected = [6, 7, 8, 9]
        self.assertEqual(intersection.range, expected)
        self.assertEqual(intersection2.range, expected)

    def test_find_empty_intersection_of_two_ranges(self):
        r1 = Range(0, 10)
        r2 = Range(20, 30)
        intersection = r1.intersection(r2)
        intersection2 = r2.intersection(r1)
        expected = []
        self.assertEqual(intersection.range, expected)
        self.assertEqual(intersection2.range, expected)


if __name__ == '__main__':
    unittest.main()