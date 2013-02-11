class PokerHand:
    def __init__(self, cards):
        if any(isinstance(card, Card) == False for card in cards):
            raise PokerHand.InvalidHandError
        self.cards = cards

    def show(self):
        return tuple(card.show() for card in self.cards)

    def rank(self):
        hand_type = 'High Card'
        self.sort_cards_by_value()
        high_card = self.cards[0]
        return (hand_type, high_card.value)

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