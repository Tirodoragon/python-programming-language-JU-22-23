import random


class RandomQueue:

    def __init__(self, capacity=10):
        self.items = []
        self.capacity = capacity

    def insert(self, item):   # wstawia element w czasie O(1)
        if self.is_full():
            raise ValueError("RandomQueue is already full!")
        self.items.append(item)

    def remove(self):   # zwraca losowy element w czasie O(1)
        if self.is_empty():
            raise ValueError("RandomQueue is empty!")
        index = random.randint(0, len(self.items) - 1)
        item = self.items[index]
        self.items[index] = self.items[-1]
        self.items.pop()
        return item

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def clear(self):   # czyszczenie listy
        self.items = []
