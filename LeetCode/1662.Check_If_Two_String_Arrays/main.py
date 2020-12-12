#!/usr/bin/python

from solution import Solution

# Unit Test
word1 = ["ab", "c"]
word2 = ["a", "bc"]

word11 = ["a", "cb"]
word22 = ["ab", "c"]

s = Solution()
if (s.numIdenticalPairs(word1, word2) == True):
    print("Pass")
else:
    print("Test 1 Failed")
if (s.numIdenticalPairs(word11, word22) == False):
    print("Pass")
else:
    print("Test 2 Failed")