class Range:
    def __init__(self, start=None, end=None):
        if start is None:
            self.range = []
        else:
            self.range = range(start, end)

    def in_range(self, n):
        return n in self.range

    def intersection(self, other_range):
        intersection_list = [n for n in other_range.range if n in self.range]
        if len(intersection_list) > 0:
            start = min(intersection_list)
            end = max(intersection_list) + 1
            return Range(start, end)
        return Range()