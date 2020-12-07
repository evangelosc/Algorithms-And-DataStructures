#!/usr/bin/python

class Solution(object):
    def __init__(self):
        self.minS = ""
        self.prefix = ""

    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        self.minS = min(strs)
        self.prefix = ""
        # Loop through characters of smallest string
        for i in range(len(self.minS)):
            count = 0
            # Loop through strings in list
            for j in range(len(strs)):
                # If string starts with same letters as 'self.minS' up to index i, increment count
                if (strs[j].startswith(self.minS[:i+1])):
                    count+=1
                else:
                    count = 0
                    break
                # If all strings in list have same self.prefix up to index i as self.minS, add character @ i to self.prefix
                if (count == len(strs)):
                    self.prefix += self.minS[i]
        return self.prefix
        