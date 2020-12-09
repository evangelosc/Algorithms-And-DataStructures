#!/usr/bin/python

from solution import Solution

# Unit Test
nums1 = [1,3,5,6]
nums2 = [1]
t1 = 5
t2 = 2
t3 = 7 
t4 = 0

s1 = Solution(nums1, t1)
s2 = Solution(nums1, t2)
s3 = Solution(nums1, t3)
s4 = Solution(nums1, t4)
s5 = Solution(nums2, t4)

if (s1.searchInsert()==2):
    print("Pass")
    s1.resetAll()
else:
    print("Test 1 Failed")
if (s2.searchInsert()==1):
    print("Pass")
    s2.resetAll()
else:
    print("Test 2 Failed")
if (s3.searchInsert()==4):
    print("Pass")
    s3.resetAll()
else:
    print("Test 3 Failed")
if (s4.searchInsert()==0):
    print("Pass")
    s4.resetAll()
else:
    print("Test 4 Failed")
if (s5.searchInsert()==0):
    print("Pass")
    s5.resetAll()
else:
    print("Test 5 Failed")