# Problem: Implement an algorithm to determine if a string has all unique characters. 
s1 = 'unique'
s2 = 'bear'

print(len(s2) == len(set(s2)))

def uniqueHash(theStr):
    # Time: O(N)
    # Space: O(N)
    hashT = dict()
    for el in theStr:
        if el in hashT:
            return False
        else:
            hashT[el] = 1
    return True

print(uniqueHash(s1))