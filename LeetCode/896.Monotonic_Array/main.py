#!/usr/bin/python
from solution import Solution

# Unit Test
v1 = [1,2,2,3]
v2 = [6,5,4,4]
v3 = [1,3,2]
v4 = [1,2,4,5]
v4 = [1,1,1,1]
s = Solution()
if (s.isMonotonic(v1)==True):
    print("PASS")
else:
    print("TEST 1 FAILED")

if (s.isMonotonic(v2)==False):
    print("PASS")
else:
    print("TEST 2 FAILED")


if (s.isMonotonic(v3)==False):
    print("PASS")
else:
    print("TEST 3 FAILED")


if (s.isMonotonic(v4)==False):
    print("PASS")
else:
    print("TEST 4 FAILED")

if (s.isMonotonic(v5)==False):
    print("PASS")
else:
    print("TEST 5 FAILED")