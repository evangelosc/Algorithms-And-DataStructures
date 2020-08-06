# You are given some integer as input, (i.e. ... -3, -2, -1, 0, 1, 2, 3 ...)
# Convert the integer you are given to a string. Do not make use
# of the built-in "str" function.
# Examples:
#     Input: 123
#     Output: "123"
#     Input: -123
#     Output: "-123"

def integerToStr(num):
    if num < 0:
        isNegative = True
        num *= -1
    else:
        isNegative = False
    theOut = list()
    while num > 0:
        theOut.append(chr(ord('0') + num%10))
        num //= 10
    theOut = theOut[::-1]
    theOut = ''.join(theOut)
    if isNegative:
        return '-' + theOut
    else:
        return theOut


print(integerToStr(-123))