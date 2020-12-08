#!/usr/bin/python
from solution import Solution

# Unit Test

s = Solution()
if (s.romanToInt("IV") == 4):
    print("Pass")
    s.setRes(0)
else:
    print("Failed - IV")
if (s.romanToInt("IX") == 9):
    print("Pass")
    s.setRes(0)
else:
    print("Failed - IX")
if (s.romanToInt("XL") == 40):
    print("Pass")
    s.setRes(0)
else:
    print("Failed - XL")
if (s.romanToInt("XC") == 90):
    print("Pass")
    s.setRes(0)
else:
    print("Failed - XC")
if (s.romanToInt("CD") == 400):
    print("Pass")
    s.setRes(0)
else:
    print("Failed - CD")
if (s.romanToInt("CM") == 900):
    print("Pass")
    s.setRes(0)
else:
    print("Failed - CM")
if (s.romanToInt("MMXIV") == 2014):
    print("Pass")
    s.setRes(0)
else:
    print("Failed - MMXIV")
if (s.romanToInt("MDCCCLXXXIV") == 1884):
    print("Pass")
    s.setRes(0)
else:
    print("Failed -MDCCCLXXXIV")
    