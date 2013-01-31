class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def __len__(self):
        return len(self.contacts)

    def add_contact(self, name, number):
        number = number.replace(' ', '')
        numbers = self.contacts.values()

        short_matches = [entry[:len(number)] == number for entry in numbers]
        long_matches = [number[:len(entry)] == entry for entry in numbers]
        inconsistent_entries = short_matches + long_matches

        if any(inconsistent_entries):
            raise PhoneBook.InconsistentEntryError
        self.contacts[name] = number

    def lookup_number(self, name):
        return self.contacts[name]

    def lookup_name(self, number):
        name = (name for name, num in self.contacts.items() if num == number)
        return name.next()

    class InconsistentEntryError(Exception):
        pass