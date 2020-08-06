def nonRepeating(s1):
    hashT = dict()
    for i in range(len(s1)):
        if s1[i] in hashT:
            hashT[s1[i]] += 1
        else:
            hashT[s1[i]] = 1
    for keyes, values in hashT.items():
        if values == 1:
            return keyes
print(nonRepeating("abcbad"))