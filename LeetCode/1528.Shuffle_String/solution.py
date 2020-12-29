#!/usr/bin/python

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        finale = list()
        for i in range(len(indices)):
            finale.append("")
        for i in range(len(indices)):
            finale[indices[i]] = s[i]
        res = ""
        for el in finale:
            res += el
        return res