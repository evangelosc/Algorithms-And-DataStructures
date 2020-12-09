#!/usr/bin/python

class Solution(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        self.first = 0
        self.last = len(nums) - 1
        self.m = self.first+self.last // 2
    
    def resetAll(self):
        self.first = 0
        self.last = len(self.nums) - 1
        self.m = self.first+self.last // 2

    def searchInsert(self):
        self.first = 0
        self.last = len(self.nums)-1
        while (self.first<=self.last):
            self.m = (self.first+self.last)//2
            if (self.nums[self.m]>=self.target):
                self.last = self.m - 1
            if (self.nums[self.m]<self.target):
                self.first = self.m + 1
        if self.nums[self.m]<self.target:
            return self.m+1
        return self.m