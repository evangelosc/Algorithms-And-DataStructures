# In this video, we will be considering how to determine 
# if a string has all unique characters. One approach to this problem 
# may be to use an additional data structure, like a hash table. 
# We will consider how one may solve this problem without the use 
# of such a data structure. We'll present a number of solutions 
# to this problem and give a rough time and space complexity analysis of each approach.

uniqueStr = 'AbCDefG'
nonUniqueStr = 'non Unique STR'

def isUnique(theStr):
    # Time: O(N)
    # Space: O(N)
    theStr = theStr.replace(' ', '').lower()
    if len(theStr) < 2:
        return False
    hashT = dict()
    for el in theStr:
        if el in hashT:
            return False
        else:
            hashT[el] = 1
    return True

def isUniqueNoHash(theStr):
    # Time: O(NlogN)
    # Space: O(1)
    theStr = theStr.replace(' ', '').lower()
    theStr = sorted(theStr)
    prev = None
    for el in theStr:
        if el == prev:
            return False
        prev = el
    return True

def isUniqueSet(theStr):
    return len(set(theStr)) == len(theStr)

print(isUnique(uniqueStr))
print(isUniqueNoHash(uniqueStr))
print(isUniqueSet(uniqueStr))