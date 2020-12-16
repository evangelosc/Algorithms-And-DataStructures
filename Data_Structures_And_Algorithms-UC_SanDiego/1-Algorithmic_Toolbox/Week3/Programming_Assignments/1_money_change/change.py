# Uses python3
import sys

def get_change(m):
    n = 0
    while m:
        if m//10!=0:
            m -= 10
            n += 1
        elif m//5!=0:
            m -= 5
            n += 1
        else:
            m -= 1
            n += 1
    return n

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
