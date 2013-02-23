class PokerGame:
    def __init__(self, hand_1, hand_2):
        self.hands = (hand_1, hand_2)

    def winner(self):
        winner = 1 if self.hands[0] > self.hands[1] else 2
        winning_hand = sorted(self.hands)[-1]
        return 'Player %s wins - %s' % (winner, winning_hand.hand_name())