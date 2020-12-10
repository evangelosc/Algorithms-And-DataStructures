#!/usr/bin/python

from solution import Solution

# Unit Test
a1 = "11"
b1 = "1"
a2 = "1010"
b2 = "1011"

s = Solution()
if (s.addBinary(a1, b1)=="100"):
    print("Pass")
else:
    print("Test 1 Failed")
if (s.addBinary(a2, b2)=="10101"):
    print("Pass")
else:
    print("Test 2 Failed")