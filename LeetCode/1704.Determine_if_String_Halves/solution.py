#!/usr/bin/python


class Solution(object):
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        pivot = len(s)//2
        if self.counterVowels(s[:pivot]) == self.counterVowels(s[pivot:]):
            return True
        return False
    
    def counterVowels(self, s):
        print(s)
        solution = ['a', 'e', 'i', 'o', 'u']
        counter = 0
        for el in s:
            if el in solution:
                counter += 1
        return counter