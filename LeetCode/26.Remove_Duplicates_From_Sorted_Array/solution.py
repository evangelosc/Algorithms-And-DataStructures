#!/usr/bin/python
from itertools import groupby

class Solution(object):
    def __init__(self):
        self.i = 0
        
    def reset_i(self, val):
        self.i = val

    def removeDuplicates(self, nums):
        for k, _ in groupby(nums):
            nums[self.i] = k
            self.i += 1
        return self.i