#!/usr/bin/python
import random

class Solution(object):
    def getRandom(self, lista):
        totalNums = 0
        for ranges in lista:
            totalNums += ranges[1] - ranges[0] + 1
        randomNumber = random.randint(0, totalNums-1)
        for ranges in lista:
            currentRange = ranges[1] - ranges[0] + 1
            if randomNumber < currentRange:
                answer = ranges[0] + randomNumber
            else:
                randomNumber -= currentRange
        return answer