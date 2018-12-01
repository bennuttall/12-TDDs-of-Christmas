class Calculator:
    def __init__(self, values):
        self.values = values

    def __getattr__(self, attr):
        return {
            'min': min(self.values),
            'max': max(self.values),
            'len': len(self.values),
            'avg': sum(self.values) / len(self.values),
        }[attr]
