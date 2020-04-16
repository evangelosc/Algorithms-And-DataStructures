def sortedArray(lista):
    res = list()
    low = 0
    high = len(lista)-1
    for i in range(len(lista)):
        res.append(0)
    for i in range(len(lista)-1,-1,-1):
        if abs(lista[low]) > lista[high]:
            res[i] = lista[low]*lista[low]
            low += 1
        else:
            res[i] = lista[high]*lista[high]
            high -= 1
    return res
print(sortedArray([-7,-3,-1,4,8,12]))