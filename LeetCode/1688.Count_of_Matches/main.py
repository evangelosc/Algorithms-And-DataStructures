#!/usr/bin/python
from solution import Solution

# Unit Test

solutionObject = Solution()
if (solutionObject.numberOfMatches(14) == 13):
    print("PASS")
else:
    print("FAILED")
if (solutionObject.numberOfMatches(7) == 6):
    print("PASS")
else:
    print("FAILED")