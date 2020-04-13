# Problem:
# Given two strings, check whether two given strings are an anagram 
# of each other or not. An anagram of a string is another string 
# that contains same characters, only the order of characters can be different. 
# For example, “act” and “tac” are an anagram of each other.

s1 = 'practise makes perfect'
s2 = 'perfect makes practise'
s3 = 'allergy'
s4 = 'allergic'

def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if not s1.isalpha() and not s2.isalpha():
        return False
    hasht = dict()
    for el in s1:
        if el in hasht:
            hasht[el] += 1
        else:
            hasht[el] = 1
    for el in s2:
        if el in hasht:
            hasht[el] -= 1
        else:
            return False
    return True

print(isAnagram(s1,''))