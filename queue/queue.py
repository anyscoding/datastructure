class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)