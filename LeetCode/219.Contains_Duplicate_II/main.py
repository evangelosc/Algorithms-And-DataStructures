#!/usr/bin/python
from solution import Solution

# Unit Test
s = Solution()
if (s.containsNearbyDuplicate([1,2,3,1], 3) == True):
    print("Pass")
else:
    print("Failed")
if (s.containsNearbyDuplicate([1,0,1,1], 1) == True):
    print("Pass")
else:
    print("Failed")
if (s.containsNearbyDuplicate([1,2,3,1,2,3], 2) == False):
    print("Pass")
else:
    print("Failed")