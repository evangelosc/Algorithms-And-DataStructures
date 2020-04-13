# Problem:
# Given an array of numbers consisting of daily stock prices,
# calculate the maximum amount of profit that can be made from 
# buying on one day and selling on another day.

A = [310,315,275,295,260,270,290,230,255,250]

def buyNSell(A):
    # Time: O(N^2)
    # Space: O(1)
    maxProfit = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[j]-A[i]>maxProfit:
                maxProfit = A[j]-A[i]
    return maxProfit

# print(buyNSell(A))

def buyNSell2(A):
    # Time: O(N)
    # Space: O(1)
    minValue = A[0]
    maxProfit = 0
    for i in range(len(A)):
        minValue = min(minValue, A[i])
        profit = A[i] - minValue
        maxProfit = max(maxProfit, profit)
    return maxProfit

print(buyNSell2(A))