#!/usr/bin/python

from solution import Solution

# Unit Test
t1 = "GGLLGG"
t2 = "GG"
t3 = "GL"
s = Solution()
if (s.isRobotBounded(t1)==True):
    print("Pass")
else:
    print("Test 1 Failed")
if (s.isRobotBounded(t2)==False):
    print("Pass")
else:
    print("Test 2 Failed")
if (s.isRobotBounded(t3)==True):
    print("Pass")
else:
    print("Test 3 Failed")