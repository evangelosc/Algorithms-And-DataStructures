#!/usr/bin/python

from solution import Solution

# Unit Test

s = Solution()
if (s.removeElement([3,2,2,3], 3) == 2):
    print("Pass")
    s.reset_i(0)
else:
    print("Failed nums1")
if (s.removeElement([0,1,2,2,3,0,4,2], 2) == 5):
    print("Pass")
    s.reset_i(0)
else:
    print("Failed nums2")