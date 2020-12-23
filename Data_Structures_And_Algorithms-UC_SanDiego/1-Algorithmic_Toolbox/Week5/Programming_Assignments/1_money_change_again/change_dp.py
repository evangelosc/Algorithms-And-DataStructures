# Uses python3
import sys

def get_change(m):
    element = float("inf")
    minCoins = list()
    sumCoins = 0
    coins = [1,3,4]
    minCoins[0] = 0
    for i in range(1, m+2):
        minCoins.append(element)
    for i in range(1, m + 1):
        for el in coins:
            if i >= el:
                sumCoins = minCoins[i - el] + 1
                if sumCoins < minCoins[i]:
                    minCoins[i] = sumCoins
    return minCoins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
