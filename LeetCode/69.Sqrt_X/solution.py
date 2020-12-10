#!/usr/bin/python


class Solution(object):
    def __init__(self):
        pass
    def mySqrt(self, x):
        if(x<1):
            return 0
        if(x<4):
            return 1
        first = 1
        last = x
        while(first<=last):
            mid = (first+last)//2
            if (mid*mid <= x):
                res = mid
                first = mid + 1
            if (mid*mid > x):
                last = mid - 1
        return int(res)