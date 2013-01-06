import unittest
from number_names import Number


class Test(unittest.TestCase):
    def test_zero(self):
        number = Number(0)
        self.assertEqual(number.name(), 'zero')

    def test_one(self):
        number = Number(1)
        self.assertEqual(number.name(), 'one')

    def test_two(self):
        number = Number(2)
        self.assertEqual(number.name(), 'two')

    def test_three(self):
        number = Number(3)
        self.assertEqual(number.name(), 'three')

    def test_ten(self):
        number = Number(10)
        self.assertEqual(number.name(), 'ten')

    def test_thirteen(self):
        number = Number(13)
        self.assertEqual(number.name(), 'thirteen')

    def test_sixteen(self):
        number = Number(16)
        self.assertEqual(number.name(), 'sixteen')

    def test_twenty(self):
        number = Number(20)
        self.assertEqual(number.name(), 'twenty')

    def test_twenty_one(self):
        number = Number(21)
        self.assertEqual(number.name(), 'twenty one')

    def test_ninety_nine(self):
        number = Number(99)
        self.assertEqual(number.name(), 'ninety nine')

    def test_one_hundred(self):
        number = Number(100)
        self.assertEqual(number.name(), 'one hundred')

    def test_one_hundred_and_one(self):
        number = Number(101)
        self.assertEqual(number.name(), 'one hundred and one')

    def test_one_hundred_and_eleven(self):
        number = Number(111)
        self.assertEqual(number.name(), 'one hundred and eleven')

    def test_six_hundred_and_seventy_two(self):
        number = Number(672)
        self.assertEqual(number.name(), 'six hundred and seventy two')

    def test_nine_hundred_and_ninety_nine(self):
        number = Number(999)
        self.assertEqual(number.name(), 'nine hundred and ninety nine')

    def test_one_thousand(self):
        number = Number(1000)
        self.assertEqual(number.name(), 'one thousand')

    def test_one_thousand_and_one(self):
        number = Number(1001)
        self.assertEqual(number.name(), 'one thousand and one')

    def test_one_thousand_one_hundred_and_one(self):
        number = Number(1101)
        self.assertEqual(number.name(), 'one thousand, one hundred and one')

    def test_one_million_one_thousand(self):
        number = Number(1001000)
        self.assertEqual(number.name(), 'one million, one thousand')

    def test_one_million_one_thousand_and_twenty(self):
        number = Number(1001020)
        self.assertEqual(number.name(), 'one million, one thousand and twenty')

    def test_one_million_and_one(self):
        number = Number(1000001)
        self.assertEqual(number.name(), 'one million and one')

    def test_1234567890(self):
        number = Number(1234567890)
        self.assertEqual(number.name(), 'one billion, two hundred and thirty four million, five hundred and sixty seven thousand, eight hundred and ninety')

    def test_103030060090(self):
        number = Number(103030060090)
        self.assertEqual(number.name(), 'one hundred and three billion, thirty million, sixty thousand and ninety')

    def test_negative_one(self):
        number = Number(-1)
        self.assertEqual(number.name(), 'negative one')

    def test_negative_103030060090(self):
        number = Number(-103030060090)
        self.assertEqual(number.name(), 'negative one hundred and three billion, thirty million, sixty thousand and ninety')

    def test_three_point_one_four(self):
        number = Number(3.14)
        self.assertEqual(number.name(), 'three point one four')

    def test_negative_six_point_two_eight(self):
        number = Number(-6.28)
        self.assertEqual(number.name(), 'negative six point two eight')


if __name__ == '__main__':
    unittest.main()
