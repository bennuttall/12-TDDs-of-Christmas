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
        return self.high_card()

    def high_card(self):
        hand_type = 'High Card'
        self.sort_cards_by_value()
        high_card = self.cards[0]
        return (hand_type, high_card.value)

    def pairs(self):
        card_values = [card.value for card in self.cards]
        pair_values = [a for (a, b) in combinations(card_values, 2) if a == b]
        if len(pair_values) == 2:
            return ('Two Pair', tuple(pair_values))
        return ('Pair', pair_values[0])

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