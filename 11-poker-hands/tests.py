from poker_hands import PokerHand, Card
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
        hand_1 = PokerHand(cards)
        expected_hand = ('AS', '2H', '3C', 'QD', 'KS')
        self.assertEqual(hand_1.show(), expected_hand)

    def test_can_determine_card_value_index(self):
        card_1 = Card(value='A', suit='S')
        value_index_1 = card_1.value_index
        expected_index_1 = 0
        self.assertEqual(value_index_1, expected_index_1)

        card_2 = Card(value='5', suit='H')
        value_index_2 = card_2.value_index
        expected_index_2 = 9
        self.assertEqual(value_index_2, expected_index_2)

        card_3 = Card(value='J', suit='D')
        value_index_3 = card_3.value_index
        expected_index_3 = 3
        self.assertEqual(value_index_3, expected_index_3)

    def test_can_determine_high_card_from_deck(self):
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


if __name__ == '__main__':
    unittest.main()
