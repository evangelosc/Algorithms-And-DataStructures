def luckyNum(matrix):
    minList = list()
    maxList = list()
    for row in matrix:
        minList.append(min(row))
    for col in map(list, zip(*matrix)):
        maxList.append(max(col))
    if set(maxList) & set(minList):
        return set(maxList) & set(minList)
    else:
        return None

print(luckyNum([[3,7,8],[9,11,13],[15,16,17]]))