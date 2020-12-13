#!/usr/bin/python

class Solution(object):
    def isMonotonic(self, A):
        if sorted(A, reverse=True)==A or sorted(A)==A:
            return True
        return False