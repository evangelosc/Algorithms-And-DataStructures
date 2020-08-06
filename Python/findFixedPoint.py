# Given an array of n distinct integers sorted in ascending order, 
# write a function that returns a "fixed point" in the array. 
# If there is not a fixed point return "None".

# A fixed point in an array "A" is an index "i" such that A[i] is equal to "i".

def isFixedPoint(lista):
    # Time: O(N)
    # Space: O(1)
    for i in range(len(lista)-1):
        if lista[i] == i:
            return lista[i]
    return None

print(isFixedPoint([-10,-5,0,3,7]))
print(isFixedPoint([-10,-5,3,4,7,9]))

def binaryFixedPoint(lista):
    # Time: O(logN)
    # Space: O(1)
    low = 0
    high = len(lista)-1
    if len(lista) == 0:
        return None
    while low <= high:
        mid = low + (high-low)//2
        if mid < lista[mid]:
            high = mid - 1
        elif mid > lista[mid]:
            low = mid + 1
        else:
            return lista[mid]
    return None

print(binaryFixedPoint([-10,-5,0,3,7]))
print(binaryFixedPoint([-10,-5,3,4,7,9]))
# print(binaryFixedPoint([2,1,11]))