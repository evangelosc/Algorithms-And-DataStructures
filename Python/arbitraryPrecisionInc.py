# # %%
# A = [1,4,9]
# s = ''.join(map(str, A))
# print(int(s)+1)

def incF(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] = A[i-1] + 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

print(incF([9,9,9]))