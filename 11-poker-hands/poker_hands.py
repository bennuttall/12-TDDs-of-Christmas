from itertools import combinations


class PokerHand:
    def __init__(self, cards):
        invalid_cards = any(isinstance(card, Card) == False for card in cards)
        card_set = {repr(card) for card in cards}
        duplicate_cards = len(card_set) < len(cards)

        if invalid_cards or duplicate_cards or len(cards) != 5:
            raise PokerHand.InvalidHandError
        self.cards = cards

    def show(self):
        return tuple(card.show() for card in self.cards)

    def rank(self):
        card_value_set = {card.value for card in self.cards}
        unique_cards = len(card_value_set)
        if unique_cards < 5:
            return self.pairs()
        straight = self.straight()
        return straight if straight else self.high_card()

    def high_card(self):
        self.sort_cards_by_value()
        hand_type = 'High Card'
        high_card = self.cards[0]
        return (hand_type, high_card.value)

    def pairs(self):
        card_values = [card.value for card in self.cards]
        repeated_values = [a for (a, b) in combinations(card_values, 2) if a == b]
        if len(repeated_values) == 2:
            return ('Two Pair', tuple(repeated_values))
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
        self.sort_cards_by_value()
        min_card, min_value_index = self.cards[4], self.cards[4].value_index
        max_card, max_value_index = self.cards[0], self.cards[0].value_index
        if min_value_index == max_value_index + 4:
            return ('Straight', max_card.value)

    def sort_cards_by_value(self):
        self.cards = sorted(self.cards, key=lambda card: card.value_index)

    class InvalidHandError(Exception):
        pass


class Card:
    values = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2')
    suits = ('H', 'D', 'S', 'C')

    def __init__(self, value, suit):
        self.value = Card.validate_card_element(value, Card.values)
        self.suit = Card.validate_card_element(suit, Card.suits)
        self.value_index = Card.values.index(self.value)

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

    @staticmethod
    def validate_card_element(element, group):
        if element not in group:
            raise Card.InvalidCardError
        return element

    def show(self):
        return '%s%s' % (self.value, self.suit)

    class InvalidCardError(Exception):
        pass