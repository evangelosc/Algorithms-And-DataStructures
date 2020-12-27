#!/usr/bin/python
from solution import Solution

# Unit Test

solutionObject = Solution()
if (solutionObject.halvesAreAlike("book") == True):
    print("PASS")
else:
    print("FAILED")
if (solutionObject.halvesAreAlike("textbook") == False):
    print("PASS")
else:
    print("FAILED")