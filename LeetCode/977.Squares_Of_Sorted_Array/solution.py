#!/usr/bin/python

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = list()
        for el in nums:
            res.append(el**2)
        return sorted(res)