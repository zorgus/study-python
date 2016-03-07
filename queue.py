
class Queue():

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return (len(self.items) == 0)

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

