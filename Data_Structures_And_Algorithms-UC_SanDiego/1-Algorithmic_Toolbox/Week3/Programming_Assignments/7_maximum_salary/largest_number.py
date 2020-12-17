#Uses python3

import sys

def largest_number(lst):
    n = len(lst)
    for i in range(n - 1):
        for i in range(n - 1 - i):
            if lst[i] + lst[i+1] < lst[i + 1] + lst[i]:
                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
    res = ""
    for d in lst:
        res += d
    return res

if __name__ == '__main__':
    n = int(input())
    data = input().split()
    print(largest_number(data))
    
