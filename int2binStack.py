from stack import stack

def int2bin(num):
    s = stack()

    while num > 0:
        reminder = num%2
        s.push(reminder)
        num = num//2
    
    binaryStr = ''
    while not s.is_empty():
        binaryStr += str(s.pop())

    return binaryStr


res = int2bin(242)
print(res)
