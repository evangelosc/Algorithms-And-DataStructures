#!/usr/bin/python

from solution import Solution

# Unit Test
t1 = 1
t2 = 4
s = Solution()
if (s.countAndSay(t1)=="1"):
    print("Pass")
else:
    print("Test 1 Failed")
if (s.countAndSay(t2) == "1211"):
    print("Pass")
else:
    print("Test 2 Failed")