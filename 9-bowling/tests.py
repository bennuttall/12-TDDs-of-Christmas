from bowling import *
import unittest


class Test(unittest.TestCase):
    def test_point_str_to_int(self):
        score_miss = point_str_to_int('-')
        self.assertEqual(score_miss, 0)

        score_one = point_str_to_int('1')
        self.assertEqual(score_one, 1)

        score_five = point_str_to_int('5')
        self.assertEqual(score_five, 5)

        score_strike = point_str_to_int('X')
        self.assertEqual(score_strike, 10)

    def test_frame_score(self):
        miss_miss = ('-', '-')
        frame_score_1 = frame_score(miss_miss)
        expected_1 = (0, 0)
        self.assertEqual(frame_score_1, expected_1)

        miss_one = ('-', '1')
        frame_score_2 = frame_score(miss_one)
        expected_2 = (0, 1)
        self.assertEqual(frame_score_2, expected_2)

        four_five = ('4', '5')
        frame_score_3 = frame_score(four_five)
        expected_3 = (4, 5)
        self.assertEqual(frame_score_3, expected_3)

        four_spare = ('4', '/')
        frame_score_4 = frame_score(four_spare)
        expected_4 = (4, 6)
        self.assertEqual(frame_score_4, expected_4)

    def test_frame_score_to_scoring_tuple(self):
        zero_zero = (0, 0)
        score_1 = frame_score_to_scoring_tuple(zero_zero)
        expected_1 = (0, 0)
        self.assertEqual(score_1, expected_1)

        one_one = (1, 1)
        score_2 = frame_score_to_scoring_tuple(one_one)
        expected_2 = (2, 0)
        self.assertEqual(score_2, expected_2)

        two_three = (2, 3)
        score_3 = frame_score_to_scoring_tuple(two_three)
        expected_3 = (5, 0)
        self.assertEqual(score_3, expected_3)

        four_six = (4, 6)
        score_4 = frame_score_to_scoring_tuple(four_six)
        expected_4 = (10, 1)
        self.assertEqual(score_4, expected_4)

        strike = (10, 0)
        score_5 = frame_score_to_scoring_tuple(strike)
        expected_5 = (10, 2)
        self.assertEqual(score_5, expected_5)

    def test_all_misses_score_is_zero(self):
        frames = '--|--|--|--|--|--|--|--|--|--'
        score = get_score(frames)
        expected_score = 0
        self.assertEqual(score, expected_score)

    def test_all_frames_under_ten_score_is_sum(self):
        frames = '11|22|33|44|5-|-5|44|33|22|11'
        score = get_score(frames)
        expected_score = 50
        self.assertEqual(score, expected_score)

    def test_all_9s_no_spares_score_is_90(self):
        frames = '9-|9-|9-|9-|9-|9-|9-|9-|9-|9-'
        score = get_score(frames)
        expected_score = 90
        self.assertEqual(score, expected_score)

    def test_all_5s_with_spares_score_is_150(self):
        frames = '5/|5/|5/|5/|5/|5/|5/|5/|5/|5/|5'
        score = get_score(frames)
        expected_score = 150
        self.assertEqual(score, expected_score)

    def test_all_strikes_score_is_300(self):
        frames = 'X|X|X|X|X|X|X|X|X|X|X|X'
        score = get_score(frames)
        expected_score = 300
        self.assertEqual(score, expected_score)

    def test_uncle_bob_example(self):
        frames = '14|45|6/|5/|X|-1|7/|6/|X|2/|6'
        score = get_score(frames)
        expected_score = 133
        self.assertEqual(score, expected_score)


if __name__ == '__main__':
    unittest.main()