#!/usr/bin/python
from solution import Solution

# Unit Test
string1 = "UD"
string2 = "LL"
string3 = "LDRRLRUULR"
s = Solution()
if (s.judgeCircle(string1)==True):
    print("PASS")
else:
    print("TEST 1 FAILED")

if (s.judgeCircle(string2)==False):
    print("PASS")
else:
    print("TEST 2 FAILED")


if (s.judgeCircle(string3)==False):
    print("PASS")
else:
    print("TEST 2 FAILED")