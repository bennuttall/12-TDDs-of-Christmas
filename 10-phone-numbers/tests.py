from phone_numbers import PhoneBook
import unittest


class Test(unittest.TestCase):
    def test_new_phonebook(self):
        phonebook = PhoneBook()
        self.assertIsInstance(phonebook, PhoneBook)

    def test_empty_phonebook_length(self):
        phonebook = PhoneBook()
        number_of_entries = len(phonebook)
        self.assertEqual(number_of_entries, 0)

    def test_add_number_to_phonebook(self):
        phonebook = PhoneBook()
        number_of_entries = len(phonebook)
        self.assertEqual(number_of_entries, 0)

        phonebook.add_contact('Bob', '91 12 54 26')
        new_number_of_entries = len(phonebook)
        self.assertEqual(new_number_of_entries, 1)

        phonebook.add_contact('Alice', '97 625 992')
        new_new_number_of_entries = len(phonebook)
        self.assertEqual(new_new_number_of_entries, 2)

    def test_lookup_number_by_name(self):
        phonebook = PhoneBook()
        phonebook.add_contact('Bob', '91 12 54 26')
        bob_number = phonebook.lookup_number('Bob')
        bob = '91125426'
        self.assertEqual(bob, bob_number)

    def test_lookup_name_by_number(self):
        phonebook = PhoneBook()
        phonebook.add_contact('Bob', '91 12 54 26')
        name = phonebook.lookup_name('91125426')
        bob = 'Bob'
        self.assertEqual(name, bob)

    def test_lookup_name_by_number(self):
        phonebook = PhoneBook()
        phonebook.add_contact('Bob', '91 12 54 26')
        name = phonebook.lookup_name('91125426')
        bob = 'Bob'
        self.assertEqual(name, bob)

    def test_add_inconsistent_smaller_number(self):
        phonebook = PhoneBook()
        phonebook.add_contact('Bob', '91 12 54 26')
        exception = PhoneBook.InconsistentEntryError
        self.assertRaises(exception, phonebook.add_contact, 'Emergency', '911')

    def test_add_inconsistent_longer_number(self):
        phonebook = PhoneBook()
        phonebook.add_contact('Emergency', '911')
        exception = PhoneBook.InconsistentEntryError
        self.assertRaises(exception, phonebook.add_contact, 'Bob', '91 12 54 26')


if __name__ == '__main__':
    unittest.main()