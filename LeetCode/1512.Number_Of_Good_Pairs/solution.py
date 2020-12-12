#!/usr/bin/python


class Solution:
    def numIdenticalPairs(self, nums):
        res = 0
        hashT = dict()
        for el in nums:
            if el in hashT:
                hashT[el] += 1
            else:
                hashT[el] = 1
        for _, v in hashT.items():
            if v>=2:
                res += v*(v-1)/2
        return int(res)