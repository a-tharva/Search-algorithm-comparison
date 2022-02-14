"""list

class:

    _stack

functions:

    add(value)
    peek()
    remove()
"""


class _stack:
    def __init__(self):
        self.stack = []
        self.length = 0
    
    
    def add(self, value):
        if value not in self.stack:
            self.stack.append(data)
            self.length += 1
            return True
        else:
            return False
    
    
    def peek(self):
        return self.stack[-1]
    
    
    def remove(self):
        if self.length <= 0:
            return('No element in stack')
        else:
            return self.stack.pop()