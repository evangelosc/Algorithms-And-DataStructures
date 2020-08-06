# Specifically, we want to solve the problem:
# Given two strings, write a function to determine 
# if one is a permutation of the other. 

# We solve this problem in Python and analyze the time and 
# space complexity of our approach. 

s1 = 'dog'
s2 = 'god'

def isPermuation(s1,s2):
    # Time: O(N)
    # Space: O(N)
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
            hashT[el] -=1
        else:
            hashT[el] = 1
    return all(value==0 for value in hashT.values())

print(isPermuation(s1,s2))