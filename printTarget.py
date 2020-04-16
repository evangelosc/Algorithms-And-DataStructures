def target(lista, target):
    hashT = dict()
    for el in lista:
        if el in hashT:
            hashT[el] += 1
        else:
            hashT[el] = 1
    for i in range(len(lista)-1):
        if lista[i] in hashT:
            if (target-lista[i]) > 0 and (target-lista[i]) in hashT:
                return (abs(target-lista[i]), lista[i])
    return ("No valid pairs.")
print(target([14,13,6,7,8,10,1,2],-63))