#!/usr/bin/python
class Solution(object):
    def judgeCircle(self, moves: str) -> bool:
        x_prime_x = 0
        y_prime_y = 0
        for el in moves:
            if el == "R":
                x_prime_x += 1
            if el == "L":
                x_prime_x -= 1
            if el == "U":
                y_prime_y += 1
            if el == "D":
                y_prime_y -= 1
        if x_prime_x == 0 and y_prime_y == 0:
            return True
        return False