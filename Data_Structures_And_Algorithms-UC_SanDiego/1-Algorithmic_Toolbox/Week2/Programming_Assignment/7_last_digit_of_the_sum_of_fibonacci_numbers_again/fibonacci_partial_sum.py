# Uses python3
import sys

def fibonacci_partial_sum_naive(m, n):
    # last digit of the fibonacci numbers, 0 ~ 59 a cycle
    F = [0, 1]
    last = [0, 1]
    for i in range(2, 60):
        F.append(F[i - 1] + F[i - 2])
        last.append(int(str(F[i])[-1]))

    q = int( (n - m + 1) / 60 )

    total = 0
    for i in range((m + q * 60), (n + 1)):
        total = total + last[i % 60]

    return total % 10


if __name__ == '__main__':
    # input = sys.stdin.read();
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))