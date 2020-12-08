#!/usr/bin/python
from solution import Solution

# Unit Test

s = Solution()
nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]
if (s.removeDuplicates(nums1) == 2):
    print("Pass")
    s.reset_i(0)
else:
    print("Failed - nums1")
if (s.removeDuplicates(nums2) == 5):
    print("Pass")
    s.reset_i(0)
else:
    print("Failed - nums2")