class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = list()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s.reverse()
        self.s.append(x)
        self.s.reverse()
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.s.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()