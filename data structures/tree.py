

class _tree:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


#    def print_tree(self):


    def add_child(self, child):
        child.parent = self
        self.children.append(child)
