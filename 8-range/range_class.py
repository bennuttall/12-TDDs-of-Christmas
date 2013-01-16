class Range:
    def __init__(self, start=None, end=None):
        if start is None:
            self.range = None
        else:
            self.range = (start, end)

    def in_range(self, n):
        start, end = self.range
        return start <= n <= end

    def intersection(self, other):
        if self.range is None or other.range is None:
            return Range()

        a = self.range if self.range[0] < other.range[0] else other.range
        b = other.range if a == self.range else self.range

        a_min, a_max = a
        b_min, b_max = b

        if a_max < b_min:
            return Range()

        if b_max > a_max:
            start = b_min
            end = a_max
            return Range(start, end)

        start = b_min
        end = b_max
        return Range(start, end)