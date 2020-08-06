# Problem: Given two strings, write a function to decide 
# if one is a permutation of the other. 

s1 = 'racecar'
s2 = "Dammit I'm mad."
s3 = 'madam'

class stack(object):
    def __init__(self):
        self.items = list()
    def push(self, element):
        self.items.append(element)
    def pop(self):
        if not self.isempty():
            return self.items.pop()
    def isempty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.isempty():
            return self.items[-1]


import string
def isPalindrome(s1):
    if len(s1) < 2 or not s1.isalpha():
        return False
    s1 = s1.replace(' ', '').lower()
    s1 = s1.translate(str.maketrans('', '', string.punctuation))
    theStack = stack()
    for el in s1:
        theStack.push(el)
    for el in s1:
        if not el == theStack.pop():
            return False
    return True

print(isPalindrome(s3))