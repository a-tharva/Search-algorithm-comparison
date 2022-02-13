"""list

class:

    _lsit

functions:

    linear_search(array, search_element)
    jump_search(array, array_length, search_element)
    binary_search(array, left, right, search_element)
    interpolation_search(array, lower_limit, higher_limit, search_element)
"""

import ctypes

class _list:
    
    def __init__(self):
        self.length = 0
        self.capacity = 10
        self.array = (self.capacity * ctypes.py_object)()
        
    def append(self, item):
        if self.length == self.capacity:
            self._resize(self.capacity*2)
        self.array[self.length] = item
        self.length += 1
        
    def _resize(self, new_cap):
        new_arr = (new_cap * ctypes.py_object)()
        for idx in range(self.length):
            new_arr[idx] = self.array[idx]
        self.array = new_arr
        self.capacity = new_cap
        
    def __len__(self):
        return self.length
    
    def __getitem__(self, idx):
        return self.array[idx]