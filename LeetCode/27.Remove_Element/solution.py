#!/usr/bin/python

class Solution(object):
    def __init__(self):
        self.i = 0
    
    def reset_i(self, val):
        self.i = val

    def removeElement(self, nums, val):
        i = 0
        while(i<len(nums)):
            if nums[i]==val:
                del nums[i]
            else:
                i += 1
        return len(nums)