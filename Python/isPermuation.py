# Problem: Given two strings, write a function to decide 
# if one is a permutation of the other. 

s1 = 'driving'
s2 = 'drivign'
s3 = 'ddriving'

def isPermu(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')
    for el in s1:
        if el in s2:
            s2 = s2.replace(el, '')
    return len(s2)==0
print(isPermu(s1,s2))
print(isPermu(s1,s3))

def isPermuation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')
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
    # for _, values in hashT.items():
    #     if values != 0:
    #         return False
    # return True

print(isPermuation(s1,s2))

