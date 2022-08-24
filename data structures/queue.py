"""Hash Table

class:

    _queue

functions:

    enqueue(value)
    dequeue()
    is_empty()
    size()
"""


class _queue:

    def __init__(self):
        self.queue = []
        self.length = 0

    def enqueue(self, value):
        self.queue.append(value)
        self.length += 1

    def dequeue(self):
        if self.length <= 0:
            return('No element in queue')
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return self.length <= 0

    def size(self):
        return self.length
