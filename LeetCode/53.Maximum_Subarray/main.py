#!/usr/bin/python

from solution import Solution

# Unit Test
t1 = [-2,1,-3,4,-1,2,1,-5,4]
t2 = [1]
t3 = [0]
t4 = [-1]
t5 = [-2147483647]
s = Solution()
if (s.maxSubArray(t1)==6):
    print("Pass")
else:
    print("Test 1 Failed")
if (s.maxSubArray(t2)==1):
    print("Pass")
else:
    print("Test 2 Failed")
if (s.maxSubArray(t3)==0):
    print("Pass")
else:
    print("Test 3 Failed")
if (s.maxSubArray(t4)==-1):
    print("Pass")
else:
    print("Test 4 Failed")
if (s.maxSubArray(t5)==-2147483647):
    print("Pass")
else:
    print("Test 5 Failed")
