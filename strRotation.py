# Problem:
# String Rotation: Given two strings, s1 and s2, write code to check 
# if s2 is a rotation of s1 (e.g. "waterbottle" is a rotation of "erbottlewat").

def strRotation(s1,s2):
    if len(s1) != len(s2):
        return False
    s1 = s1.lower()
    s2 = s2.lower()
    hashT = dict()
    for el in s1:
        if el in hashT:
            hashT[el] += 1
        else:
            hashT[el] = 1
    for el in s2:
        if el in hashT:
            hashT[el] -= 1
        else:
            return False
    return True

