# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments.sort()
    n = len(segments)
    current = 0
    while (current<n):
        last = current
        while current<n-1 and segments[current+1][0] <= segments[last][1]:
            current += 1
            if (segments[current][1]<segments[last][1]):
                last = current
        points.append(segments[last][1])
        current += 1
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
