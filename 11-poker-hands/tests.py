from card import Card
from poker_hand import PokerHand
from poker_game import PokerGame
import unittest


class Test(unittest.TestCase):
    def test_can_create_card(self):
        card_1 = Card(value='A', suit='S')
        self.assertIsInstance(card_1, Card)

    def test_can_create_genuine_cards(self):
        card_1 = Card(value='2', suit='S')
        self.assertIsInstance(card_1, Card)
        card_2 = Card(value='3', suit='H')
        self.assertIsInstance(card_2, Card)
        card_3 = Card(value='5', suit='C')
        self.assertIsInstance(card_3, Card)
        card_4 = Card(value='9', suit='D')
        self.assertIsInstance(card_4, Card)
        card_5 = Card(value='J', suit='S')
        self.assertIsInstance(card_5, Card)

    def test_cannot_create_invalid_cards(self):
        with self.assertRaises(Card.InvalidCardError):
            card_1 = Card(value='1', suit='S')
        with self.assertRaises(Card.InvalidCardError):
            card_2 = Card(value='3', suit='A')
        with self.assertRaises(Card.InvalidCardError):
            card_3 = Card(value='5', suit='B')
        with self.assertRaises(Card.InvalidCardError):
            card_4 = Card(value='99', suit='D')
        with self.assertRaises(Card.InvalidCardError):
            card_5 = Card(value='Z', suit='Z')

    def test_can_create_poker_hand_from_five_given_cards(self):
        card_1 = Card(value='A', suit='S')
        card_2 = Card(value='2', suit='H')
        card_3 = Card(value='3', suit='C')
        card_4 = Card(value='Q', suit='D')
        card_5 = Card(value='K', suit='S')

        cards = (card_1, card_2, card_3, card_4, card_5)
        hand_1 = PokerHand(cards)
        self.assertIsInstance(hand_1, PokerHand)

    def test_can_only_create_hand_of_card_objects(self):
        with self.assertRaises(PokerHand.InvalidHandError):
            hand_1 = PokerHand('AH')

        cards = ('TS', '5H', '4C', 'JD', '9H')
        with self.assertRaises(PokerHand.InvalidHandError):
            hand_2 = PokerHand(cards)

        card_1 = Card(value='2', suit='H')
        card_2 = Card(value='3', suit='C')
        card_3 = Card(value='Q', suit='D')
        card_4 = Card(value='K', suit='S')
        card_5 = 'AS'

        cards = (card_1, card_2, card_3, card_4, card_5)
        with self.assertRaises(PokerHand.InvalidHandError):
            hand_3 = PokerHand(cards)

    def test_cannot_have_duplicate_cards_in_deck(self):
        card_1 = Card(value='2', suit='H')
        card_2 = Card(value='3', suit='C')
        card_3 = Card(value='Q', suit='D')
        card_4 = Card(value='K', suit='S')
        card_5 = Card(value='3', suit='C')
        cards = (card_1, card_2, card_3, card_4, card_5)

        with self.assertRaises(PokerHand.InvalidHandError):
            hand = PokerHand(cards)

    def test_poker_hand_must_be_exactly_five_cards(self):
        card_1 = Card(value='2', suit='H')
        card_2 = Card(value='3', suit='C')
        card_3 = Card(value='Q', suit='D')
        card_4 = Card(value='K', suit='S')
        card_5 = Card(value='T', suit='C')
        card_6 = Card(value='A', suit='H')
        cards_1 = (card_1,)

        with self.assertRaises(PokerHand.InvalidHandError):
            hand_1 = PokerHand(cards_1)

        cards_2 = (card_1, card_2, card_3, card_4)

        with self.assertRaises(PokerHand.InvalidHandError):
            hand_2 = PokerHand(cards_2)

        cards_3 = (card_1, card_2, card_3, card_4, card_5, card_6)

        with self.assertRaises(PokerHand.InvalidHandError):
            hand_3 = PokerHand(cards_3)

    def test_can_show_card(self):
        card_1 = Card(value='A', suit='S')
        expected_card = 'AS'
        self.assertEqual(repr(card_1), expected_card)

    def test_poker_hand_can_show_hand(self):
        card_1 = Card(value='A', suit='S')
        card_2 = Card(value='2', suit='H')
        card_3 = Card(value='3', suit='C')
        card_4 = Card(value='Q', suit='D')
        card_5 = Card(value='K', suit='S')

        cards = (card_1, card_2, card_3, card_4, card_5)
        hand = PokerHand(cards)
        actual_cards = hand.show()
        expected_cards = ['AS', '2H', '3C', 'QD', 'KS']
        all_cards_expected = all(card in expected_cards for card in actual_cards)
        self.assertTrue(all_cards_expected)
        self.assertEqual(len(actual_cards), 5)

    def test_can_determine_card_value_index(self):
        card_1 = Card(value='A', suit='S')
        value_index_1 = card_1.value_index
        expected_index_1 = 12
        self.assertEqual(value_index_1, expected_index_1)

        card_2 = Card(value='5', suit='H')
        value_index_2 = card_2.value_index
        expected_index_2 = 3
        self.assertEqual(value_index_2, expected_index_2)

        card_3 = Card(value='J', suit='D')
        value_index_3 = card_3.value_index
        expected_index_3 = 9
        self.assertEqual(value_index_3, expected_index_3)

    def test_can_determine_high_card_from_hand(self):
        card_1 = Card(value='A', suit='S')
        card_2 = Card(value='2', suit='H')
        card_3 = Card(value='4', suit='C')
        card_4 = Card(value='6', suit='D')
        card_5 = Card(value='7', suit='S')

        cards = (card_1, card_2, card_3, card_4, card_5)
        hand_1 = PokerHand(cards)
        actual_rank_1 = hand_1.rank()
        expected_rank_1 = ('High Card', 'A')
        self.assertEqual(actual_rank_1, expected_rank_1)

        card_6 = Card(value='J', suit='H')
        card_7 = Card(value='8', suit='C')
        card_8 = Card(value='T', suit='D')
        card_9 = Card(value='K', suit='D')
        card_10 = Card(value='3', suit='S')

        cards_2 = (card_6, card_7, card_8, card_9, card_10)
        hand_2 = PokerHand(cards_2)
        actual_rank_2 = hand_2.rank()
        expected_rank_2 = ('High Card', 'K')
        self.assertEqual(actual_rank_2, expected_rank_2)

    def test_can_determine_pair_from_hand(self):
        card_1 = Card(value='A', suit='S')
        card_2 = Card(value='2', suit='H')
        card_3 = Card(value='4', suit='C')
        card_4 = Card(value='2', suit='D')
        card_5 = Card(value='7', suit='S')

        cards_1 = (card_1, card_2, card_3, card_4, card_5)
        hand_1 = PokerHand(cards_1)
        actual_rank_1 = hand_1.rank()
        expected_rank_1 = ('Pair', '2')
        self.assertEqual(actual_rank_1, expected_rank_1)

        card_6 = Card(value='T', suit='C')
        card_7 = Card(value='3', suit='C')
        card_8 = Card(value='8', suit='H')
        card_9 = Card(value='T', suit='H')
        card_10 = Card(value='K', suit='D')

        cards_2 = (card_6, card_7, card_8, card_9, card_10)
        hand_2 = PokerHand(cards_2)
        actual_rank_2 = hand_2.rank()
        expected_rank_2 = ('Pair', 'T')
        self.assertEqual(actual_rank_2, expected_rank_2)

    def test_can_determine_two_pair_from_hand(self):
        card_1 = Card(value='A', suit='S')
        card_2 = Card(value='A', suit='H')
        card_3 = Card(value='4', suit='C')
        card_4 = Card(value='4', suit='D')
        card_5 = Card(value='7', suit='S')

        cards_1 = (card_1, card_2, card_3, card_4, card_5)
        hand_1 = PokerHand(cards_1)
        actual_rank_1 = hand_1.rank()
        expected_rank_1 = ('Two Pairs', ('A', '4'))
        self.assertEqual(actual_rank_1, expected_rank_1)

        card_6 = Card(value='7', suit='H')
        card_7 = Card(value='J', suit='S')
        card_8 = Card(value='7', suit='C')
        card_9 = Card(value='T', suit='D')
        card_10 = Card(value='J', suit='C')

        cards_2 = (card_6, card_7, card_8, card_9, card_10)
        hand_2 = PokerHand(cards_2)
        actual_rank_2 = hand_2.rank()
        expected_rank_2 = ('Two Pairs', ('J', '7'))
        self.assertEqual(actual_rank_2, expected_rank_2)

    def test_can_determine_three_of_a_kind_from_hand(self):
        card_1 = Card(value='2', suit='C')
        card_2 = Card(value='2', suit='H')
        card_3 = Card(value='9', suit='S')
        card_4 = Card(value='2', suit='S')
        card_5 = Card(value='Q', suit='D')

        cards_1 = (card_1, card_2, card_3, card_4, card_5)
        hand_1 = PokerHand(cards_1)
        actual_rank_1 = hand_1.rank()
        expected_rank_1 = ('Three of a Kind', '2')
        self.assertEqual(actual_rank_1, expected_rank_1)

        card_6 = Card(value='A', suit='S')
        card_7 = Card(value='7', suit='C')
        card_8 = Card(value='7', suit='H')
        card_9 = Card(value='7', suit='D')
        card_10 = Card(value='Q', suit='C')

        cards_2 = (card_6, card_7, card_8, card_9, card_10)
        hand_2 = PokerHand(cards_2)
        actual_rank_2 = hand_2.rank()
        expected_rank_2 = ('Three of a Kind', '7')
        self.assertEqual(actual_rank_2, expected_rank_2)

    def test_can_determine_four_of_a_kind_from_hand(self):
        card_1 = Card(value='3', suit='C')
        card_2 = Card(value='3', suit='H')
        card_3 = Card(value='3', suit='D')
        card_4 = Card(value='3', suit='S')
        card_5 = Card(value='6', suit='S')

        cards_1 = (card_1, card_2, card_3, card_4, card_5)
        hand_1 = PokerHand(cards_1)
        actual_rank_1 = hand_1.rank()
        expected_rank_1 = ('Four of a Kind', '3')
        self.assertEqual(actual_rank_1, expected_rank_1)

        card_6 = Card(value='K', suit='H')
        card_7 = Card(value='K', suit='C')
        card_8 = Card(value='K', suit='S')
        card_9 = Card(value='2', suit='S')
        card_10 = Card(value='4', suit='D')

        cards_2 = (card_6, card_7, card_8, card_9, card_10)
        hand_2 = PokerHand(cards_2)
        actual_rank_2 = hand_2.rank()
        expected_rank_2 = ('Three of a Kind', 'K')
        self.assertEqual(actual_rank_2, expected_rank_2)

    def test_can_determine_straight_from_hand(self):
        card_1 = Card(value='2', suit='D')
        card_2 = Card(value='3', suit='H')
        card_3 = Card(value='4', suit='H')
        card_4 = Card(value='5', suit='C')
        card_5 = Card(value='6', suit='C')

        cards_1 = (card_1, card_2, card_3, card_4, card_5)
        hand_1 = PokerHand(cards_1)
        actual_rank_1 = hand_1.rank()
        expected_rank_1 = ('Straight', '6')
        self.assertEqual(actual_rank_1, expected_rank_1)

        card_6 = Card(value='6', suit='H')
        card_7 = Card(value='7', suit='H')
        card_8 = Card(value='8', suit='C')
        card_9 = Card(value='9', suit='D')
        card_10 = Card(value='T', suit='S')

        cards_2 = (card_6, card_7, card_8, card_9, card_10)
        hand_2 = PokerHand(cards_2)
        actual_rank_2 = hand_2.rank()
        expected_rank_2 = ('Straight', 'T')
        self.assertEqual(actual_rank_2, expected_rank_2)

    def test_can_determine_straight_including_ace_from_hand(self):
        card_1 = Card(value='T', suit='S')
        card_2 = Card(value='J', suit='H')
        card_3 = Card(value='Q', suit='C')
        card_4 = Card(value='K', suit='D')
        card_5 = Card(value='A', suit='H')

        cards_1 = (card_1, card_2, card_3, card_4, card_5)
        hand_1 = PokerHand(cards_1)
        actual_rank_1 = hand_1.rank()
        expected_rank_1 = ('Straight', 'A')
        self.assertEqual(actual_rank_1, expected_rank_1)

        card_6 = Card(value='A', suit='S')
        card_7 = Card(value='2', suit='H')
        card_8 = Card(value='3', suit='S')
        card_9 = Card(value='4', suit='D')
        card_10 = Card(value='5', suit='C')

        cards_2 = (card_6, card_7, card_8, card_9, card_10)
        hand_2 = PokerHand(cards_2)
        actual_rank_2 = hand_2.rank()
        expected_rank_2 = ('Straight', '5')
        self.assertEqual(actual_rank_2, expected_rank_2)

    def test_can_determine_flush_from_hand(self):
        card_1 = Card(value='2', suit='D')
        card_2 = Card(value='4', suit='D')
        card_3 = Card(value='5', suit='D')
        card_4 = Card(value='T', suit='D')
        card_5 = Card(value='K', suit='D')

        cards_1 = (card_1, card_2, card_3, card_4, card_5)
        hand_1 = PokerHand(cards_1)
        actual_rank_1 = hand_1.rank()
        expected_rank_1 = ('Flush', 'K')
        self.assertEqual(actual_rank_1, expected_rank_1)

        card_6 = Card(value='3', suit='S')
        card_7 = Card(value='4', suit='S')
        card_8 = Card(value='7', suit='S')
        card_9 = Card(value='T', suit='S')
        card_10 = Card(value='J', suit='S')

        cards_2 = (card_6, card_7, card_8, card_9, card_10)
        hand_2 = PokerHand(cards_2)
        actual_rank_2 = hand_2.rank()
        expected_rank_2 = ('Flush', 'J')
        self.assertEqual(actual_rank_2, expected_rank_2)

    def test_can_determine_full_house_from_hand(self):
        card_1 = Card(value='3', suit='D')
        card_2 = Card(value='3', suit='H')
        card_3 = Card(value='7', suit='H')
        card_4 = Card(value='7', suit='S')
        card_5 = Card(value='7', suit='C')

        cards_1 = (card_1, card_2, card_3, card_4, card_5)
        hand_1 = PokerHand(cards_1)
        actual_rank_1 = hand_1.rank()
        expected_rank_1 = ('Full House', '7')
        self.assertEqual(actual_rank_1, expected_rank_1)

        card_6 = Card(value='K', suit='S')
        card_7 = Card(value='4', suit='H')
        card_8 = Card(value='K', suit='C')
        card_9 = Card(value='4', suit='D')
        card_10 = Card(value='4', suit='S')

        cards_2 = (card_6, card_7, card_8, card_9, card_10)
        hand_2 = PokerHand(cards_2)
        actual_rank_2 = hand_2.rank()
        expected_rank_2 = ('Full House', '4')
        self.assertEqual(actual_rank_2, expected_rank_2)

    def test_can_determine_straight_flush_from_hand(self):
        card_1 = Card(value='3', suit='C')
        card_2 = Card(value='4', suit='C')
        card_3 = Card(value='5', suit='C')
        card_4 = Card(value='6', suit='C')
        card_5 = Card(value='7', suit='C')

        cards_1 = (card_1, card_2, card_3, card_4, card_5)
        hand_1 = PokerHand(cards_1)
        actual_rank_1 = hand_1.rank()
        expected_rank_1 = ('Straight Flush', '7')
        self.assertEqual(actual_rank_1, expected_rank_1)

        card_6 = Card(value='A', suit='S')
        card_7 = Card(value='K', suit='S')
        card_8 = Card(value='Q', suit='S')
        card_9 = Card(value='J', suit='S')
        card_10 = Card(value='T', suit='S')

        cards_2 = (card_6, card_7, card_8, card_9, card_10)
        hand_2 = PokerHand(cards_2)
        actual_rank_2 = hand_2.rank()
        expected_rank_2 = ('Straight Flush', 'A')
        self.assertEqual(actual_rank_2, expected_rank_2)

    def test_can_create_poker_game(self):
        card_1 = Card(value='2', suit='S')
        card_2 = Card(value='3', suit='H')
        card_3 = Card(value='6', suit='C')
        card_4 = Card(value='7', suit='D')
        card_5 = Card(value='9', suit='S')

        cards = (card_1, card_2, card_3, card_4, card_5)
        hand_1 = PokerHand(cards)

        card_6 = Card(value='3', suit='H')
        card_7 = Card(value='4', suit='C')
        card_8 = Card(value='5', suit='D')
        card_9 = Card(value='9', suit='D')
        card_10 = Card(value='T', suit='S')

        cards_2 = (card_6, card_7, card_8, card_9, card_10)
        hand_2 = PokerHand(cards_2)

        game_1 = PokerGame(hand_1, hand_2)
        self.assertIsInstance(game_1, PokerGame)

    def dtest_can_determine_winner_between_pair_and_high_card(self):
        card_1 = Card(value='2', suit='S')
        card_2 = Card(value='4', suit='H')
        card_3 = Card(value='6', suit='C')
        card_4 = Card(value='4', suit='D')
        card_5 = Card(value='7', suit='S')

        cards_1 = (card_1, card_2, card_3, card_4, card_5)
        hand_1 = PokerHand(cards_1)

        card_6 = Card(value='3', suit='H')
        card_7 = Card(value='4', suit='C')
        card_8 = Card(value='5', suit='D')
        card_9 = Card(value='9', suit='D')
        card_10 = Card(value='T', suit='S')

        cards_2 = (card_6, card_7, card_8, card_9, card_10)
        hand_2 = PokerHand(cards_2)

        game_1 = PokerGame(hand_1, hand_2)
        winner = game_1.winner()
        self.assertEqual(winner, 'Player 1 wins - Pair 4')

    def test_can_determine_winner_over_two_high_card_hands(self):
        card_1 = Card(value='2', suit='S')
        card_2 = Card(value='3', suit='H')
        card_3 = Card(value='6', suit='C')
        card_4 = Card(value='7', suit='D')
        card_5 = Card(value='9', suit='S')

        cards_1 = (card_1, card_2, card_3, card_4, card_5)
        hand_1 = PokerHand(cards_1)

        card_6 = Card(value='3', suit='H')
        card_7 = Card(value='4', suit='C')
        card_8 = Card(value='5', suit='D')
        card_9 = Card(value='9', suit='D')
        card_10 = Card(value='T', suit='S')

        cards_2 = (card_6, card_7, card_8, card_9, card_10)
        hand_2 = PokerHand(cards_2)

        game_1 = PokerGame(hand_1, hand_2)
        winner = game_1.winner()
        self.assertEqual(winner, 'Player 2 wins - High Card T')

if __name__ == '__main__':
    unittest.main()