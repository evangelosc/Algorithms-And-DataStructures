#!/usr/bin/python

class Solution:
    def __init__(self):
        pass
    def isRobotBounded(self, instructions: str) -> bool:
        orientation = 1
        pos = [0, 0]
        circle = 4
        for el in instructions:
            if el == "L":
                orientation += 1
                orientation %= circle
            elif el == "R":
                orientation -= 1
                orientation %= circle
            elif el == "G":
                if orientation == 1:
                    pos[1] += 1
                elif orientation == 2:
                    pos[0] -= 1
                elif orientation == 3:
                    pos[1] -= 1
                else:
                    pos[0] += 1
        return orientation != 1 or pos == [0, 0]