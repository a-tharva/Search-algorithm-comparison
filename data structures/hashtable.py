"""Hash Table

class:

    _HashTable

functions:

    get_hash(self, key)
    __getitem__(self, index)
    __setitem__(self, key, val)
    __delitem__(self, key)
"""

class _HashTable:
    
    
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
        
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        for _ in self.arr[h]:
            if _[0] == index:
                return _[1]
    
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))
        
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, _ in enumerate(self.arr[h]):
            if _[0] == key:
                print('del', index)
                del self.arr[h][index]