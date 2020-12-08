#!/usr/bin/python
from solution import Solution

# Unit Test

solutionObject = Solution()
print(solutionObject.isValid("()"))
print(solutionObject.isValid("()[]{}"))
print(solutionObject.isValid("(]"))
print(solutionObject.isValid("([)]"))
