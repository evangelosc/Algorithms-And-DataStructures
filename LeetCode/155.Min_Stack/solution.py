#!/usr/bin/python

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lista = list()
        self.minEl = float("inf")

    def push(self, x: int) -> None:
        self.minEl = min(self.minEl, x)
        self.lista.append((x, self.minEl))
        
    def pop(self) -> None:
        self.lista.pop()
        if len(self.lista):
            self.minEl = self.lista[-1][1]
        else:
            self.minEl = float("inf")

    def top(self) -> int:
        return self.lista[-1][0]

    def getMin(self) -> int:
        return self.lista[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()