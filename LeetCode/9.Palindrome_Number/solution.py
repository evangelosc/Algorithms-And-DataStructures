#!/usr/bin/python

class Solution(object):
    def __init__(self):
        self.given = 0
        self.dig = 0
        self.rev = 0

    def isPalindrome(self, num):
        self.given = num
        while (num>0):
            self.dig = num%10
            self.rev = self.rev*10 + self.dig
            num //= 10
        if self.rev == self.given:
            return True
        return False