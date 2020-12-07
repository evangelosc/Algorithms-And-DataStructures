#!/usr/bin/python

class Solution(object):
    def __init__(self):
        self.buff = dict()
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if nums[i] in self.buff:
                return self.buff[nums[i]], i
            else:
                self.buff[target-nums[i]] = i

     