from recently_used_list import RecentlyUsedList
import unittest


class Test(unittest.TestCase):
    def test_list_is_initially_empty(self):
        recents = RecentlyUsedList()
        self.assertEqual(recents.size(), 0)

    def test_most_recently_added_item_is_top(self):
        recents = RecentlyUsedList()
        recents.add_item('A')
        recents.add_item('B')
        top_item = recents.get_top_item()
        self.assertEqual(top_item, 'B')

    def test_least_recently_added_item_is_bottom(self):
        recents = RecentlyUsedList()
        recents.add_item('A')
        recents.add_item('B')
        bottom_item = recents.get_bottom_item()
        self.assertEqual(bottom_item, 'A')

    def test_lookup_item_by_index(self):
        recents = RecentlyUsedList()
        recents.add_item('A')
        recents.add_item('B')
        recents.add_item('C')
        recents.add_item('D')
        item_1 = recents.get_item(1)
        self.assertEqual(item_1, 'C')
        item_2 = recents.get_item(2)
        self.assertEqual(item_2, 'B')

    def test_lookup_item_out_of_range(self):
        recents = RecentlyUsedList()
        recents.add_item('A')
        recents.add_item('B')
        self.assertRaises(IndexError, recents.get_item, 5)

    def test_adding_exist_item_should_move_to_top(self):
        recents = RecentlyUsedList()
        recents.add_item('A')
        recents.add_item('B')
        recents.add_item('A')
        top_item = recents.get_top_item()
        self.assertEqual(top_item, 'A')
        self.assertEqual(recents.size(), 2)

    def test_null_insertions_are_not_allowed(self):
        recents = RecentlyUsedList()
        expected_exception = RecentlyUsedList.NullInsertionError
        self.assertRaises(expected_exception, recents.add_item, '')

    def test_bounded_capacity(self):
        recents = RecentlyUsedList(5)
        recents.add_item('A')
        recents.add_item('B')
        recents.add_item('C')
        recents.add_item('D')
        recents.add_item('E')
        self.assertEqual(recents.size(), 5)
        self.assertEqual(recents.get_bottom_item(), 'A')
        recents.add_item('F')
        self.assertEqual(recents.size(), 5)
        self.assertEqual(recents.get_bottom_item(), 'B')


if __name__ == '__main__':
    unittest.main()