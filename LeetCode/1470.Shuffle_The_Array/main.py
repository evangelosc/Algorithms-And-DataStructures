#!/usr/bin/python

from solution import Solution

# Unit Test
nums1 = [2,5,1,3,4,7]
n = 3
s = Solution()
if (s.shuffle(nums1, n)==[2,3,5,4,1,7]):
    print("Pass")
else:
    print("Test 1 Failed")