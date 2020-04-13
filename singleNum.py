# Problem: Given an array of integers, every element appears twice 
# except for one. Find that single one.

# Note: Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

def singleNum(num):
    # Time: O(N)
    # Space: O(N)
    if len(num) < 4:
        return False
    hashT = dict()
    for el in num:
        if el in hashT:
            hashT[el] += 1
        else:
            hashT[el] = 1
    for keys, values in hashT.items():
        if values == 1:
            return keys
    return False

print(singleNum([1,2,2,3,1]))

def xorNumber(num):
    if len(num) < 4:
        return False
    result = 0
    for el in num:
        result ^= el
    return result

print(xorNumber([1,2,2,3,1]))