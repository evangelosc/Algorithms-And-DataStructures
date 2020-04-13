# You are given some numeric string as input. Convert the string you are
# given to an integer. Do not make use of the built-in "int" function.
# Example:
#     "123" : 123
#     "-12332" : -12332
#     "554" : 554
#     etc.

def strToInt(theStr):
    if not theStr.isnumeric():
        return False
    if theStr[0] == '-':
        startLoop = 1
        isNegative = True
    else:
        startLoop = 0
        isNegative = False
    theResult = 0
    for i in range(startLoop, len(theStr)):
        base = 10**(len(theStr) - (i+1))
        num = ord(theStr[i]) - 48
        theResult += base*num
    if isNegative:
        return -1*theResult
    return theResult

print(strToInt('3'))