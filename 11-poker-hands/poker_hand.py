from itertools import combinations
from card import Card


class PokerHand:
    hand_types = (
        'High Card',
        'Pair',
        'Two Pairs',
        'Three of a Kind',
        'Straight',
        'Flush',
        'Full House',
        'Four of a Kind',
        'Straight Flush'
    )

    def __init__(self, cards):
        invalid_cards = any(isinstance(card, Card) == False for card in cards)
        card_set = {repr(card) for card in cards}
        duplicate_cards = len(card_set) < len(cards)

        if invalid_cards or duplicate_cards or len(cards) != 5:
            raise PokerHand.InvalidHandError
        self.cards = sorted(cards)

    def __str__(self):
        return str(self.show())

    def __repr__(self):
        return str(self.show())

    def __gt__(self, other):
        self_hand, self_cards = self.rank()
        other_hand, other_cards = other.rank()
        self_hand_value = PokerHand.hand_types.index(self_hand)
        other_hand_value = PokerHand.hand_types.index(other_hand)
        if self_hand_value == other_hand_value:
            if self_hand == other_hand:
                return False
            return self_hand > other_hand
        return self_hand_value > other_hand_value

    def show(self):
        return tuple(card.show() for card in self.cards)

    def hand_name(self):
        rank, cards = self.rank()
        cards = ' '.join(cards)
        return '%s %s' % (rank, cards)

    def rank(self):
        card_suit_set = {card.suit for card in self.cards}
        unique_card_suits = len(card_suit_set)
        if unique_card_suits == 1:
            highest_card = self.cards[-1]
            straight = self.straight()
            if straight:
                return ('Straight Flush', highest_card.value)
            return ('Flush', highest_card.value)

        card_value_set = {card.value for card in self.cards}
        unique_card_values = len(card_value_set)
        if unique_card_values < 5:
            return self.repeats()

        straight = self.straight()
        return straight if straight else self.high_card()

    def high_card(self):
        hand_type = 'High Card'
        high_card = self.cards[-1]
        return (hand_type, high_card.value)

    def pairs(self):
        card_values = [card.value for card in self.cards]
        card_combinations = combinations(card_values, 2)
        repeated_values = [a for (a, b) in card_combinations if a == b]
        if len(repeated_values) == 2:
            return ('Two Pairs', tuple(reversed(repeated_values)))
        repeated_value = repeated_values[0]
        return self.which_n_of_a_kind(repeated_value)

    def which_n_of_a_kind(self, repeated_value):
        hand_types = {
            2: 'Pair',
            3: 'Three of a Kind',
            4: 'Four of a Kind'
        }
        card_values = [card.value for card in self.cards]
        n = card_values.count(repeated_value)
        return (hand_types[n], repeated_value)

    def straight(self):
        min_card, min_value_index = self.cards[0], self.cards[4].value_index
        max_card, max_value_index = self.cards[4], self.cards[0].value_index
        if min_value_index == max_value_index + 4:
            return ('Straight', max_card.value)

    def full_house(self):
        most_frequent_card = self.most_frequent_card()
        return ('Full House', most_frequent_card.value)

    def repeats(self):
        card_value_set = {card.value for card in self.cards}
        unique_card_values = len(card_value_set)
        if unique_card_values == 2:
            card_values = [card.value for card in self.cards]
            first_card_count = card_values.count(list(card_value_set)[0])
            last_card_count = card_values.count(list(card_value_set)[1])
            three_two = first_card_count == 3 and last_card_count == 2
            two_three = first_card_count == 2 and last_card_count == 3
            if three_two or two_three:
                return self.full_house()
        return self.pairs()

    def most_frequent_card(self):
        card_values = [card.value for card in self.cards]
        most_common_value = max(set(card_values), key=card_values.count)
        most_common_card = card_values.index(most_common_value)
        return self.cards[most_common_card]

    class InvalidHandError(Exception):
        pass