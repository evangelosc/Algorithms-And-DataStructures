#!/usr/bin/python

class Solution(object):
    def __init__(self, haystack, needle):
        self.haystack = haystack
        self.needle = needle

    def strStr(self):
        if len(self.needle)==0:
            return 0
        if len(self.needle) > len(self.haystack):
            return -1
        s = 0
        f = len(self.needle)-1
        while(f<len(self.haystack)):
            if self.haystack[s:f+1]!=self.needle:
                s += 1
            else:
                return s
            f += 1
        return -1