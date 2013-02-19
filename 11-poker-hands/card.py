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

    def __eq__(self, card):
        return self.value == card.value

    def __lt__(self, card):
        return Card.values.index(self.value) < Card.values.index(card.value)

    def __gt__(self, card):
        return Card.values.index(self.value) > Card.values.index(card.value)

    @staticmethod
    def validate_card_element(element, group):
        if element not in group:
            raise Card.InvalidCardError
        return element

    def show(self):
        return '%s%s' % (self.value, self.suit)

    class InvalidCardError(Exception):
        pass