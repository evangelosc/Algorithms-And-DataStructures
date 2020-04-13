A = [6,7,5,5,2,3]

def tasksPrint(A):
    A = sorted(A)
    for i in range(len(A)//2):
        print(A[i], A[~i])

tasksPrint(A)