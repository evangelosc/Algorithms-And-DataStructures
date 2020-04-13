# Given two arrays, A and B, determine their intersection. 
# That is, what elements are common to A and B?
A = [1,2,3,5,7,9,11,14,16]
B = [3,4,5,6,10,11]
import time
print(set(A).intersection(B))
def intersectionTwoArray(A, B):
    time1 = time.time()
    hashT = dict() 
    for el in A:
        if el in hashT:
            hashT[el] += 1
        else:
            hashT[el] = 1
    for el in B:
        if el in hashT:
            hashT[el] = 'found'
        else:
            hashT[el] = 1
    for key, values in hashT.items():
        if values == 'found':
            print(key)
    print(time.time()-time1)

def intersectionTwoArrayLinear(A,B):
    time1 = time.time()
    a = 0
    b = 0
    intersection = list()
    while a<len(A) and b<len(B):
        if A[a] == B[b]:
            if a == 0 or A[a] != A[a-1]:
                intersection.append(A[a])
            a += 1
            b += 1
        elif A[a] < B[b]:
            a += 1
        else:
            b += 1
    print(time.time() - time1)
    return intersection

intersectionTwoArray(A,B)
# intersectionTwoArrayLinear(A,B)