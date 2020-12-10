#!/usr/bin/python

class Solution(object):
    def lengthOfLastWord(self, s):
        firstChar = True
        counter = 0
        for el in reversed(s):
            if el!=" ":
                counter += 1
                firstChar = False
            else:
                if not firstChar:
                    break
        return counter
#    def lengthOfLastWord(self, s: str) -> int:
#         if len(s)==0:
#             return 0
#         if s==" ":
#             return 0
#         if self.singleWord(s):
#             return len(s)
#         current_counter = 0
#         last_counter = 0
#         idx = self.firstWordFound(s)
#         for i in range(idx, len(s)):
#             if s[i]!=" ":
#                 current_counter += 1
#                 last_counter = current_counter
#             else:
#                 current_counter = 0
#         return last_counter
    
#     def firstWordFound(self, s):
#         idx = 0
#         for idx in range(len(s)):
#             if s[idx]!=" ":
#                 return idx
#         return idx
        
        
#     def singleWord(self, s):
#         singleWord = True
#         for el in s:
#             if el==" ":
#                 singleWord = False
#         return singleWord
        