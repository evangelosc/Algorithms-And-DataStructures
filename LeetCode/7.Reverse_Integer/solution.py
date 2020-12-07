#!/usr/bin/python

class Solution(object):
    def __init__(self):
        self.is_negative = False
        self.reversed = 0
        self.INT_MAX_32 = 2**32 - 1

    def reverse(self, x):
        self.is_negative = x < 0
        x = abs(x)
        self.reversed = 0

        while x:
            self.reversed *= 10
            self.reversed += x % 10
            x /= 10
            x = int(x)
            
        if self.reversed > self.INT_MAX_32:
            return 0
        elif self.is_negative:
            return -self.reversed
        else:
            return self.reversed