import random

class Game:
    def __init__(self, prize=None):
        self._options = [1, 2, 3]
        self._prize = prize if prize else random.choice(self.options)
        self._selection = None
        self.won = None

    @property
    def options(self):
        return self._options

    def select_door(self, door):
        if door not in self.options:
            raise ValueError
        self._selection = door
        if door == self._prize:
            other_doors = [opt for opt in self.options if opt != door]
            open_door = random.choice(other_doors)
            self._options = [opt for opt in self.options if opt != open_door]
        else:
            open_door = [opt for opt in self.options
                         if opt != door and opt != self._prize][0]
            self._options = [opt for opt in self.options if opt != open_door]

    def final_selection(self, change=True):
        if self._selection is None:
            raise ValueError
        if change:
            self._selection = [opt for opt in self.options
                               if opt != self._selection][0]
        else:
            self._selection = [opt for opt in self.options
                               if opt == self._selection][0]
        self.won = self._selection == self._prize

if __name__ == '__main__':
    n = 10000
    kept_selection_wins = 0
    for i in range(n):
        game = Game()
        first_choice = random.choice([1, 2, 3])
        game.select_door(first_choice)
        game.final_selection(change=False)
        if game.won:
            kept_selection_wins += 1

    changed_selection_wins = 0
    for i in range(n):
        game = Game()
        first_choice = random.choice([1, 2, 3])
        game.select_door(first_choice)
        game.final_selection(change=True)
        if game.won:
            changed_selection_wins += 1

    print(f'Kept selection wins: {kept_selection_wins/n*100:.2f}%')
    print(f'Changed selection wins: {changed_selection_wins/n*100:.2f}%')
