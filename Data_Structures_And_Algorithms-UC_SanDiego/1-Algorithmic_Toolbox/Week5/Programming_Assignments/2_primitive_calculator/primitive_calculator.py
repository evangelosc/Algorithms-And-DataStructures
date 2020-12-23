# Uses python3
import sys

def minElement(el1, el2, el3):
    minEl = -float("inf")
    if (el1<=el2 and el1<=el3):
        minEl = el1
    if (el2<=el1 and el2<=el3):
        minEl = el2
    if (el3<=el1 and el3<=el2):
        minEl = el3
    return minEl

def optimal_operations(n):
    element = float("inf")
    sequence = list()
    lastSequence = list()
    for i in range(0, 2):
        sequence.append(0)
    for i in range(2, n+2):
        sequence.append(element)
    n2, n3 = 0, 0
    for i in range(n+2):
        lastSequence.append(0)
    for i in range(2, n + 1):
        if i % 3 != 0:
            n3 = element
        else:
            n3 = sequence[(i // 3)]
        if i % 2 != 0:
            n2 = element
        else:
            n2 = sequence[(i // 2)]
        sequence[i] = minElement(sequence[i - 1], n2, n3) + 1
        if sequence[i] == temp_3 + 1:
            lastSequence [i] = (i // 3)
            continue
        if sequence[i] == n2 + 1:
            lastSequence[i] = (i // 2)
            continue
        if sequence[i] == sequence[i - 1] + 1:
            lastSequence[i] = i - 1
    return sequence, lastSequence

def optimal_sequence(lastSequence, n):
    seq = list()
    lastNumber = 0
    seq.append(n)
    i = n
    while i > 1:
        lastNumber = lastNumber[i]
        seq.append(lastNumber)
        i = lastNumber
    return seq.sort()

input = sys.stdin.read()
n = int(input)
sequence, lastSequence = optimal_operations(n)
print(len(sequence) - 1)
seq = optimal_sequence(lastSequence, n)
for x in seq:
    print(x, end=' ')
