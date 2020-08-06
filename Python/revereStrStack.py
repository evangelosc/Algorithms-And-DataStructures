# Reverse a String in Python reverseStr[::-1]
from stack import stack

def reverseString(stack, strInput):
    for i in range(len(strInput)):
        stack.push(strInput[i])
    revString = ''
    while not stack.is_empty():
        revString += stack.pop()
    return revString

ourStack = stack()
theReversed = reverseString(ourStack, 'Maria')
print(theReversed)