# Given two strings figure out if they are equal
# the '#' char represents the backspace char

def remove(theStr):
    # Time: O(N)
    # Space: O(N)
    newStr = ''
    for el in theStr:
        if el == '#':
            if len(el):
                newStr = newStr[:-1]
        else:
            newStr += el
    return newStr

print(remove('a#c') == remove('b'))
