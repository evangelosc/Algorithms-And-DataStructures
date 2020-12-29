#!/usr/bin/python

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashT = dict()
        idx = 0
        for el in nums:
            if el not in hashT:
                hashT[el] = idx
            else:
                if (idx - hashT[el]) <= k:
                    return True
                hashT[el] = idx
            idx += 1
        return False