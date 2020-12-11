#!/usr/bin/python

class Solution(object):
    def shuffle(self, nums, n):
        res = list()
        for i in range(len(nums)//2):
            res.append(nums[i])
            res.append(nums[i+n])
        return res