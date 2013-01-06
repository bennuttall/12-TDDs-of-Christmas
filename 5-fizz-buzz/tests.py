from fizzbuzz import fizzbuzz, print_fizzbuzz
import unittest


class Test(unittest.TestCase):
    def test_multiple_of_neither_3_nor_5(self):
        self.assertEqual(fizzbuzz(1), '1')

    def test_another_multiple_of_neither_3_nor_5(self):
        self.assertEqual(fizzbuzz(2), '2')

    def test_multiple_of_3_not_5(self):
        self.assertEqual(fizzbuzz(3), 'fizz')

    def test_multiple_of_5_not_3(self):
        self.assertEqual(fizzbuzz(5), 'buzz')

    def test_multiple_of_both_3_and_5(self):
        self.assertEqual(fizzbuzz(15), 'fizzbuzz')

    def test_range_1_to_3(self):
        actual = print_fizzbuzz(1, 3)
        expected = "1\n2\nfizz"
        self.assertEqual(expected, actual)

    def test_range_1_to_16(self):
        actual = print_fizzbuzz(1, 16)
        expected = "1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz\n16"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()