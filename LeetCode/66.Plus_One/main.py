#!/usr/bin/python

from solution import Solution

# Unit Test
string1 = [1,2,3]
string2 = [4,3,2,1]
string3 = [9,9]
s = Solution()
if (s.plusOne(string1)==[1,2,4]):
    print("Pass")
else:
    print("Test 1 Failed")
if (s.plusOne(string2)==[4,3,2,2]):
    print("Pass")
else:
    print("Test 2 Failed")
if (s.plusOne(string3)==[1,0,0]):
    print("Pass")
else:
    print("Test 3 Failed")