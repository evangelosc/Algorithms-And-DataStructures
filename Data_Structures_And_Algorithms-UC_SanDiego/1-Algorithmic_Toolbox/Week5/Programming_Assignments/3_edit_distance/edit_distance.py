# Uses python3

def minElement(el1, el2, el3):
    minEl = -float("inf")
    if (el1<=el2 and el1<=el3):
        minEl = el1
    if (el2<=el1 and el2<=el3):
        minEl = el2
    if (el3<=el1 and el3<=el2):
        minEl = el3
    return minEl

def edit_distance(s, t):
    element = float("inf")
    distance = 0
    tmpVec = list()
    D = list(list())
    for i in range(len(t)+1):
        tmpVec.append(element)
    for i in range(len(s)+1):
        D.append(tmpVec)
    for i in range(len(s) + 1):
        D[i][0] = i
    for i in range(len(t) + 1):
        D[0][i] = i
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                distance = 0
            else:
                distance = 1
            D[i][j] = minElement(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + distance)
    return D[len(s)][len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
