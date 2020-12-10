#!/usr/bin/python


class Solution(object):
    def addBinary(self, a, b):
        a_dec = self.binary2decimal(a)
        if (len(str(a_dec))==0): a_dec="0"
        b_dec = self.binary2decimal(b)
        if (len(str(b_dec))==0): b_dec="0"
        c_dec = int(a_dec) + int(b_dec)
        if (len(str(c_dec))==0): c_dec="0"
        c_bin = self.decimal2binary(c_dec)
        if (len(str(c_bin))==0): c_bin="0"
        return c_bin

    def binary2decimal(self, a):
        tmp = list(a)
        res = 0
        for i in range(len(tmp)):
            digit = tmp.pop()
            if digit==str(1):
                res += 2**i
        return res
    
    def decimal2binary(self, a):
        res = list()
        while(a>=1):
            res.append(a%2)
            a = a//2
        string = ""
        for el in reversed(res):
            string += str(el)
        return string
            
        