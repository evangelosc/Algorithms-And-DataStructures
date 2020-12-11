#!/usr/bin/python
from solution import Solution

# Unit Test
string1 = "A man, a plan, a canal: Panama"
string2 = "race a car"
s = Solution()
if (s.isPalindrome(string1)==True):
    print("PASS")
else:
    print("TEST 1 FAILED")

if (s.isPalindrome(string2)==False):
    print("PASS")
else:
    print("TEST 2 FAILED")