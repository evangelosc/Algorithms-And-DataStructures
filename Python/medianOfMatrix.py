# Problem:
# We are given a row-wise sorted matrix of size r*c, 
# we need to find the median of the matrix given. 
# It is assumed that r*c is always odd.

def medianOfMatrix(A):
    if len(A) == 1:
        vec = A[0]
        return vec[len(vec)//2]
    else:
        newL = list()
        for i in range(len(A)):
            newL.extend(A[i])
        newL = sorted(newL)
    return newL[len(newL)//2]



l1 = [1,3,5]
l2 = [2,6,9]
l3 = [3,6,9]
A = [l1,l2,l3]
print(medianOfMatrix(A))