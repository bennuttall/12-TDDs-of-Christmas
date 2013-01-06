from monty_hall import MontyHall
import unittest


class Test(unittest.TestCase):
    def test_start_game(self):
        monty_hall = MontyHall()
        self.assertIsInstance(monty_hall, MontyHall)

    def test_choose_door_out_of_range(self):
        monty_hall = MontyHall()
        expected_exception = MontyHall.Error404DoorNotFound
        self.assertRaises(expected_exception, monty_hall.choose_door, 4)

    def test_choose_door(self):
        monty_hall = MontyHall()
        choice = 1
        switch_options = monty_hall.choose_door(choice)
        self.assertIsInstance(switch_options, list)
        number_of_options = len(switch_options)
        self.assertEqual(number_of_options, 2)
        self.assertTrue(all(option in range(1, 4) for option in switch_options))
        self.assertTrue(choice in switch_options)

    def test_make_erroneous_second_choice(self):
        monty_hall = MontyHall()
        switch_options = set(monty_hall.choose_door(1))
        all_doors = set(range(1, 4))
        door_shown = all_doors.difference(switch_options)
        expected_exception = MontyHall.Error403ForbiddenDoor
        self.assertRaises(expected_exception, monty_hall.make_second_choice, door_shown)

    def test_make_second_choice(self):
        monty_hall = MontyHall()
        switch_options = monty_hall.choose_door(1)
        win_or_lose = monty_hall.make_second_choice(1)
        self.assertIsInstance(win_or_lose, bool)


if __name__ == '__main__':
    unittest.main()