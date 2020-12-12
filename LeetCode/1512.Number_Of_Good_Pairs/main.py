#!/usr/bin/python

from solution import Solution

# Unit Test
nums1 = [1,2,3,1,1,3]
nums2 = [1,1,1,1]
nums3 = [1,2,3]
s = Solution()
if (s.numIdenticalPairs(nums1) == 4):
    print("Pass")
else:
    print("Test 1 Failed")
if (s.numIdenticalPairs(nums2) == 6):
    print("Pass")
else:
    print("Test 2 Failed")
if (s.numIdenticalPairs(nums3) == 0):
    print("Pass")
else:
    print("Test 3 Failed")