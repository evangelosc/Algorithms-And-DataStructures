A = [-2,1,2,4,7,11]
target = 13

def twoSumBruteForce(A, target):
    # Time: O(N^2)
    # Space: O(1) we do not store anything
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i]+A[j]==target:
                print(A[i], A[j])
                return True
    return False

# print(twoSumBruteForce(A, target))

def twoSumHashTable(A, target):
    # Time: O(N)
    # Space: O(N)
    hashTable = dict()
    for i in range(len(A)):
        if A[i] in hashTable:
            print(hashTable[A[i]], A[i])
            return True
        else:
            hashTable[target-A[i]] = A[i]
    return False

# print(twoSumHashTable(A, target))

def twoSumIterators(A, target):
    # Time: O(N)
    # Space: O(1)
    i = 0
    j = len(A)-1
    while i<=j:
        if A[i]+A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i]+A[j] < target:
            i += 1
        else:
            j -= 1
    return False

print(twoSumIterators(A, target))