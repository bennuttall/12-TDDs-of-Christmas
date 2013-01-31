class Number:
    def __init__(self, n):
        self.n = str(n)

        self.units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        self.units = {str(i): self.units[i] for i in range(10)}

        self.teens = {
                '1': 'eleven',
                '2': 'twelve',
                '3': 'thirteen',
                '5': 'fifteen',
                '8': 'eighteen'
                }
        for i in range(1, 10):
            if str(i) not in self.teens:
                self.teens[str(i)] = self.units[str(i)] + 'teen'

        self.tens = {
                '1': 'ten',
                '2': 'twenty',
                '3': 'thirty',
                '4': 'forty',
                '5': 'fifty'
                }
        for i in range(1, 10):
            if str(i) not in self.tens:
                self.tens[str(i)] = self.units[str(i)] + 'ty'

        self.orders = ['', ' thousand', ' million', ' billion', ' trillion', ' quadrillion', ' quintillion']

    def name(self):
        if self.n == '0':
            return 'zero'

        if '.' in self.n:
            number, decimals = self.n.split('.')
            number = Number(number)
            number = '%s point ' % number.name()
            decimals = [self.units[d] for d in decimals]
            number += ' '.join(decimals)
            return number

        neg = '' if int(self.n) > 0 else self.negative()

        triples = self.three_split()

        orders_needed = self.orders[:len(triples)]

        number_strings = []
        for triple in triples:
            triple_name = self.triple_to_name(triple)
            order = orders_needed.pop()
            if len(triple_name) > 0:
                number_strings.append(triple_name + order)

        if len(number_strings) > 1:
            if 'and' in number_strings[-1]:
                return neg + ', '.join(number_strings)
            return neg + ', '.join(number_strings[:-1]) + ' and ' + number_strings[-1]
        return neg + number_strings[0]

    def negative(self):
        self.n = self.n[1:]
        return 'negative '

    def three_split(self):
        self.zero_prepend()
        triples = []
        for i in range(0, len(self.n), 3):
            j = i + 3
            triples.append(self.n[i:j])
        return triples

    def zero_prepend(self):
        while len(self.n) % 3 > 0:
            self.n = '0%s' % self.n

    def triple_to_name(self, triple):
        hundred, ten, unit = triple

        units = self.units
        teens = self.teens
        tens = self.tens

        number_string = ''
        if hundred != '0':
            number_string += units[hundred] + ' hundred'
            if ten != '0' or unit != '0':
                number_string += ' and '

        if ten == '1' and unit in teens:
            number_string += teens[unit]
        else:
            if ten != '0':
                number_string += tens[ten]
                if unit != '0':
                    number_string += ' '

            if unit != '0':
                number_string += units[unit]

        return number_string