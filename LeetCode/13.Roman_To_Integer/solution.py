#!/usr/bin/python

class Solution(object):
    def __init__(self):
        self.roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        self.res = 0
    def setRes(self, val):
        self.res = 0
    def romanToInt(self, s):
        for i in range(len(s)):
            if i+1<len(s) and self.roman_map[s[i]]<self.roman_map[s[i+1]]:
                self.res -= self.roman_map[s[i]]
            else:
                self.res += self.roman_map[s[i]]
        return self.res