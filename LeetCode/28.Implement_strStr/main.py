#!/usr/bin/python

from solution import Solution

# Unit Test
haystack1 = "hello"
needle1 = "ll"
haystack2 = "aaaaa"
needle2 = "bba"
haystack3 = ""
needle3 = ""

s1 = Solution(haystack1, needle1)
s2 = Solution(haystack2, needle2)
s3 = Solution(haystack3, needle3)

if (s1.strStr()==2):
    print("Pass")
else:
    print("Test 1 Failed")
if (s2.strStr()==-1):
    print("Pass")
else:
    print("Test 2 Failed")
if (s3.strStr()==0):
    print("Pass")
else:
    print("Test 3 Failed")