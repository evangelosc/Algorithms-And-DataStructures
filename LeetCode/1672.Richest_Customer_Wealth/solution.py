#!/usr/bin/python

class Solution(object):
    def __init__(self):
        self.max_pointer = 0
        self.current_pointer = 0
    def maximumWealth(self, accounts):
        for client in accounts:
            for el in client:
                self.current_pointer += el
            if self.current_pointer>self.max_pointer:
                self.max_pointer = self.current_pointer
            self.current_pointer = 0
        return self.max_pointer

        