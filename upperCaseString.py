# Given a string, develop an algorithm to return the first occurring uppercase letter. 
# We require both an iterative and recursive solution to this problem. 

# For instance, for the strings:

# str_1 = "lucidProgramming"
# str_2 = "LucidProgramming"
# str_3 = "lucidprogramming"

# The algorithm should return "P", "L", and output a message 
# indicating no such capital letter found, respectively for the above strings.

def upperCaseString(inputStr):
    for x in inputStr:
        if x.isupper():
            return x
    return ("No uppercase string")


def upperCaseStringRec(inputStr, idx=0):
    if inputStr[idx].isupper():
        return inputStr[idx]
    if idx == len(inputStr)-1:
        return ("No uppercase string")
    return upperCaseStringRec(inputStr, idx+1)

str_1 = "lucidProgramming"
str_2 = "LucidProgramming"
str_3 = "lucidprogramming"
print(upperCaseString(str_1))
print(upperCaseString(str_2))
print(upperCaseString(str_3))
print(upperCaseStringRec(str_1))
print(upperCaseStringRec(str_2))
print(upperCaseStringRec(str_3))