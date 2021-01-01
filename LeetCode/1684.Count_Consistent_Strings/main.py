#!/usr/bin/python
from solution import Solution

# Unit Test

solutionObject = Solution()
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
if (s.countConsistentStrings(allowed, words) == 2):
    print("PASS")
else:
    print("FAILED")