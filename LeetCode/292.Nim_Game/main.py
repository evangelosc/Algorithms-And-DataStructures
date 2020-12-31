#!/usr/bin/python
from solution import Solution

# Unit Test
s = Solution()
if (s.canWinNim(1) == True):
    print("Pass")
else:
    print("Failed")
if (s.canWinNim(2) == True):
    print("Pass")
else:
    print("Failed")