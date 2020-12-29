#!/usr/bin/python

from solution import Solution

# Unit Test
s1 = "codeleet", indices1 = [4,5,6,7,0,2,1,3]
s2 = "abc", indices2 = [0,1,2]
s3 = "aiohn", indices3 = [3,1,4,2,0]
s = Solution()
if (s.restoreString(s1, indices1) == "leetcode"):
    print("Pass")
else:
    print("Test 1 Failed")
if (s.restoreString(s2, indices2) == "abc"):
    print("Pass")
else:
    print("Test 2 Failed")
if (s.restoreString(s3, indices3) == "nihao"):
    print("Pass")
else:
    print("Test 3 Failed")