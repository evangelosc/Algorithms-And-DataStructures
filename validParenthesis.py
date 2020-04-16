class stack(object):
    def __init__(self):
        self.items = list()
    def push(self,element):
        self.items.append(element)
    def isEmpty(self):
        return len(self.items) == 0
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

def match(s1,s2):
    if s1=="(" and s2==")":
        return True
    elif s1=="[" and s2=="]":
        return True
    elif s1=="{" and s2=="}":
        return True
    return False


def validParenthesis(s1):
    theStack = stack()
    balance = True
    for el in s1:
        if el in "({[":
            theStack.push(el)
        else:
            if not match(theStack.pop(),el):
                balance = False
    return balance

print(validParenthesis("{[())]}"))