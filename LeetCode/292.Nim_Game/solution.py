#!/usr/bin/python

class Solution:
    def canWinNim(self, n: int) -> bool:
        flag = [True, True, True, True]
        if (n<=3):
            return True
        i = 4
        while(i<=n):
            tmp1 = not flag[1]
            tmp2 = not flag[2] 
            tmp3 = not flag[3]
            
            flag[0] = tmp1 or tmp2 or tmp3
            
            flag[3] = flag[2]
            flag[2] = flag[1]
            flag[1] = flag[0]            
            i += 1
        return flag[0]