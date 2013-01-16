from range_classes import Range, FloatRange
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

    def test_can_create_float_range(self):
        r = FloatRange(0, 10)
        the_range = r.range
        expected = (0, 10)
        self.assertEqual(the_range, expected)

    def test_check_float_lies_in_float_range(self):
        r = FloatRange(0, 10)
        tau_in_range = r.in_range(6.28)
        twelve_point_five_in_range = r.in_range(12.5)
        self.assertTrue(tau_in_range)
        self.assertFalse(twelve_point_five_in_range)

    def test_check_range_limits_lie_in_float_range(self):
        r = FloatRange(3.14, 6.28)
        pi_in_range = r.in_range(3.14)
        tau_in_range = r.in_range(6.28)
        self.assertTrue(tau_in_range)
        self.assertTrue(pi_in_range)

    def test_intersection_of_empty_float_ranges(self):
        r1 = FloatRange()
        r2 = FloatRange()
        intersection = r1.intersection(r2)
        intersection2 = r2.intersection(r1)
        expected = None
        self.assertEqual(intersection.range, expected)
        self.assertEqual(intersection2.range, expected)

    def test_find_intersection_of_separate_float_ranges(self):
        r1 = FloatRange(0, 10)
        r2 = FloatRange(20, 30)
        intersection = r1.intersection(r2)
        intersection2 = r2.intersection(r1)
        expected = None
        self.assertEqual(intersection.range, expected)
        self.assertEqual(intersection2.range, expected)

    def test_find_intersection_of_overlapping_float_ranges(self):
        r1 = FloatRange(0, 10)
        r2 = FloatRange(5, 15)
        intersection = r1.intersection(r2)
        intersection2 = r2.intersection(r1)
        expected = (5, 10)
        self.assertEqual(intersection.range, expected)
        self.assertEqual(intersection2.range, expected)

    def test_find_intersection_of_float_ranges_one_inside_other(self):
        r1 = FloatRange(10, 40)
        r2 = FloatRange(20, 30)
        intersection = r1.intersection(r2)
        intersection2 = r2.intersection(r1)
        expected = (20, 30)
        self.assertEqual(intersection.range, expected)
        self.assertEqual(intersection2.range, expected)

    def test_find_intersection_of_identical_float_ranges(self):
        r1 = FloatRange(10, 20)
        r2 = FloatRange(10, 20)
        intersection = r1.intersection(r2)
        intersection2 = r2.intersection(r1)
        expected = (10, 20)
        self.assertEqual(intersection.range, expected)
        self.assertEqual(intersection2.range, expected)

    def test_find_intersection_of_just_touching_float_ranges(self):
        r1 = FloatRange(10, 20)
        r2 = FloatRange(20, 30)
        intersection = r1.intersection(r2)
        intersection2 = r2.intersection(r1)
        expected = (20, 20)
        self.assertEqual(intersection.range, expected)
        self.assertEqual(intersection2.range, expected)


if __name__ == '__main__':
    unittest.main()