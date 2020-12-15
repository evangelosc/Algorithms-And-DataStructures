# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    # last digit of the fibonacci numbers, 0 ~ 59 a cycle
    F = [0, 1]
    last = [0, 1]
    for i in range(2, 60):
        F.append(F[i - 1] + F[i - 2])
        last.append(int(str(F[i])[-1]))

    res = last[n % 60] * last[n % 60] + last[n % 60] * last[(n - 1) % 60]

    return res % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))
