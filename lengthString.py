# Given a string, calculate its length recursively. 
def lengthString(newStr):
    count = 0
    for _ in newStr:
        count += 1
    return count


def lengthStringRec(newStr):
    if newStr == "":
        return 0
    return 1 + lengthStringRec(newStr[1:])

print(lengthString("012345"))
print(lengthStringRec("012345"))