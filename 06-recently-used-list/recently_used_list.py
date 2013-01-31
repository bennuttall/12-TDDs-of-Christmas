class RecentlyUsedList:
    def __init__(self, capacity=False):
        self.list = []
        self.capacity = capacity

    def size(self):
        return len(self.list)

    def add_item(self, item):
        if item == '':
            raise RecentlyUsedList.NullInsertionError
        if item in self.list:
            self.list.remove(item)
        self.list.append(item)
        if self.capacity and len(self.list) > self.capacity:
            del self.list[0]

    def get_top_item(self):
        return self.list[-1]

    def get_bottom_item(self):
        return self.list[0]

    def get_item(self, index):
        return list(reversed(self.list))[index]

    class NullInsertionError(Exception):
        pass