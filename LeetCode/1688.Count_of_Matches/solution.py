#!/usr/bin/python

class Solution(object):
    def numberOfMatches(self, n):
        sum_teams = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
                sum_teams += n                
            else:
                n //= 2 
                sum_teams += n + 1
        return sum_teams