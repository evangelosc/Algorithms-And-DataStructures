#!/usr/bin/python


class Solution(object):
    def __init__(self):
        pass
    def maxSubArray(self, nums):
        if len(nums)==1:
            return nums[0]
        currentSum = 0
        maxSumSeen = nums[0]
        for el in nums:
            currentSum = max(el, currentSum+el)
            maxSumSeen = max(currentSum, maxSumSeen)
        return maxSumSeen