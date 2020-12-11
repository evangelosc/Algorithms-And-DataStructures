#!/usr/bin/python


class Solution(object):
    def isPalindrome(self, s):
        if len(s)==0:
            return True
        res = ""
        for el in s:
            if el.isalnum():
                res += el
        res = res.lower()
        first = 0
        last = len(res)-1
        while(first<=last):
            if res[first]!=res[last]:
                return False
            first += 1
            last -= 1
        return True