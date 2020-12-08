#!/usr/bin/python

class Solution(object):
    def __init__(self):
        self.stack = list()
        self.map_pairs = {'(': ')', '[': ']', '{': '}'}
    def isValid(self, s):
        for el in s:
            if el in self.map_pairs:
                self.stack.append(self.map_pairs[el])
            else:
                if len(self.stack)==0 or self.stack.pop()!=el:
                    return False
        return len(self.stack)==0