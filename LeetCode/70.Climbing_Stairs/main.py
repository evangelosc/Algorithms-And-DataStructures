#!/usr/bin/python

from solution import Solution

# Unit Test
t1 = 2
t2 = 3
s = Solution()
if (s.climbStairs(t1)==2):
    print("Pass")
else:
    print("Test 1 Failed")
if (s.climbStairs(t2) == 3):
    print("Pass")
else:
    print("Test 2 Failed")