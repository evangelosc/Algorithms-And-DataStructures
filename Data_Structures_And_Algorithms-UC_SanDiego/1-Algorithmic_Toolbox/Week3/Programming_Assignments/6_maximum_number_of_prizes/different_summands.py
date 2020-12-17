# Uses python3
import sys

def optimal_summands(n):
    summands = []
    i = 0
    while n > 0:
        i += 1
        if n - i <= i:
            i = n
        summands.append(i)
        n -= i
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
