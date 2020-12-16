# python3
import sys


def compute_min_refills(distance, tank, stops):
    current = 0
    count = 0
    stops = [0] + stops + [distance]
    while current <= len(stops)-2:
        last = current
        while current <= len(stops)-2 and stops[current + 1] - stops[last] <= tank:
            current = current + 1
        if current == last:
            return -1
        if current <= len(stops)-2:
            count = count + 1
    return count

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
