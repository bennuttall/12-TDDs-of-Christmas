class CalcStats:
    def __init__(self, values):
        self.values = values

    def min(self):
        return min(self.values)

    def max(self):
        return max(self.values)

    def len(self):
        return len(self.values)

    def ave(self):
        return round(float(sum(self.values)) / self.len(), 6)
