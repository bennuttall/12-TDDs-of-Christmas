from random import choice


class MontyHall:
    def __init__(self):
        self.doors = range(1, 4)
        self.prize_location = choice(self.doors)

    def choose_door(self, door):
        if door not in self.doors:
            raise MontyHall.Error404DoorNotFound
        self.initial_choice = door
        self.switch_options = self.get_switch_options()
        return self.switch_options

    def get_switch_options(self):
        if self.initial_choice == self.prize_location:
            show_options = self.doors[::]
            show_options.remove(self.prize_location)
            door_shown = choice(show_options)
            switch_options = self.doors[::]
            switch_options.remove(door_shown)
            return switch_options
        return [self.initial_choice, self.prize_location]

    def make_second_choice(self, door):
        if door not in self.switch_options:
            raise MontyHall.Error403ForbiddenDoor
        return door == self.prize_location

    class Error404DoorNotFound(Exception):
        pass

    class Error403ForbiddenDoor(Exception):
        pass


def main():
    doors = range(1, 4)
    iterations = 10000
    print 'Monte Carlo simulation'

    print 'Strategy: keep same door'
    wins = 0
    for i in range(iterations):
        monty_hall = MontyHall()
        first_choice = choice(doors)
        switch_options = monty_hall.choose_door(first_choice)
        wins += monty_hall.make_second_choice(first_choice)
    win_percentage = 100 * float(wins) / iterations
    print 'Won %s%%' % win_percentage

    print 'Strategy: change door'
    wins = 0
    for i in range(iterations):
        monty_hall = MontyHall()
        first_choice = choice(doors)
        switch_options = monty_hall.choose_door(first_choice)
        switch_options.remove(first_choice)
        second_choice = switch_options[0]
        wins += monty_hall.make_second_choice(second_choice)
    win_percentage = 100 * float(wins) / iterations
    print 'Won %s%%' % win_percentage

if __name__ == '__main__':
    main()