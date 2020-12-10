#!/usr/bin/python
import math

class Solution(object):
    def __init__(self):
        pass
    def climbStairs(self, n: int) -> int:
        if (n==0):
            return 0
        if (n==1):
            return 1
        res = 0
        for el in range(n//2+1):
            res += math.factorial(n-el)/(math.factorial(el)*math.factorial(n-2*el))
        return int(res)