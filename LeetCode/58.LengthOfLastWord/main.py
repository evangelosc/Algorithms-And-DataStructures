#!/usr/bin/python

from solution import Solution

# Unit Test
string1 = "Hello World"
string2 = " "
string3 = " a"
s = Solution()
if (s.lengthOfLastWord(string1)==5):
    print("Pass")
else:
    print("Test 1 Failed")
if (s.lengthOfLastWord(string2)==0):
    print("Pass")
else:
    print("Test 2 Failed")
if (s.lengthOfLastWord(string3)==1):
    print("Pass")
else:
    print("Test 3 Failed")