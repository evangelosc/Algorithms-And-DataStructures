#!/usr/bin/python

from solution import Solution

# Unit Test
t1 = 4
t2 = 8
s = Solution()
if (s.mySqrt(t1)==2):
    print("Pass")
else:
    print("Test 1 Failed")
if (s.mySqrt(t2) == 2):
    print("Pass")
else:
    print("Test 2 Failed")