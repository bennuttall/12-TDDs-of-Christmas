class RecentlyUsedList:
    def __init__(self, limit=False):
        self._list = []
        self.limit = limit

    def __len__(self):
        return len(self._list)

    def __getitem__(self, i):
        return self.items[i]

    def add(self, item):
        if not isinstance(item, str) or len(item) == 0:
            raise ValueError
        if item in self.items:
            del self._list[self._list.index(item)]
        if self.limit and len(self) == self.limit:
            del self._list[0]
        self._list.append(item)

    @property
    def items(self):
        return list(reversed(self._list))
