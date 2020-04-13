class stack:
    def __init__(self):
        self.items = list()
    def push(self, element):
        self.items.append(element)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)